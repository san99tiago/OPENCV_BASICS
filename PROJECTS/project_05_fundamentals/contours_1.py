# WORKING WITH CONTOURS
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




def main():
    # Get the paths for all the images (for all imgs to be fixed)
    img_1 = get_img_path(get_imgs_folder_path(), "Patron.jpg")
    img_2 = get_img_path(get_imgs_folder_path(), "Patron_2.JPG")

    # Read images
    img_1 = cv.imread(img_1, 0)
    img_2 = cv.imread(img_2, 0)

    # Binarize images
    ret, img_1_bin = cv.threshold(img_1, 128, 255, cv.THRESH_BINARY_INV)
    ret, img_2_bin = cv.threshold(img_2, 128, 255, cv.THRESH_BINARY_INV)

    # Show original images
    cv.imshow("img_1_bin", img_1_bin)
    cv.imshow("img_2_bin", img_2_bin)

    # Get countours and hierarchy
    cnt, hie = cv.findContours(img_1_bin, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    print("HIERARCHY: \n", hie)

    # Get img size and create a black image
    h, w = img_1.shape[:2]
    imgCnt = np.zeros((h, w, 3), np.uint8)


    for cont in cnt:
        color = list(np.random.random(size=3)*256)

        cv.drawContours(imgCnt, cont, -1, color, 1)


    cv.imshow("contornos", imgCnt)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
