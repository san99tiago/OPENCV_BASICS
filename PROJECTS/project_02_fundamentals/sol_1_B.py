# SECOND PART OF SOLUTION 1 (FINDING OPTIMAL BGR VALUES FOR TRESHOLD)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# Values where the limits for the BGR filters-trackbars will start
BH = 255
BL = 173
GH = 255
GL = 176
RH = 255
RL = 40


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


def apply_BGR_filters(img, BL, BH, GL, GH, RL, RH ):
    h, w = img.shape[:2]

    # Get the three specific "H", "S", "V" img channels (to apply filters)
    imgBGR_B = img[:, :, 0]
    imgBGR_G = img[:, :, 1]
    imgBGR_R = img[:, :, 2]

    # Apply specific lower and upper RGB filters to Blue channel
    retval, imgBGR_B_1 = cv.threshold(imgBGR_B, BL, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_B_1", imgBGR_B_1)

    retval, imgBGR_B_2 = cv.threshold(imgBGR_B, BH, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_B_2", imgBGR_B_2)

    imgBGR_B_intersection = cv.bitwise_or(imgBGR_B_1, imgBGR_B_2)
    cv.imshow("imgBGR_B_intersection", imgBGR_B_intersection)

    retval, imgBGR_G_1 = cv.threshold(imgBGR_G, GL, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_G_1", imgBGR_G_1)

    retval, imgBGR_G_2 = cv.threshold(imgBGR_G, GH, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_G_2", imgBGR_G_2)

    imgBGR_G_intersection = cv.bitwise_or(imgBGR_G_1, imgBGR_G_2)
    cv.imshow("imgBGR_G_intersection", imgBGR_G_intersection)

    retval, imgBGR_R_1 = cv.threshold(imgBGR_R, RL, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_R_1", imgBGR_R_1)

    retval, imgBGR_R_2 = cv.threshold(imgBGR_R, RH, 255, cv.THRESH_BINARY)
    # cv.imshow("imgBGR_R_2", imgBGR_R_2)

    imgBGR_R_intersection = cv.bitwise_or(imgBGR_R_1, imgBGR_R_2)
    cv.imshow("imgBGR_R_intersection", imgBGR_R_intersection)


    # Mix all channels in the new BGR img
    imgBGR_new = np.zeros((h, w, 3), np.uint8)

    imgBGR_new[:, :, 0] = imgBGR_B
    imgBGR_new[:, :, 1] = imgBGR_G
    imgBGR_new[:, :, 2] = imgBGR_R

    return imgBGR_new


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    # img_path = get_img_path(img_folder_path, "21.png")
    img_path = get_img_path(img_folder_path, "monedas.jpg")

    global BH, BL, GH, GL, RH, RL
    img = cv.imread(img_path, 1)

    h, w = img.shape[:2]  # Get the shape of the image (height, width)


    # Create main trackbars to all BGR upper and lower limits (control them)
    cv.namedWindow("TrackBar", cv.WINDOW_NORMAL)
    cv.createTrackbar("BH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("BH", "TrackBar", BH)
    cv.createTrackbar("BL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("BL", "TrackBar", BL)
    cv.createTrackbar("GH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("GH", "TrackBar", GH)
    cv.createTrackbar("GL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("GL", "TrackBar", GL)
    cv.createTrackbar("RH", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("RH", "TrackBar", RH)
    cv.createTrackbar("RL", "TrackBar", 0, 255, nothing)
    cv.setTrackbarPos("RL", "TrackBar", RL)


    cv.imshow("img", img)   

    # Main loop to keep updating image
    while (True):

        # Exit when "q" key is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break

        # Update BGR limits from the trackbars
        BH = cv.getTrackbarPos("BH", "TrackBar")
        BL = cv.getTrackbarPos("BL", "TrackBar")
        GH = cv.getTrackbarPos("GH", "TrackBar")
        GL = cv.getTrackbarPos("GL", "TrackBar")
        RH = cv.getTrackbarPos("RH", "TrackBar")
        RL = cv.getTrackbarPos("RL", "TrackBar")

        # Function to return BGR image after filters
        imgBGR_new = apply_BGR_filters(img, BL, BH, GL, GH, RL, RH)

        # Keep showing images
        cv.imshow("img_new", imgBGR_new)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)

