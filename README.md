# Gesture Volume Control using Computer Vision

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-v4.5.1-red.svg)
![Mediapipe](https://img.shields.io/badge/mediapipe-v0.8.6.2-orange.svg)

This project enables gesture-based volume control using computer vision techniques. It utilizes OpenCV and Mediapipe libraries to track hand gestures and adjust system audio volume accordingly.

## Overview

Gesture recognition in real-time video streams allows users to control audio volume by moving their hands. This project uses hand tracking and pose estimation to interpret gestures and adjust volume levels dynamically.
![Image Description](img.jpg)

## Files

- `VolumHandControl.py`: Main script for gesture-based volume control.
- `handTrackModule.py`: Module providing functions for hand tracking using OpenCV.
- `handTrackerMin.py`: Minimal version of hand tracking module (possibly outdated).
- `myNewGame.py`: Placeholder for potential game integration or future development.
- `requirements.txt`: List of Python dependencies required to run the project.

## Usage

1. Ensure your webcam is connected and accessible.

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
Run the VolumHandControl.py script:

  ```
  python VolumHandControl.py
  ```
Adjust system audio volume by performing gestures recognized by the program.

## Features

Hand detection and tracking using OpenCV.
Gesture recognition for volume control.
Real-time FPS (Frames Per Second) display.

## Dependencies
Python 3.6+
OpenCV 4.5.1
Mediapipe 0.8.6.2

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any new features or fixes.
