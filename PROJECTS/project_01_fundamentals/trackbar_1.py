# PROJECT TO WORK WITH CREATING A TRACKBAR TO APPLY FILTERS
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


# Our usefull function to properly work with a trackbar
def nothing(x):
    pass


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "21.png")

    img = cv.imread(img_path, 1)

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Change to grayscale
    imgGrayBin = imgGray.copy()

    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    cv.namedWindow("TrackBar")
    cv.createTrackbar("U", "TrackBar", 0, 255, nothing)

    # Main loop to keep updating image
    while (True):

        # Exit when "q" key is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")):
            break

        U = cv.getTrackbarPos("U", "TrackBar")

        # Keep showing images
        cv.imshow("TrackBar", imgGray)
        cv.imshow("ImgGrayBin", imgGrayBin)


        # Apply a filter treshold to specific channels
        for i in range(0, h):
            for j in range(0, w):
                if (imgGray[i, j] < U):
                    imgGrayBin[i, j] = 0
                else:
                    imgGrayBin[i, j] = 255


if __name__ == "__main__":
    main()
    cv.destroyAllWindows()  # (always at the end)
