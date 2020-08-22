# PROJECT TO WORK WITH MOUSE EVENTS
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


# Mouse click event to obtain (x, y) coordinates with left clicks (down-up)
# ... also we obtain the clicked pixels info
def mouse_click(event, x, y, flags, param):
    global h1, w1, h2, w2
    if (event == cv.EVENT_LBUTTONDOWN):
        h1 = y
        w1 = x
        print("\nLEFT BUTTON DOWN...(x, y) = ({}, {})".format(x, y))
        print("CURRENT PIXEL: [{}, {}, {}]".format(
            img[y, x][0], img[y, x][1], img[y, x][2])
            )

    if (event == cv.EVENT_LBUTTONUP):
        h1 = y
        w1 = x
        print("\nLEFT BUTTON UP...(x, y) = ({}, {})".format(x, y))
        print("CURRENT PIXEL: [{}, {}, {}]".format(
            img[y, x][0], img[y, x][1], img[y, x][2])
            )


def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    img_path = get_img_path(img_folder_path, "21.png")

    global img
    img = cv.imread(img_path, 1)
    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    cv.namedWindow("MyMouseClick")
    cv.setMouseCallback("MyMouseClick", mouse_click)

    while (True):
        # Exit
        if (cv.waitKey(1) & 0xFF == ord("q")):
            break

        # Keep showing images
        cv.imshow("MyMouseClick", img)


if __name__ == "__main__":
    main()
    cv.destroyAllWindows()  # (always at the end)
