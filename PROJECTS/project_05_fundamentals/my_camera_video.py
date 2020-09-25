# WORKING WITH VIDEOS
# Santiago Garcia Arango, 2020

import numpy as np
import cv2 as cv
import os

def main():
    # Get the video from MY CAMERA
    video_path = 0

    capture_img = cv.VideoCapture(video_path)

    while (capture_img.isOpened() == True):

        # Get current image frame from video
        ret, img_color = capture_img.read()

        # Change image to gray (to be able to binarize it)
        img_1 = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

        # Binarize the image
        _, img_1_bin = cv.threshold(img_1, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

        # Show current image frame
        cv.imshow("current_frame", img_1_bin)

        # Be able to stop video at any time
        if cv.waitKey(1) & 0xFF == ord('q'):
            break





if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
