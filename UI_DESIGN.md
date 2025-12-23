# 🎨 UI Design Documentation

## Application Layout

The Object Detection & Classification System features a modern, professional dark-themed interface designed for ease of use and optimal workflow.

## Window Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  🎯 Object Detection & Classification System                       │
├──────────────┬──────────────────────────────────────────────────────┤
│              │                                                       │
│  Control     │                                                       │
│  Panel       │         Video Display Area                           │
│              │                                                       │
│  ┌────────┐  │    ┌──────────────────────────────────────────┐     │
│  │ Source │  │    │                                          │     │
│  └────────┘  │    │                                          │     │
│              │    │         Live Video Feed                  │     │
│  ┌────────┐  │    │      with Detection Boxes                │     │
│  │Settings│  │    │                                          │     │
│  └────────┘  │    │                                          │     │
│              │    └──────────────────────────────────────────┘     │
│  ┌────────┐  │                                                       │
│  │Controls│  │                                                       │
│  └────────┘  │                                                       │
│              │                                                       │
├──────────────┴──────────────────────────────────────────────────────┤
│  Status: Ready | Device: CUDA | Frame: 0                            │
└─────────────────────────────────────────────────────────────────────┘
```

## Control Panel Components (Left Side - 300px width)

### 1. Title Section
- **Large heading**: "🎯 Object Detection & Classification System"
- **Font**: Bold, 28pt
- **Color**: White text on dark background

### 2. Video Source Section
```
┌─────────────────────────────────┐
│   📹 Video Source               │
├─────────────────────────────────┤
│                                 │
│  ┌─────────────────────────┐   │
│  │    Use Camera           │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  Select Video File      │   │
│  └─────────────────────────┘   │
│                                 │
└─────────────────────────────────┘
```

**Components:**
- Section header with camera emoji
- "Use Camera" button (blue, 40px height)
- "Select Video File" button (blue, 40px height)
- Full width with 20px padding

### 3. Settings Section
```
┌─────────────────────────────────┐
│   ⚙️ Settings                   │
├─────────────────────────────────┤
│                                 │
│  Confidence Threshold           │
│  ├────────○──────────┤          │
│        0.5                      │
│                                 │
│  [ ✓ ] Enable Classification   │
│                                 │
└─────────────────────────────────┘
```

**Components:**
- Section header with gear emoji
- Confidence threshold label
- Slider (0.1 to 0.9, step 0.1)
- Current value display
- Toggle switch for classification

### 4. Controls Section
```
┌─────────────────────────────────┐
│   🎮 Controls                   │
├─────────────────────────────────┤
│                                 │
│  ┌─────────────────────────┐   │
│  │  ▶ Start Detection      │   │
│  │      (Green)            │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  ⏸ Stop Detection       │   │
│  │      (Red)              │   │
│  └─────────────────────────┘   │
│                                 │
└─────────────────────────────────┘
```

**Components:**
- Section header with controller emoji
- Start button (green, 50px height, bold 16pt)
- Stop button (red, 50px height, bold 16pt, initially disabled)
- Full width with 20px padding

### 5. Info Section (Bottom of Control Panel)
```
┌─────────────────────────────────┐
│        ℹ️ Info                  │
│                                 │
│     YOLOv8 Detection            │
│            +                    │
│   ImageNet Classification       │
└─────────────────────────────────┘
```

## Video Display Area (Right Side - Expandable)

### Main Video Panel
```
┌──────────────────────────────────────────────┐
│                                              │
│  ┌────────────────────────────────────────┐ │
│  │                                        │ │
│  │  ┌──────────────────┐                 │ │
│  │  │ person 0.95      │                 │ │
│  │  │                  │                 │ │
│  │  └──────────────────┘                 │ │
│  │                                        │ │
│  │         ┌────────────────┐            │ │
│  │         │ car 0.87       │            │ │
│  │         │                │            │ │
│  │         └────────────────┘            │ │
│  │                                        │ │
│  └────────────────────────────────────────┘ │
│                                              │
└──────────────────────────────────────────────┘
```

**Features:**
- Fills remaining window space
- Scales video maintaining aspect ratio
- Shows detection bounding boxes in various colors
- Labels with class name and confidence score
- Labels have colored background matching box color

### Detection Box Colors
The application uses a color palette for different object classes:
- Red (255, 0, 0)
- Green (0, 255, 0)
- Blue (0, 0, 255)
- Yellow (255, 255, 0)
- Magenta (255, 0, 255)
- Cyan (0, 255, 255)
- And 6 more variations

## Status Bar (Bottom - Full Width)

```
┌────────────────────────────────────────────────────────────┐
│  Ready | Device: CUDA | Frame: 0                           │
└────────────────────────────────────────────────────────────┘
```

**Information Displayed:**
- Current status (Ready, Processing, Error, etc.)
- Device being used (CPU or CUDA)
- Current frame number (when processing)
- Small font (12pt)
- Full width

## Color Scheme

### Primary Colors
- **Background**: Dark gray (#2B2B2B)
- **Panels**: Slightly lighter gray (#3B3B3B)
- **Text**: White (#FFFFFF)
- **Primary Accent**: Blue (#1F6AA5)

### Button Colors
- **Normal Buttons**: Blue (#1F6AA5)
- **Start Button**: Green (#2D7A2D)
- **Stop Button**: Red (#C13838)
- **Hover Effects**: Darker shades of base colors

### Text Colors
- **Headers**: White, bold
- **Body Text**: White, regular
- **Status**: White on dark background
- **Labels on Video**: White on colored background

## Typography

- **Main Title**: 28pt, Bold
- **Section Headers**: 18pt, Bold
- **Buttons**: 14-16pt, Regular/Bold
- **Body Text**: 12pt, Regular
- **Status Bar**: 12pt, Regular

## Spacing & Padding

- **Window Padding**: 10px all sides
- **Panel Padding**: 20px vertical, 20px horizontal
- **Button Spacing**: 5-10px between buttons
- **Section Spacing**: 30px between sections

## Responsive Behavior

- Control panel maintains fixed 300px width
- Video display expands to fill available space
- Minimum window size: 1400x900
- Video scales proportionally within display area

## User Experience Features

1. **Visual Feedback**
   - Buttons change color on hover
   - Disabled state for stop button when not running
   - Status updates in real-time

2. **Accessibility**
   - High contrast dark theme
   - Large, clear buttons
   - Readable font sizes
   - Emoji icons for visual guidance

3. **Professional Appearance**
   - Clean, organized layout
   - Consistent spacing and alignment
   - Modern UI components
   - Smooth visual transitions

## Detection Visualization

### Bounding Boxes
- **Line Width**: 2 pixels
- **Color**: Class-specific from color palette
- **Style**: Solid rectangle

### Labels
- **Position**: Top-left of bounding box
- **Background**: Filled rectangle matching box color
- **Text**: White, 0.6 scale
- **Content**: "class_name confidence"
  - Example: "person 0.95"
  - With classification: "person (human) 0.95"

## Window Behavior

- **Title**: "Object Detection & Classification System"
- **Size**: 1400x900 pixels
- **Resizable**: Yes
- **Close Handling**: Properly stops detection and cleans up resources
- **Theme**: Dark mode (customtkinter dark theme)

## Interactive Elements

All buttons and controls provide immediate visual feedback:
- Hover state shows darker shade
- Click state confirmed by action
- Disabled state clearly visible (grayed out)
- Status updates confirm actions

This design creates a professional, user-friendly interface that makes complex AI functionality accessible to users of all skill levels.
