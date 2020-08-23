# FIRST PART OF SECOND CHALLENGE (FIND AVERAGE COIN SIZE)
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# Vector to keep the (h, w) values of selected coins
coin_dimensions = []


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
# ... also we obtain the clicked pixels' info
def mouse_click(event, x, y, flags, param):
    global h1, w1, h2, w2, coin_dimensions, COIN_HEIGHT, COIN_WIDTH
    if (event == cv.EVENT_LBUTTONDOWN):
        h1 = y
        w1 = x
        print("\nLEFT BUTTON DOWN...(x, y) = ({}, {})".format(x, y))

    if (event == cv.EVENT_LBUTTONUP):
        h2 = y
        w2 = x
        print("\nLEFT BUTTON UP...(x, y) = ({}, {})".format(x, y))

        # Get the current selected coin size
        current_coin_h = abs(h1-h2)
        current_coin_w = abs(w1-w2)

        # Add current coin dimensions to vector of dimensions
        coin_dimensions.append((current_coin_h, current_coin_w))
        print("VECTOR OF COIN DIMENSIONS ", coin_dimensions)

        # Everytime a coin is added, re-calculate the averege height and width
        COIN_HEIGHT = 0
        COIN_WIDTH = 0
        for hi, wi in coin_dimensions:
            COIN_HEIGHT = COIN_HEIGHT + hi
            COIN_WIDTH = COIN_WIDTH + wi
        total_coins = len(coin_dimensions)
        COIN_HEIGHT = int(COIN_HEIGHT / total_coins)
        COIN_WIDTH = int(COIN_WIDTH / total_coins)

        print("AVERAGE COINS SIZE = ({}, {})".format(COIN_HEIGHT, COIN_WIDTH))



def main():
    # Get the paths for the images
    img_folder_path = get_imgs_folder_path()
    # img_path = get_img_path(img_folder_path, "21.png")
    img_path = get_img_path(img_folder_path, "monedas.jpg")

    global img
    img = cv.imread(img_path, 1)

    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    # Add window that allows a callback-function for events (clicks)
    cv.namedWindow("MyMouseClick")
    cv.setMouseCallback("MyMouseClick", mouse_click)

    # Explain the user the procedure (in a pop-up text)
    cv.putText(img, "Select the images in squares!", (30, 30),
        cv.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (0, 0, 0), 1)

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
    cv.destroyAllWindows()  # (always at the end)
