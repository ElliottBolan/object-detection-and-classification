#!/usr/bin/env python3
"""
Quick Start Script
This script helps users get started with the application
"""

import subprocess
import sys
import os

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version is compatible (3.8+)")
        return True
    else:
        print("✗ Python 3.8 or higher is required")
        return False

def install_dependencies():
    """Install required dependencies"""
    print_header("Installing Dependencies")
    
    print("This may take several minutes...")
    print("Downloading and installing packages:\n")
    
    try:
        # Try to install dependencies
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("\n✓ All dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("\n✗ Failed to install dependencies")
        print("Please try manually: pip install -r requirements.txt")
        return False

def download_models_info():
    """Provide information about model downloads"""
    print_header("Model Download Information")
    
    print("On first run, the application will download:")
    print("  • YOLOv8n model (~6 MB)")
    print("  • ResNet50 model (~98 MB)")
    print("\nTotal download: ~104 MB")
    print("This happens automatically on first launch.")
    print("\nEnsure you have a stable internet connection.")

def run_application():
    """Attempt to run the application"""
    print_header("Launching Application")
    
    print("Starting Object Detection & Classification System...")
    print("The GUI window should open shortly.\n")
    
    try:
        subprocess.run([sys.executable, "main.py"])
    except Exception as e:
        print(f"\n✗ Failed to run application: {e}")
        return False
    
    return True

def main():
    """Main quick start function"""
    print("="*60)
    print("  🎯 Object Detection & Classification System")
    print("  Quick Start Setup")
    print("="*60)
    
    # Check Python version
    if not check_python_version():
        print("\nPlease upgrade Python to version 3.8 or higher.")
        return 1
    
    # Ask user if they want to install dependencies
    print_header("Setup Options")
    print("1. Install dependencies and run application")
    print("2. Skip installation (dependencies already installed)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        if install_dependencies():
            download_models_info()
            input("\nPress Enter to launch the application...")
            run_application()
        else:
            print("\nSetup failed. Please install dependencies manually.")
            return 1
    
    elif choice == "2":
        download_models_info()
        input("\nPress Enter to launch the application...")
        run_application()
    
    elif choice == "3":
        print("\nSetup cancelled.")
        print("To run later: python main.py")
        return 0
    
    else:
        print("\nInvalid choice. Exiting.")
        return 1
    
    print("\n" + "="*60)
    print("  Thank you for using the application!")
    print("="*60 + "\n")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user.")
        sys.exit(1)
