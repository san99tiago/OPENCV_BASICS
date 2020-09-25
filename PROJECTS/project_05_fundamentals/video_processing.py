# WORKING WITH VIDEOS
# Santiago Garcia Arango, 2020

import numpy as np
import cv2 as cv
import os

def main():
    # Get the video (must be in same directory to work)
    video_path = "video.mp4"

    capture_img = cv.VideoCapture(video_path)

    while (capture_img.isOpened() == True):

        # Get current image frame from video
        ret, img_color = capture_img.read()

        # Change image to gray (to be able to binarize it)
        img_1 = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

        # Binarize the image
        _, img_1_bin = cv.threshold(img_1, 50, 255, cv.THRESH_BINARY_INV)

        # Show current image frame
        cv.imshow("current_frame", img_1_bin)

        # Be able to stop video at any time
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        # # Get countours and hierarchy
        # cnt, hie = cv.findContours(img_1_bin, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        # print("HIERARCHY: \n", hie)

        # # Get img size and create a black image
        # h, w = img_1.shape[:2]
        # imgCnt = np.zeros((h, w, 3), np.uint8)


        # for cont in cnt:
        #     color = list(np.random.random(size=3)*256)

        #     cv.drawContours(imgCnt, cont, -1, color, 1)



if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
