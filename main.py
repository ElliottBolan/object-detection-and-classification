"""
Object Detection and Classification Application
State-of-the-art multi-object detection using YOLOv8 and classification
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import numpy as np
from ultralytics import YOLO
import torch
from torchvision import models, transforms
import os

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ObjectDetectionApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Object Detection & Classification System")
        self.window.geometry("1400x900")
        
        # Initialize models
        self.detection_model = None
        self.classification_model = None
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Video/Camera variables
        self.video_path = None
        self.cap = None
        self.is_running = False
        self.use_camera = False
        
        # Detection settings
        self.confidence_threshold = 0.5
        self.show_classification = True
        
        # Initialize UI
        self.setup_ui()
        self.load_models()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        self.main_container = ctk.CTkFrame(self.window)
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Title
        title = ctk.CTkLabel(
            self.main_container,
            text="🎯 Object Detection & Classification System",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(pady=10)
        
        # Control panel (left side)
        self.control_panel = ctk.CTkFrame(self.main_container, width=300)
        self.control_panel.pack(side="left", fill="y", padx=(0, 10))
        self.control_panel.pack_propagate(False)
        
        self.setup_controls()
        
        # Video display (right side)
        self.video_frame = ctk.CTkFrame(self.main_container)
        self.video_frame.pack(side="right", fill="both", expand=True)
        
        self.video_label = ctk.CTkLabel(self.video_frame, text="No video loaded")
        self.video_label.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Status bar
        self.status_bar = ctk.CTkLabel(
            self.window,
            text="Ready | Device: " + self.device.upper(),
            font=ctk.CTkFont(size=12)
        )
        self.status_bar.pack(side="bottom", fill="x", padx=10, pady=5)
        
    def setup_controls(self):
        """Setup control panel widgets"""
        # Section: Video Source
        source_label = ctk.CTkLabel(
            self.control_panel,
            text="📹 Video Source",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        source_label.pack(pady=(20, 10))
        
        # Camera button
        self.camera_btn = ctk.CTkButton(
            self.control_panel,
            text="Use Camera",
            command=self.select_camera,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.camera_btn.pack(pady=5, padx=20, fill="x")
        
        # Select video button
        self.select_btn = ctk.CTkButton(
            self.control_panel,
            text="Select Video File",
            command=self.select_video,
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.select_btn.pack(pady=5, padx=20, fill="x")
        
        # Section: Detection Settings
        settings_label = ctk.CTkLabel(
            self.control_panel,
            text="⚙️ Settings",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        settings_label.pack(pady=(30, 10))
        
        # Confidence threshold
        conf_label = ctk.CTkLabel(
            self.control_panel,
            text="Confidence Threshold",
            font=ctk.CTkFont(size=12)
        )
        conf_label.pack(pady=(10, 0))
        
        self.conf_slider = ctk.CTkSlider(
            self.control_panel,
            from_=0.1,
            to=0.9,
            number_of_steps=8,
            command=self.update_confidence
        )
        self.conf_slider.set(0.5)
        self.conf_slider.pack(pady=5, padx=20, fill="x")
        
        self.conf_value_label = ctk.CTkLabel(
            self.control_panel,
            text="0.5",
            font=ctk.CTkFont(size=12)
        )
        self.conf_value_label.pack()
        
        # Classification toggle
        self.classification_switch = ctk.CTkSwitch(
            self.control_panel,
            text="Enable Classification",
            command=self.toggle_classification,
            font=ctk.CTkFont(size=12)
        )
        self.classification_switch.select()
        self.classification_switch.pack(pady=10, padx=20)
        
        # Section: Controls
        controls_label = ctk.CTkLabel(
            self.control_panel,
            text="🎮 Controls",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        controls_label.pack(pady=(30, 10))
        
        # Start button
        self.start_btn = ctk.CTkButton(
            self.control_panel,
            text="▶ Start Detection",
            command=self.start_detection,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="green",
            hover_color="darkgreen"
        )
        self.start_btn.pack(pady=10, padx=20, fill="x")
        
        # Stop button
        self.stop_btn = ctk.CTkButton(
            self.control_panel,
            text="⏸ Stop Detection",
            command=self.stop_detection,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="red",
            hover_color="darkred",
            state="disabled"
        )
        self.stop_btn.pack(pady=10, padx=20, fill="x")
        
        # Info section
        info_frame = ctk.CTkFrame(self.control_panel)
        info_frame.pack(side="bottom", pady=20, padx=20, fill="x")
        
        info_text = ctk.CTkLabel(
            info_frame,
            text="ℹ️ Info\n\nYOLOv8 Detection\n+\nImageNet Classification",
            font=ctk.CTkFont(size=11),
            justify="center"
        )
        info_text.pack(pady=10)
        
    def load_models(self):
        """Load detection and classification models"""
        try:
            self.update_status("Loading models...")
            
            # Load YOLOv8 for detection
            self.detection_model = YOLO('yolov8n.pt')  # nano model for speed
            
            # Load ResNet50 for classification
            self.classification_model = models.resnet50(pretrained=True)
            self.classification_model.to(self.device)
            self.classification_model.eval()
            
            # Image preprocessing for classification
            self.classify_transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                   std=[0.229, 0.224, 0.225])
            ])
            
            # Load ImageNet class labels
            self.load_imagenet_labels()
            
            self.update_status("Models loaded successfully | Device: " + self.device.upper())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load models: {str(e)}")
            self.update_status("Error loading models")
    
    def load_imagenet_labels(self):
        """Load ImageNet class labels"""
        # Simplified list of common ImageNet classes
        self.class_labels = [
            "tench", "goldfish", "great white shark", "tiger shark", "hammerhead",
            "electric ray", "stingray", "cock", "hen", "ostrich", "brambling",
            "goldfinch", "house finch", "junco", "indigo bunting", "robin",
            "bulbul", "jay", "magpie", "chickadee", "water ouzel", "kite",
            "bald eagle", "vulture", "great grey owl", "European fire salamander",
            "common newt", "eft", "spotted salamander", "axolotl", "bullfrog"
        ]
        # In a real implementation, load all 1000 ImageNet classes
        
    def select_camera(self):
        """Select camera as video source"""
        self.use_camera = True
        self.video_path = 0
        self.update_status("Camera selected as source")
        
    def select_video(self):
        """Open file dialog to select video"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mov *.mkv"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.video_path = file_path
            self.use_camera = False
            self.update_status(f"Video selected: {os.path.basename(file_path)}")
            
    def update_confidence(self, value):
        """Update confidence threshold"""
        self.confidence_threshold = float(value)
        self.conf_value_label.configure(text=f"{value:.2f}")
        
    def toggle_classification(self):
        """Toggle classification on/off"""
        self.show_classification = self.classification_switch.get()
        
    def start_detection(self):
        """Start detection process"""
        if self.video_path is None:
            messagebox.showwarning("Warning", "Please select a video source first!")
            return
            
        if self.detection_model is None:
            messagebox.showerror("Error", "Models not loaded!")
            return
            
        self.is_running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        
        # Start detection in separate thread
        detection_thread = threading.Thread(target=self.run_detection, daemon=True)
        detection_thread.start()
        
    def stop_detection(self):
        """Stop detection process"""
        self.is_running = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        if self.cap:
            self.cap.release()
        self.update_status("Detection stopped")
        
    def run_detection(self):
        """Main detection loop"""
        try:
            self.cap = cv2.VideoCapture(self.video_path)
            
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Failed to open video source!")
                self.stop_detection()
                return
                
            frame_count = 0
            
            while self.is_running:
                ret, frame = self.cap.read()
                if not ret:
                    # Loop video or stop
                    if not self.use_camera:
                        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                        continue
                    else:
                        break
                
                frame_count += 1
                
                # Run detection
                results = self.detection_model(frame, conf=self.confidence_threshold)
                
                # Process detections
                annotated_frame = self.process_detections(frame, results[0])
                
                # Display frame
                self.display_frame(annotated_frame)
                
                # Update status
                if frame_count % 30 == 0:
                    self.update_status(f"Processing... Frame: {frame_count}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Detection error: {str(e)}")
        finally:
            if self.cap:
                self.cap.release()
            self.is_running = False
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")
            
    def process_detections(self, frame, results):
        """Process detection results and optionally classify"""
        annotated_frame = frame.copy()
        
        if results.boxes is not None:
            for box in results.boxes:
                # Get box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                
                # Get class name from YOLO
                label = results.names[cls]
                
                # Optional classification
                if self.show_classification and self.classification_model:
                    try:
                        # Extract ROI
                        roi = frame[y1:y2, x1:x2]
                        if roi.size > 0:
                            class_label = self.classify_roi(roi)
                            label = f"{label} ({class_label})"
                    except:
                        pass
                
                # Draw bounding box
                color = self.get_color(cls)
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                
                # Draw label background
                label_text = f"{label} {conf:.2f}"
                (w, h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(annotated_frame, (x1, y1 - 20), (x1 + w, y1), color, -1)
                
                # Draw label text
                cv2.putText(annotated_frame, label_text, (x1, y1 - 5),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return annotated_frame
    
    def classify_roi(self, roi):
        """Classify a region of interest"""
        try:
            # Convert BGR to RGB
            rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_roi)
            
            # Preprocess and classify
            input_tensor = self.classify_transform(pil_image).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                output = self.classification_model(input_tensor)
                probabilities = torch.nn.functional.softmax(output[0], dim=0)
                top_prob, top_class = torch.topk(probabilities, 1)
                
            # Return class label (simplified)
            if top_class.item() < len(self.class_labels):
                return self.class_labels[top_class.item()]
            else:
                return f"Class {top_class.item()}"
        except:
            return "Unknown"
    
    def get_color(self, cls):
        """Get color for class"""
        colors = [
            (255, 0, 0), (0, 255, 0), (0, 0, 255),
            (255, 255, 0), (255, 0, 255), (0, 255, 255),
            (128, 0, 0), (0, 128, 0), (0, 0, 128),
            (128, 128, 0), (128, 0, 128), (0, 128, 128)
        ]
        return colors[cls % len(colors)]
    
    def display_frame(self, frame):
        """Display frame in UI"""
        try:
            # Resize frame to fit display
            display_height = 720
            aspect_ratio = frame.shape[1] / frame.shape[0]
            display_width = int(display_height * aspect_ratio)
            
            frame_resized = cv2.resize(frame, (display_width, display_height))
            
            # Convert to RGB
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            
            # Convert to PhotoImage
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Update label
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk, text="")
        except Exception as e:
            print(f"Display error: {e}")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.configure(text=message)
        
    def run(self):
        """Run the application"""
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
        
    def on_closing(self):
        """Handle window closing"""
        self.stop_detection()
        self.window.destroy()


if __name__ == "__main__":
    app = ObjectDetectionApp()
    app.run()
