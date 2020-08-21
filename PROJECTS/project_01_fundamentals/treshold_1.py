# PROJECT TO WORK WITH IMAGE TRESHOLDS AND PROCESS IT
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os


def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def apply_blue_channel_filter(imgGrayB):
    umbral = 128  # Treshold for the binary filter

    # Apply the treshold based and overwrite results in same img
    for i in range(0, h):
        for j in range(0, w):
            if (imgGrayB[i, j] < umbral):
                imgGrayB[i, j] = 255
            else:
                imgGrayB[i, j] = 0

    return imgGrayB


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "21.png")

    global h, w
    # Loading our image with its path and parameter to change format
    imgColor = cv.imread(img_path, 1)

    h, w = imgColor.shape[:2]  # Get the shape of the image (height, width)

    # Get specific blue channel of image
    imgGrayB = imgColor[:, :, 0]  # Gray version of blue channel

    # Show image blue-channel (in gray) before processing
    cv.imshow("imgGrayB BEFORE", imgGrayB)

    imgGrayB = apply_blue_channel_filter(imgGrayB)

    cv.imshow("imgGrayB AFTER 1", imgGrayB)
    cv.imshow("imgGrayB AFTER 2 (inverted)", (255 - imgGrayB))  # Invert image


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)
