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



Usage
Connect a webcam to your computer.

Clone this repository:

bash
Copy code
git clone https://github.com/your-username/aruco-marker-detection.git
Navigate to the project directory:

bash
Copy code
cd aruco-marker-detection
Run the script:

bash
Copy code
python aruco_marker_detection.py
The script will open a window displaying the webcam feed. It will detect and track the movement of a specific ArUco marker. If the marker remains stationary for more than 2 seconds, it will print its position in the terminal.

Press 'q' to quit the script.

Customization
Desired Marker Type: By default, the script detects a specific ArUco marker type defined by the dictionary and marker ID. You can modify the desired_marker_id variable in the script to specify the desired marker ID.

Threshold: You can adjust the distance threshold (dist > 10) in the script to control the sensitivity of movement detection. Increase the threshold value to make it less sensitive, and decrease it to make it more sensitive.

License
This project is licensed under the MIT License.

Acknowledgements
The ArUco marker detection is implemented using the OpenCV library.
ArUco markers are a popular choice for computer vision applications and are widely used for augmented reality and marker-based tracking.

Make sure to replace "your-username" in the clone command with your actual GitHub username. Additionally, you can modify the "Acknowledgements" section and add any relevant acknowledgements or credits for the project.
