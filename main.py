#!/usr/bin/env python3
"""
Enhanced Music21 Visual DAW - Scale Interval Display with Horizontal Scroll
"""

from kivy.app import App
from kivy.uix.label import Label

class SriMusicApp(App):
    def build(self):
        return Label(text="🎵 Sri Music App\nWelcome to your Kivy GUI!")

if __name__ == '__main__':
    SriMusicApp().run()
