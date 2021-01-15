# VIDEO APPROACH TO YOLO (YOU ONLY LOOK ONCE) OBJECT DETECTION
# Santiago Garcia Arango
# MLH2021

# My own imports
import main

# General imports
import cv2 as cv
import time


VIDEO_CAPTURE = cv.VideoCapture(0)

while True:
    # Get specific read image from each instant from video capture
    _, image = VIDEO_CAPTURE.read()

    # Apply face_detect algorithm to each image capture
    main.ObjectDetector(image, False)

    # Apply delay to obtain desired frequency
    time.sleep(0.05)

    # Exit when "q" is pressed
    if (cv.waitKey(1) & 0xFF == ord("q")):
        cv.destroyAllWindows()
        break
