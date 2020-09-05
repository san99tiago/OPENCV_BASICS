# CHALLENGE (FIND MISSING PILL AND ITS COORDINATE)
# Santiago Garcia Arango, 2020

import numpy as np
import cv2 as cv
import os
import time
import hsv_trackbars as ht

# Values found to apply optimal HSV binary filter
HH = 205
HL = 0
SH = 183
SL = 85
VH = 208
VL = 96



def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def show_img(window_name, img):
    cv.imshow(window_name, img)
    return 0


def close_all():
    cv.waitKey(0)
    cv.destroyAllWindows()


def find_coordinates(img):
    h, v = img.shape[:2]

    for i in range(h-10):
        pass


def main():
    # Get the paths for the images
    img_path_1 = get_img_path(get_imgs_folder_path(), "21.jpg")
    img_path_2 = get_img_path(get_imgs_folder_path(), "22.jpg")

    # Read, convert to HSV and apply custon HSV function to binarize it good
    img_1 = cv.imread(img_path_1, 1)
    img_1_HSV = cv.cvtColor(img_1, cv.COLOR_BGR2HSV)
    img_1_bin = ht.apply_HSV_filters(img_1_HSV, HL, HH, SL, SH, VL, VH)
    
    # Read, convert to HSV and apply custon HSV function to binarize it good
    img_2 = cv.imread(img_path_2, 1)
    img_2_HSV = cv.cvtColor(img_2, cv.COLOR_BGR2HSV)
    img_2_bin = ht.apply_HSV_filters(img_2_HSV, HL, HH, SL, SH, VL, VH)

    # Apply built-in opencv function to substract img_1 and img_2
    new_img_result = cv.subtract(img_1_bin, img_2_bin)

    # Apply simple blur to reduce noise
    new_img_result = cv.blur(new_img_result,(5,5))


    # Show process and img result
    show_img("img_1", img_1)
    show_img("img_2", img_2)
    show_img("img_1_bin", img_1_bin)
    show_img("img_2_bin", img_2_bin)
    show_img("new_img_result", new_img_result)


    close_all()


if __name__ == "__main__":
    main()
