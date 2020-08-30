# HISTOGRAM GENERATION BASED ON GRAY_SCALE IMAGE (SEE CONTRAST-SHINE)
# Santiago Garcia Arango, 2020

import numpy as np
import cv2 as cv
import os
import time


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


def prob_pixel(val_pixel, img_gray):
    count_pixel = np.count_nonzero(img_gray == val_pixel)
    h, w = img_gray.shape[:2]
    return (count_pixel / (h * w))


def create_histogram(window_name, img_gray):
    # Create specific dimensions for histogram
    wbins = 256  # Horizontal space
    hbins = 256  # Its convention, but we can use other max

    # Use built-in function to generate histogram with given boundaries
    histogram = cv.calcHist([img_gray], [0], None, [hbins], [0, wbins])

    # Find max and min values (and locations) in histogram
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(histogram)

    print("val:({}, {}), p({}, {})".format(min_val, max_val, min_loc, max_loc))

    # We will show histogram on a new image
    img_hist = np.zeros((hbins, wbins, 3), np.uint8)

    for w in range(wbins):
        intensity = int(histogram[w][0] * (hbins - 1) / max_val)
        cv.line(img_hist, (w, hbins), (w, hbins-intensity), (55, 255, 255), 2)

    show_img(window_name, img_hist)

    return 0


def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "atardecer.png")

    # Read image
    img = cv.imread(img_path, 1)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    probability_0 = prob_pixel(0, img_gray)
    print("P(0) = ", probability_0*100)

    create_histogram("histogram", img_gray)


    show_img("img", img)
    show_img("img_gray", img_gray)

    close_all()


if __name__ == "__main__":
    main()
