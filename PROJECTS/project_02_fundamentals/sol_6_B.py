# SECOND PART OF CHALLENGE 6 (USE FOUND VALUES TO CHANGE HOUSE COLORS)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os
import sol_6_A

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


def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "fachada1.png")

    global h, w, imgHSV, HH, HL, SH, SL, VH, VL
    img = cv.imread(img_path, 1)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    # Create main trackbars to all HSV upper and lower limits (control them)
    cv.namedWindow("CUSTOMIZE HOUSE COLOR", cv.WINDOW_NORMAL)
    cv.createTrackbar("R", "CUSTOMIZE HOUSE COLOR", 0, 255, nothing)
    cv.setTrackbarPos("R", "CUSTOMIZE HOUSE COLOR", 0)
    cv.createTrackbar("G", "CUSTOMIZE HOUSE COLOR", 0, 255, nothing)
    cv.setTrackbarPos("G", "CUSTOMIZE HOUSE COLOR", 128)
    cv.createTrackbar("B", "CUSTOMIZE HOUSE COLOR", 0, 255, nothing)
    cv.setTrackbarPos("B", "CUSTOMIZE HOUSE COLOR", 255)

    image_number = 0  # Lets us save images saved with ascending numbers

    # Main loop to keep updating image
    while (True):

        # Exit when "q" key is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break

        # If "enter" key is pressed, we save current image
        if (cv.waitKey(1) & 0xFF == 13):
            image_number = image_number + 1
            file_path = os.path.dirname(__file__)
            image_name = "output_{}.jpg".format(image_number)
            path_to_save = os.path.join(file_path, image_name)
            cv.imwrite(path_to_save, final_result)


        # Update HSV limits from the trackbars
        R = cv.getTrackbarPos("R", "CUSTOMIZE HOUSE COLOR")
        G = cv.getTrackbarPos("G", "CUSTOMIZE HOUSE COLOR")
        B = cv.getTrackbarPos("B", "CUSTOMIZE HOUSE COLOR")


        # Function to return HSV image of main part of home ("Fachada")
        home_main_binary = sol_6_A.apply_HSV_filters(img, HL, HH, SL, SH, VL, VH)

        # Create a 3 channel image of home to substract it from original img
        home_main_BGR = np.zeros((h, w, 3), np.uint8)
        home_main_BGR[:, :, 0] = home_main_binary
        home_main_BGR[:, :, 1] = home_main_binary
        home_main_BGR[:, :, 2] = home_main_binary

        # New house without color (image substraction from original)
        empty_house = cv.subtract(img, home_main_BGR)

        # Add new image with the specific home color (to add it strategically)
        home_main_painted = np.zeros((h, w, 3), np.uint8)

        # apply new channel colors ONLY to white pixels from home main binary
        for i in range(h):
            for j in range(w):
                if home_main_binary[i, j] > 0:
                    home_main_painted[i, j, 0] = B
                    home_main_painted[i, j, 1] = G
                    home_main_painted[i, j, 2] = R

        # Complete new image is the addition of home main painted and empy home
        final_result = cv.add(empty_house, home_main_painted)


        # Keep showing images
        cv.imshow("home_main_BGR", home_main_BGR)
        cv.imshow("empty_house", empty_house)
        cv.imshow("home_main_painted", home_main_painted)
        cv.imshow("final_result", final_result)

if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)
