# FIRST PART OF SOLUTION 1 (FINDING OPTIMAL HSV VALUES FOR TRESHOLD)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# Values where the limits for the HSV filters-trackbars will start
HH = 255
HL = 47
SH = 255
SL = 30
VH = 255
VL = 30


def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def nothing(_):
    pass


def apply_HSV_filters(img, HL, HH, SL, SH, VL, VH ):
    h, w = img.shape[:2]

    # Get the three specific "H", "S", "V" img channels (to apply filters)
    imgHSV_H = imgHSV[:, :, 0]
    imgHSV_S = imgHSV[:, :, 1]
    imgHSV_V = imgHSV[:, :, 2]

    # Apply specific desired filters to each img channels
    retval, imgHSV_H = cv.threshold(imgHSV_H, HL, HH, cv.THRESH_BINARY)
    retval, imgHSV_S = cv.threshold(imgHSV_S, SL, SH, cv.THRESH_BINARY)
    retval, imgHSV_V = cv.threshold(imgHSV_V, VL, VH, cv.THRESH_BINARY)
    
    # Mix all channels in the new HSV img
    imgHSV_new = np.zeros((h, w, 3), np.uint8)

    # More efficient with "splitting-channels"
    imgHSV_new[:, :, 0] = imgHSV_H
    imgHSV_new[:, :, 1] = imgHSV_S
    imgHSV_new[:, :, 2] = imgHSV_V

    return imgHSV_new


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "monedas.jpg")

    global h, w, imgHSV, HH, HL, SH, SL, VH, VL
    img = cv.imread(img_path, 1)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)


    h, w = img.shape[:2]  # Get the shape of the image (height, width)


    # Create main trackbars to all HSV upper and lower limits (control them)
    cv.namedWindow("TrackBar", cv.WINDOW_NORMAL)
    cv.createTrackbar("HH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("HH", "TrackBar", HH)
    cv.createTrackbar("HL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("HL", "TrackBar", HL)
    cv.createTrackbar("SH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("SH", "TrackBar", SH)
    cv.createTrackbar("SL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("SL", "TrackBar", SL)
    cv.createTrackbar("VH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("VH", "TrackBar", VH)
    cv.createTrackbar("VL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("VL", "TrackBar", VL)


    cv.imshow("img", img)   

    # Main loop to keep updating image
    while (True):

        # Exit when "q" key is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break
        
        # Update HSV limits from the trackbars
        HH = cv.getTrackbarPos("HH", "TrackBar")
        HL = cv.getTrackbarPos("HL", "TrackBar")
        SH = cv.getTrackbarPos("SH", "TrackBar")
        SL = cv.getTrackbarPos("SL", "TrackBar")
        VH = cv.getTrackbarPos("VH", "TrackBar")
        VL = cv.getTrackbarPos("VL", "TrackBar")

        # Function to return HSV image after filters (before binarizing it)
        imgHSV_new = apply_HSV_filters(img, HL, HH, SL, SH, VL, VH)

        # Keep showing images
        cv.imshow("img_new", imgHSV_new)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)
