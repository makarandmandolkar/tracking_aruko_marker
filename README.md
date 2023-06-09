# ArUco Marker Detection

This Python script detects the presence and movement of a specific ArUco marker using OpenCV.

## Requirements

- Python 3.x
- OpenCV
- Numpy

## Installation

1. Install Python 3.x from the [official Python website](https://www.python.org/downloads/).

2. Install the required packages using pip:
   ```bash
   pip install opencv-python numpy

## Usage
1. Connect a webcam to your computer.

2. Clone this repository:
   ```bash
   git clone https://github.com/makarandmandolkar/tracking_aruko_marker.git

3. Navigate to the project directory:
   ```bash
   cd tracking_aruko_marker

4. Run the script:
   ```bash
   python aruco_movement_detector.py

The script will open a window displaying the webcam feed. It will detect and track the movement of a specific ArUco marker. If the marker remains stationary for more than 2 seconds, it will print its position in the terminal.

5. Press 'q' to quit the script.

## Customization
Desired Marker Type: By default, the script detects a specific ArUco marker type defined by the dictionary and marker ID. You can modify the desired_marker_id variable in the script to specify the desired marker ID.

Threshold: You can adjust the distance threshold (dist > 10) in the script to control the sensitivity of movement detection. Increase the threshold value to make it less sensitive, and decrease it to make it more sensitive.

## License
This project is licensed under the MIT License.

## Acknowledgements
The ArUco marker detection is implemented using the OpenCV library.
ArUco markers are a popular choice for computer vision applications and are widely used for augmented reality and marker-based tracking.


