# 🚀 How to Run the Application

## Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- opencv-python (video processing)
- ultralytics (YOLOv8)
- torch & torchvision (deep learning)
- customtkinter (modern UI)
- Pillow & numpy (image handling)

**Note**: First-time installation may take 5-10 minutes depending on your internet connection.

### 2. Launch the Application
```bash
python main.py
```

### 3. Use the Interface

#### On First Launch:
The application will automatically download AI models (~100MB total):
- YOLOv8n model (~6 MB)
- ResNet50 model (~98 MB)

This only happens once. Subsequent launches are instant.

---

## What Happens When You Run It

### Window Opens
You'll see a professional dark-themed window (1400x900 pixels) with:
- **Left Panel**: Control panel with buttons and settings
- **Right Panel**: Large video display area
- **Bottom**: Status bar showing system information

### Initial State
- Status bar shows: "Ready | Device: CUDA" (or "CPU")
- Video display shows: "No video loaded"
- All buttons are ready to use

---

## Using the Application

### Option 1: Use Your Webcam

1. **Click "Use Camera"**
   - Status updates to "Camera selected as source"
   
2. **Click "▶ Start Detection"**
   - Your webcam feed appears
   - Objects are detected in real-time
   - Bounding boxes appear around detected objects
   - Labels show object name and confidence (e.g., "person 0.95")

3. **Adjust Settings** (while running):
   - Move the confidence slider to filter detections
   - Toggle classification on/off

4. **Click "⏸ Stop Detection"** when done

### Option 2: Use a Video File

1. **Click "Select Video File"**
   - File dialog opens
   - Navigate to your video file
   - Supported formats: .mp4, .avi, .mov, .mkv
   - Select the file
   
2. **Status updates** to show selected file name

3. **Click "▶ Start Detection"**
   - Video plays with detection overlays
   - Objects are detected frame-by-frame
   - Video loops automatically when it ends

4. **Click "⏸ Stop Detection"** to pause

---

## What You'll See

### Detection in Action

When objects are detected, you'll see:

**Bounding Boxes**: Colored rectangles around each detected object
```
┌─────────────┐
│ person 0.95 │
│             │
└─────────────┘
```

**Labels**: White text on colored background showing:
- Object class (e.g., "person", "car", "dog")
- Confidence score (e.g., "0.95" = 95% confident)

### With Classification Enabled

When classification is ON, labels show more detail:
```
┌──────────────────────┐
│ person (human) 0.95  │
│                      │
└──────────────────────┘
```

### Detectable Objects (80 classes)

**People & Animals**:
- person, dog, cat, horse, bird, cow, sheep, etc.

**Vehicles**:
- car, truck, bus, motorcycle, bicycle, airplane, boat, etc.

**Indoor Objects**:
- chair, couch, table, TV, laptop, keyboard, mouse, etc.

**Sports & Recreation**:
- sports ball, tennis racket, baseball bat, skateboard, etc.

**And 60+ more classes!**

---

## Performance Expectations

### With GPU (NVIDIA CUDA)
- **FPS**: 20-30+ frames per second
- **Latency**: Near real-time detection
- **Smooth**: Very smooth video playback

### With CPU Only
- **FPS**: 5-15 frames per second
- **Latency**: Slight delay (~100-200ms)
- **Usable**: Good for non-real-time analysis

### Improving Performance
- Disable classification (faster processing)
- Increase confidence threshold (fewer detections to process)
- Use lower resolution video
- Ensure CUDA is installed for GPU support

---

## Troubleshooting

### "Failed to load models"
**Solution**: 
- Check internet connection
- Ensure 500MB free disk space
- Wait for download to complete
- Restart application

### "Failed to open video source"
**Solution**:
- **For camera**: Close other apps using the camera
- **For video**: Ensure file isn't corrupted
- Try a different video format

### Low FPS / Slow Performance
**Solution**:
- Disable classification toggle
- Increase confidence threshold
- Install CUDA for GPU support
- Use smaller video resolution

### No Detections Appearing
**Solution**:
- Lower confidence threshold (try 0.3-0.4)
- Ensure good lighting
- Check that objects are visible in frame
- Verify objects are in the 80 COCO classes

---

## Tips for Best Results

### Camera Setup
- Good lighting is important
- Position camera to see full objects
- Avoid extreme angles
- Keep objects in focus

### Video Files
- 720p (1280x720) is optimal balance
- Higher resolution = slower processing
- Ensure video codec is supported
- Keep video files under 1GB for smooth playback

### Settings
- **Confidence 0.3-0.4**: Detect more objects (some false positives)
- **Confidence 0.5**: Balanced (recommended)
- **Confidence 0.6-0.8**: Only very confident detections
- **Classification ON**: More detailed labels, slower
- **Classification OFF**: Faster processing, simpler labels

---

## Example Session

1. Launch: `python main.py`
2. Wait 2-3 seconds for window to appear
3. Click "Use Camera"
4. Adjust confidence slider to 0.5
5. Toggle classification ON
6. Click "▶ Start Detection"
7. See yourself detected as "person" with confidence score
8. Move around and see detection follow you
9. Show different objects to the camera
10. Click "⏸ Stop Detection" when done
11. Close window to exit

---

## System Information

Check the status bar at the bottom for:
- Current processing state
- Device being used (CPU/CUDA)
- Frame count (when processing)
- Error messages (if any)

---

## Exiting the Application

Simply close the window or:
- Click "⏸ Stop Detection" first (recommended)
- Then close the window
- Application will clean up resources automatically

---

## Next Steps

After running successfully:
- Try different video files
- Experiment with confidence threshold
- Test with various objects
- Compare GPU vs CPU performance
- Read USER_GUIDE.md for advanced features

---

**Enjoy detecting and classifying objects! 🎯**

If you encounter any issues, check USER_GUIDE.md for detailed troubleshooting.
