# CHALLENGE FOUR (OPEN ANY IMAGE AND GENERATE A CROP FROM IT WITH MOUSE)
# Santiago Garcia Arango, 2020

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


# Main function to work with mouse-clicks for image cropping
def mouse_click(event, x, y, flags, param):
    global h1, h2, w1, w2
    if (event == cv.EVENT_LBUTTONDOWN):
        h1 = y
        w1 = x
        print("\nLEFT BUTTON DOWN...(x, y) = ({}, {})".format(x, y))

    if (event == cv.EVENT_LBUTTONUP):
        h2 = y
        w2 = x
        print("LEFT BUTTON UP...(x, y) = ({}, {})".format(x, y))

        # Find upper and lower values for height and width
        h_min = min(h1, h2)
        h_max = max(h1, h2)
        w_min = min(w1, w2)
        w_max = max(w1, w2)

        # Crop new image with the limits found with mouse-clicks
        cropped_image = img[h_min:h_max,w_min:w_max,:]

        # Keep showing cropped image, until "q" key is pressed
        while True:
            cv.imshow("cropped_image", cropped_image)
            if (cv.waitKey(1) & 0xFF == ord("q")):
                cv.destroyWindow("cropped_image")
                break


def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "rick_morty.jpg")

    global img
    img = cv.imread(img_path, 1)

    # Add window that allows a callback-function for events (clicks)
    cv.namedWindow("MyMouseClick")
    cv.setMouseCallback("MyMouseClick", mouse_click)

    # Explain the user the procedure (in a pop-up text on image)
    cv.putText(img, "Crop an image with mouse", (30, 30),
        cv.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (255, 255, 55), 1)

    while (True):
        # Exit
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break

        # Keep showing images
        cv.imshow("MyMouseClick", img)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
