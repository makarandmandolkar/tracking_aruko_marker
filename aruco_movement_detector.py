import cv2
import time
import numpy as np

# ArUco marker parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
aruco_params = cv2.aruco.DetectorParameters()

# Specify the desired ArUco marker ID and type
desired_marker_id = 42

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use cv2.CAP_DSHOW for Windows, remove it for other OS

# Initialize marker position variables
prev_marker_pos = None
prev_marker_time = time.time()

# Main loop
while True:
    # Read frame from the video capture
    ret, frame = cap.read()

    # Detect markers in the frame
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    if ids is not None:
        # Check if the desired marker ID is present in the detected markers
        if desired_marker_id in ids:
            marker_index = np.where(ids == desired_marker_id)[0][0]

            # Get the centroid of the desired marker
            marker_pos = corners[marker_index][0].mean(axis=0).astype(int)

            if prev_marker_pos is not None:
                # Calculate the Euclidean distance between current and previous marker positions
                dist = cv2.norm(marker_pos, prev_marker_pos)

                if dist > 10:  # Adjust this threshold according to your needs
                    prev_marker_pos = marker_pos
                    prev_marker_time = time.time()
                else:
                    # Check if marker has been stationary for more than 2 seconds
                    if time.time() - prev_marker_time > 2:
                        # Publish the ArUco marker position
                        print('ArUco marker NOT MOVING position:', marker_pos)

                        prev_marker_time = time.time()
            else:
                prev_marker_pos = marker_pos
                # Publish the ArUco marker position
                print('ArUco marker position:', marker_pos)

            # Draw a rectangle around the marker and mark its position
            cv2.aruco.drawDetectedMarkers(frame, corners)
            cv2.circle(frame, tuple(marker_pos), 5, (0, 255, 0), -1)
        else:
            # The desired marker ID is not detected
            prev_marker_pos = None

            # Display a message
            cv2.putText(frame, 'Desired marker ID not detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        # No ArUco marker detected
        prev_marker_pos = None

        # Display a message
        cv2.putText(frame, 'No ArUco marker detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy any open windows
cap.release()
cv2.destroyAllWindows()
