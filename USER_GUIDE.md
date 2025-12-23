# 📖 User Guide - Object Detection & Classification System

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Using the Application](#using-the-application)
4. [Features & Settings](#features--settings)
5. [Tips & Best Practices](#tips--best-practices)
6. [Troubleshooting](#troubleshooting)

## Getting Started

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ElliottBolan/object-detection-and-classification.git
   cd object-detection-and-classification
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

### First Time Launch

On the first run, the application will:
- Download YOLOv8 model weights (~6MB)
- Download ResNet50 model weights (~98MB)
- This may take a few minutes depending on your internet connection

## Interface Overview

The application window consists of three main areas:

### 1. Control Panel (Left Side)
- **Video Source Section**: Choose between camera or video file
- **Settings Section**: Adjust detection parameters
- **Controls Section**: Start/Stop buttons
- **Info Section**: Model information

### 2. Video Display (Right Side)
- Large preview area showing the processed video
- Real-time detection results with bounding boxes
- Object labels and confidence scores

### 3. Status Bar (Bottom)
- Current processing status
- Device information (CPU/CUDA)
- Frame count and performance metrics

## Using the Application

### Step-by-Step Workflow

#### 1. Select Video Source

**Option A: Use Camera**
- Click the "Use Camera" button
- Your default webcam will be selected
- Status bar will confirm: "Camera selected as source"

**Option B: Select Video File**
- Click "Select Video File"
- Browse and select a video file
- Supported formats: .mp4, .avi, .mov, .mkv
- Status bar will show the selected filename

#### 2. Adjust Settings (Optional)

**Confidence Threshold**
- Use the slider to set detection sensitivity
- Range: 0.1 (low) to 0.9 (high)
- Lower values: More detections, possible false positives
- Higher values: Fewer but more confident detections
- Default: 0.5 (recommended)

**Enable Classification**
- Toggle switch to enable/disable classification
- ON: Shows both detection and classification labels
- OFF: Shows only detection labels (faster processing)

#### 3. Start Detection

- Click "▶ Start Detection" button
- Processing begins immediately
- Video display shows:
  - Bounding boxes around detected objects
  - Class labels (e.g., "person", "car", "dog")
  - Confidence scores (e.g., "0.85")
  - Optional classification results

#### 4. Stop Detection

- Click "⏸ Stop Detection" button
- Processing stops
- Ready for new video source

## Features & Settings

### Detection Confidence Threshold

**What it does:**
- Filters detections based on confidence level
- Higher threshold = more certain detections

**When to adjust:**
- **Increase (0.6-0.9)**: Crowded scenes, reduce false positives
- **Decrease (0.2-0.4)**: Difficult lighting, small objects
- **Default (0.5)**: Balanced performance

### Classification Toggle

**When ON:**
- Provides detailed object classification
- Uses ResNet50 for 1000 ImageNet classes
- Slightly slower processing
- Example: "person (human)" or "dog (golden retriever)"

**When OFF:**
- Uses only YOLO detection classes
- Faster processing
- 80 COCO dataset classes
- Example: "person" or "dog"

## Tips & Best Practices

### For Best Performance

1. **GPU Acceleration**
   - Install CUDA-compatible PyTorch for GPU support
   - Check status bar for "Device: CUDA" confirmation
   - GPU provides 3-10x faster processing

2. **Video Resolution**
   - 720p (1280x720): Best balance of speed and quality
   - 1080p (1920x1080): Higher quality, slower processing
   - 480p (640x480): Fastest processing

3. **Confidence Threshold**
   - Start with default 0.5
   - Adjust based on your specific use case
   - Monitor false positives/negatives

4. **Classification**
   - Disable for real-time performance
   - Enable for detailed analysis
   - Useful for specific object identification

### Optimal Settings by Use Case

**Real-time Camera Monitoring:**
- Source: Camera
- Confidence: 0.5-0.6
- Classification: OFF
- Expected FPS: 20-30 (GPU), 8-15 (CPU)

**Video Analysis:**
- Source: Video File
- Confidence: 0.4-0.5
- Classification: ON
- Process offline for best results

**Security/Surveillance:**
- Source: Camera
- Confidence: 0.6-0.7
- Classification: OFF
- Higher threshold reduces false alarms

**Object Identification:**
- Source: Video File
- Confidence: 0.5
- Classification: ON
- Focus on accuracy over speed

## Troubleshooting

### Common Issues

**Issue: "Failed to load models"**
- **Cause**: Internet connection or disk space
- **Solution**: 
  - Check internet connection
  - Ensure 500MB free disk space
  - Restart application

**Issue: "Failed to open video source"**
- **Cause**: Invalid video file or camera in use
- **Solution**:
  - Verify video file is not corrupted
  - Close other applications using the camera
  - Try a different video format

**Issue: Low FPS / Slow Processing**
- **Cause**: CPU processing or high resolution
- **Solution**:
  - Install CUDA-compatible PyTorch for GPU
  - Disable classification
  - Reduce video resolution
  - Increase confidence threshold

**Issue: Camera not detected**
- **Cause**: Camera not available or permissions
- **Solution**:
  - Check camera connection
  - Grant camera permissions
  - Try different camera index (modify code)
  - Close other camera applications

**Issue: Too many false detections**
- **Cause**: Low confidence threshold
- **Solution**:
  - Increase confidence threshold (0.6-0.8)
  - Adjust based on scene complexity

**Issue: Missing detections**
- **Cause**: High confidence threshold
- **Solution**:
  - Decrease confidence threshold (0.3-0.4)
  - Ensure good lighting conditions
  - Check object size in frame

### Performance Tips

1. **For Faster Processing:**
   - Use GPU (CUDA)
   - Disable classification
   - Lower video resolution
   - Increase confidence threshold

2. **For Better Accuracy:**
   - Use appropriate confidence threshold
   - Ensure good lighting
   - Position objects clearly in frame
   - Use higher resolution video

3. **For Balanced Performance:**
   - Confidence: 0.5
   - Classification: Based on need
   - Resolution: 720p
   - GPU if available

## Keyboard Shortcuts

Currently, the application uses button controls. Keyboard shortcuts can be added in future versions.

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check the README.md for additional information
- Review the demo.py for feature overview

## Version Information

- **YOLOv8**: Latest from Ultralytics
- **ResNet50**: PyTorch pre-trained
- **UI Framework**: CustomTkinter
- **Python**: 3.8+

---

**Enjoy using the Object Detection & Classification System! 🎯**
