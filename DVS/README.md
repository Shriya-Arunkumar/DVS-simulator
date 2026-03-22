# Event Camera Simulator

A Python-based software simulator of a Dynamic Vision Sensor (DVS) — a neuromorphic camera that mimics the human retina by detecting per-pixel brightness changes instead of capturing full frames.

## What is this
A DVS (Dynamic Vision Sensor) is a physical camera made from silicon which replicates the behaviour of the human retina. Instead of capturing frames like a conventional camera, it detects per-pixel brightness changes asynchronously. This project simulates that process in pure Python — it takes a webcam feed or video file as input and produces the event stream a real DVS would generate.

## How it works
1. Each frame is converted to grayscale and log-luminance is computed
2. The difference in log-luminance between consecutive frames is calculated per pixel
3. If the change exceeds a threshold, an event is fired:
   - ON event (+1) → brightness increased → shown in red
   - OFF event (-1) → brightness decreased → shown in blue
4. Events are clustered spatially to detect moving regions, drawn as green bounding boxes

## File structure
```
event-camera-sim/
│
├── src/
│   ├── simulator.py       # Core DVS log-intensity model
│   ├── visualizer.py      # Polarity-coded event rendering
│   └── motion_detector.py # Event clustering and bounding boxes
├── main.py                # Entry point
├── config.py              # All tunable parameters
└── requirements.txt       # Dependencies
```

## How to run it
```bash
# webcam
python main.py --input 0

# video file
python main.py --input inputs/test_video.mp4
```

## Requirements
- Python 3.x
- NumPy
- OpenCV
- SciPy
```bash
pip install numpy opencv-python scipy
```

## Output
Red dots = ON events (brightness increased)
Blue dots = OFF events (brightness decreased)
Green boxes = detected motion regions