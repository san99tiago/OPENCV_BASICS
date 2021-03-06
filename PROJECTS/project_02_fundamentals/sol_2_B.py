# FIRST PART OF SECOND CHALLENGE (FIND AVERAGE COIN SIZE)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os
import math

import sol_1_B

# Values found on <sol_1_B.py> to apply an optimal BGR_filter
BH = 255
BL = 173
GH = 255
GL = 176
RH = 255
RL = 40

# Values of average coin sizes (found on <sol_2_A.py>)
COIN_HEIGHT = 59
COIN_WIDTH = 58
COIN_RADIO = (COIN_HEIGHT + COIN_WIDTH) / 4


def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def calculate_coins(img_new):
    # Expected area of a single coin (from the average coin radio)
    one_coin_area = math.pi * (math.pow(COIN_RADIO, 2))
    total_coins_area = 0
    for i in range(h):
        for j in range(w):
            if img_new[i, j] == 255:
                total_coins_area = total_coins_area + 1

    print("\nONE COIN AREA: ", one_coin_area)
    print("TOTAL COINS AREA: ", total_coins_area)
    print("TOTAL_COINS_AREA/ONE_COIN_AREA : ", total_coins_area/one_coin_area)
    print("\nEXPECTED COINS : ", round(total_coins_area/one_coin_area))


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "monedas.jpg")
    # img_path = get_img_path(img_folder_path, "monedas2.jpg")

    global img, h, w, BH, BL, GH, GL, RH, RL

    img = cv.imread(img_path, 1)
    cv.imshow("img", img)
    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    # Use filter values found on previous challenge
    img_new = sol_1_B.apply_BGR_filters(img, BL, BH, GL, GH, RL, RH)
    cv.imshow("img_new_before_binarized", img_new)

    # Apply filters to obtain binary image result
    img_new = 255 - cv.cvtColor(img_new, cv.COLOR_BGR2GRAY)
    retval, img_new = cv.threshold(img_new, 0, 255, cv.THRESH_BINARY)
    cv.imshow("img_new_after_binarized", img_new)

    # Apply function to obtain the spected amount of coins in image
    coins = calculate_coins(img_new)



if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)
