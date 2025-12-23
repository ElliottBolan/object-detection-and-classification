# 🎯 Object Detection and Classification System

A professional, state-of-the-art multi-object detection and classification application with a modern UI. This application combines YOLOv8 for real-time object detection with ResNet50 for image classification.

## ✨ Features

- **State-of-the-art Object Detection**: Uses YOLOv8 (You Only Look Once) for fast and accurate multi-object detection
- **Advanced Classification**: Integrates ResNet50 for detailed object classification using ImageNet pre-trained weights
- **Professional UI**: Modern, dark-themed interface built with CustomTkinter
- **Multiple Video Sources**: Support for both video files and live camera feed
- **Real-time Processing**: Process videos or camera streams in real-time with adjustable confidence thresholds
- **Interactive Controls**: 
  - Adjustable confidence threshold slider
  - Toggle classification on/off
  - Start/Stop controls
  - Video file selection
  - Camera input option
- **GPU Acceleration**: Automatically uses CUDA if available, falls back to CPU

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- (Optional) CUDA-capable GPU for faster processing

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ElliottBolan/object-detection-and-classification.git
cd object-detection-and-classification
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Running the Application

Simply run the main script:
```bash
python main.py
```

### Using the Interface

1. **Select Video Source**:
   - Click "Use Camera" to use your webcam
   - Click "Select Video File" to choose a video file (.mp4, .avi, .mov, .mkv)

2. **Adjust Settings**:
   - Use the confidence threshold slider to adjust detection sensitivity (0.1 - 0.9)
   - Toggle "Enable Classification" to turn classification on/off

3. **Start Detection**:
   - Click "▶ Start Detection" to begin processing
   - The video will display with bounding boxes around detected objects
   - Each detection shows the object class and confidence score

4. **Stop Detection**:
   - Click "⏸ Stop Detection" to pause processing

## 🎨 User Interface

The application features a modern, professional interface with:
- Left control panel with all settings and controls
- Large video display area on the right
- Status bar showing current processing state
- Dark theme for comfortable viewing

## 🔧 Technical Details

### Models Used

- **YOLOv8n**: Lightweight version of YOLOv8 for real-time detection
  - Detects 80 different object classes (COCO dataset)
  - Optimized for speed and accuracy balance

- **ResNet50**: Deep residual network for classification
  - Pre-trained on ImageNet (1000 classes)
  - Provides additional classification for detected objects

### Performance

- **GPU Mode**: 30+ FPS on modern GPUs
- **CPU Mode**: 5-15 FPS depending on CPU

## 📋 Requirements

- opencv-python >= 4.8.0
- ultralytics >= 8.0.0 (YOLOv8)
- torch >= 2.0.0
- torchvision >= 0.15.0
- Pillow >= 10.0.0
- numpy >= 1.24.0
- customtkinter >= 5.2.0

## 🛠️ Development

### Project Structure

```
object-detection-and-classification/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🐛 Troubleshooting

### Models not downloading
On first run, the application will automatically download YOLOv8 and ResNet50 weights. Ensure you have a stable internet connection.

### Camera not detected
Make sure your camera is properly connected and not being used by another application.

### Low FPS
- Reduce video resolution
- Lower the confidence threshold
- Disable classification
- Use a GPU if available

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

Elliott Bolan

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- PyTorch and torchvision
- CustomTkinter for modern UI components