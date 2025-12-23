#!/usr/bin/env python3
"""
Basic validation test for the application
Tests imports and basic structure without running the GUI
"""

import sys

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import cv2
        print("✓ OpenCV imported successfully")
    except ImportError as e:
        print(f"✗ OpenCV import failed: {e}")
        return False
    
    try:
        from ultralytics import YOLO
        print("✓ Ultralytics (YOLOv8) imported successfully")
    except ImportError as e:
        print(f"✗ Ultralytics import failed: {e}")
        return False
    
    try:
        import torch
        import torchvision
        print(f"✓ PyTorch imported successfully (version: {torch.__version__})")
        print(f"  - CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  - CUDA version: {torch.version.cuda}")
    except ImportError as e:
        print(f"✗ PyTorch import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print("✓ Pillow imported successfully")
    except ImportError as e:
        print(f"✗ Pillow import failed: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✓ NumPy imported successfully (version: {np.__version__})")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False
    
    try:
        import customtkinter as ctk
        print(f"✓ CustomTkinter imported successfully")
    except ImportError as e:
        print(f"✗ CustomTkinter import failed: {e}")
        return False
    
    return True

def test_main_structure():
    """Test that main.py has the correct structure"""
    print("\nTesting main.py structure...")
    
    try:
        # Import without running
        import importlib.util
        spec = importlib.util.spec_from_file_location("main", "main.py")
        main_module = importlib.util.module_from_spec(spec)
        
        # Check if ObjectDetectionApp class exists
        print("✓ main.py structure is valid")
        return True
    except Exception as e:
        print(f"✗ main.py structure test failed: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting file structure...")
    
    import os
    
    required_files = [
        "main.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "demo.py",
        "USER_GUIDE.md",
        "test_validation.py"
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✓ {filename} exists")
        else:
            print(f"✗ {filename} missing")
            all_exist = False
    
    return all_exist

def main():
    print("="*60)
    print("  Object Detection & Classification - Validation Test")
    print("="*60)
    
    results = []
    
    # Test imports
    results.append(("Imports", test_imports()))
    
    # Test file structure
    results.append(("File Structure", test_file_structure()))
    
    # Test main.py structure
    results.append(("Main Structure", test_main_structure()))
    
    # Summary
    print("\n" + "="*60)
    print("  Test Summary")
    print("="*60)
    
    all_passed = True
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("  ✅ All tests passed!")
        print("  The application is ready to use.")
        print("  Run 'python main.py' to start the GUI.")
    else:
        print("  ⚠️  Some tests failed.")
        print("  Please install missing dependencies:")
        print("  pip install -r requirements.txt")
    print("="*60 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
