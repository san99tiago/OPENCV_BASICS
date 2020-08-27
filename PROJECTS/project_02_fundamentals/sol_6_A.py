# FIRST PART OF CHALLENGE SIX (FIND IMAGE HSV TRESHOLDS FOR MAIN HOME AREA)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# Values where the limits for the HSV filters-trackbars will start
HH = 166
HL = 61
SH = 245
SL = 93
VH = 195
VL = 41


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

    # Get specific limits for HSV filter
    HSV_H = np.array([HH, SH, VH], np.uint8)
    HSV_L = np.array([HL, SL, VL], np.uint8)

    # Apply specific desired filters to each img channels
    imgHSV_new = cv.inRange(img, HSV_L, HSV_H)

    retval, imgHSV_new = cv.threshold(imgHSV_new, 200, 255, cv.THRESH_BINARY)

    return imgHSV_new


def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "fachada1.png")

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

        # Function to return HSV image of main part of home ("Fachada")
        home_main_binary = apply_HSV_filters(img, HL, HH, SL, SH, VL, VH)

        # Create a 3 channel image of home to substract it from original img
        home_main_BGR = np.zeros((h, w, 3), np.uint8)
        home_main_BGR[:, :, 0] = home_main_binary
        home_main_BGR[:, :, 1] = home_main_binary
        home_main_BGR[:, :, 2] = home_main_binary

        # Keep showing images
        cv.imshow("home_main_BGR", home_main_BGR)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)

