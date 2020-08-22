# PROJECT TO APPLY A FILTER TRESHOLD TO HVS AND RETURN IT IN RGB FORMAT
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


def apply_HSV_treshold(imgHSV):
    # Apply treshold to an "HSV" img and return its "RGB" format
    imgHSV_treshold = imgHSV.copy()

    U = 120
    for i in range(0, h):
        for j in range(0, w):
            if (imgHSV[i, j, 0] < U):
                imgHSV_treshold[i, j, 0] = 200

    imgHSV_treshold = cv.cvtColor(imgHSV_treshold, cv.COLOR_HSV2BGR)
    return imgHSV_treshold


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "fachada1.png")

    global h, w
    img = cv.imread(img_path, 1)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    # Apply a filter treshold to specific "H" channel
    imgHSV_treshold = apply_HSV_treshold(imgHSV)

    cv.imshow("img", img)
    cv.imshow("imgHSV", imgHSV)
    cv.imshow("imgHSV_treshold", imgHSV_treshold)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()  # (always at the end)
