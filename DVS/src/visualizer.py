# main.py — the only file you ever run. It opens the video, loops through frames, and calls the other modules in the right order.
# src/simulator.py — takes a grayscale frame in, returns a list of (x, y, timestamp, polarity) events out. This is the DVS brain.
# src/visualizer.py — takes that event list, paints red/blue dots on a canvas, applies decay each frame. This is what you see on screen.
# src/motion_detector.py — takes the event list, bins events into a grid, finds clusters of activity, returns bounding boxes around moving regions.
# src/__init__.py — empty file that tells Python "this folder is a module you can import from."
# inputs/ — drop your test video here.
# outputs/ — recorded demo videos get saved here.
# requirements.txt — three lines: numpy, opencv-python, scipy.
# README.md — what the project is, how to run it, what the output looks like.

import numpy as np
import config

class Visualizer:
    def __init__(self, height, width):
        self.canvas = np.zeros((height, width, 3), dtype=np.float32)
    
    def update(self, events):
        self.canvas *= config.DECAY

        for x, y, t, polarity in events:
            if polarity == 1:
                self.canvas[y,x] = config.ON_COLOR
            else:
                self.canvas[y,x] = config.OFF_COLOR
        return self.canvas.astype(np.uint8)