# GENERAL SCRIPT TO OPEN IMAGE AND GENERATE MULTIPLE CROPS UNTIL "ENTER" KEY
# Santiago Garcia Arango, 2020

import numpy as np
import cv2 as cv
import os


def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "sudoku_imgs"))
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
        current_cropped_image = img[h_min:h_max,w_min:w_max,:]

        # Add cropped image to a global vector
        vector_cropped_imgs.append(current_cropped_image)



def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "Sudoku_R1.png")

    global img, vector_cropped_imgs
    img = cv.imread(img_path, 1)

    vector_cropped_imgs = []

    # Add window that allows a callback-function for events (clicks)
    cv.namedWindow("MyMouseClick")
    cv.setMouseCallback("MyMouseClick", mouse_click)


    while (True):
        # Exit
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break

        # If "enter" key is pressed
        if (cv.waitKey(1) & 0xFF == 13):
            for i in range(len(vector_cropped_imgs)):
                cv.imshow("crop # {}".format(i), vector_cropped_imgs[i])
            
            # After "enter" key is pressed, destroy vector of all cropped imgs
            vector_cropped_imgs = []

        # Keep showing images
        cv.imshow("MyMouseClick", img)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
