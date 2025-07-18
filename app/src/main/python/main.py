#!/usr/bin/env python3
"""
Simple Android app using Chaquopy
This demonstrates a basic Python app that can be built into an APK
"""

import sys
import os
from datetime import datetime

def main():
    """Main function for the Android app"""
    print("🎵 Sri Music App Started!")
    print(f"📱 Python version: {sys.version}")
    print(f"⏰ Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📂 Current directory: {os.getcwd()}")
    
    # Simple app logic
    app_info = {
        "name": "Sri Music",
        "version": "1.0.0",
        "description": "A simple music player app",
        "platform": "Android via Chaquopy"
    }
    
    print("\n📋 App Information:")
    for key, value in app_info.items():
        print(f"   {key.title()}: {value}")
    
    print("\n✅ App initialized successfully!")
    print("🚀 Ready to add music functionality...")
    
    return "App started successfully"

if __name__ == '__main__':
    result = main()
    print(f"\n🎯 Result: {result}")