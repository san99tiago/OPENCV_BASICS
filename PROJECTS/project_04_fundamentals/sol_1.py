# SOLUTION 1 (FIX LICENSE PLATES IMAGES)
# Santiago Garcia Arango, September 2020

import numpy as np
import cv2 as cv
import os

def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "malas"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def fix_image_type_A(img):
    # Change orientation of image to fix them
    h, w = img.shape[:2]  # Get the shape of the image (height, width, c)

    # Now we play to generate 3 new images with Blue, Green, Red backgrounds
    reflection = np.zeros((h, w, 3), np.uint8)

    # Change image from specific reflections
    for i in range(0, h):
        for j in range(0, w):
            reflection[i, j] = img[h-1-i, w-1-j]  # "-1" because index 0

    print("...Done fixing current image\n")
    return reflection


def fix_image_type_B(img):
    # Change orientation of image to fix them
    h, w = img.shape[:2]  # Get the shape of the image (height, width, c)

    # Now we play to generate 3 new images with Blue, Green, Red backgrounds
    reflection = np.zeros((h, w, 3), np.uint8)

    # Change image from specific reflections
    for i in range(0, h):
        for j in range(0, w):
            reflection[i, j] = img[h-1-i, j]  # "-1" because index 0

    print("...Done fixing current image\n")
    return reflection


def main():
    # Get the paths for all the images (for all imgs to be fixed)
    img_1 = get_img_path(get_imgs_folder_path(), "placa_1_P1.png")
    img_2 = get_img_path(get_imgs_folder_path(), "placa_2_P1.png")
    img_3 = get_img_path(get_imgs_folder_path(), "placa_3_P1.png")
    img_4 = get_img_path(get_imgs_folder_path(), "placa_4_P1.png")
    img_5 = get_img_path(get_imgs_folder_path(), "placa_5_P1.png")

    print("\n\n ***** PRESS ENTER TO KEEP SHOWING FIXED IMAGES *****\n\n")

    # Fix image 1
    print("\nFIXING IMAGE 1:")
    img_1 = cv.imread(img_1, 1)
    img_1_fixed = fix_image_type_A(img_1)
    cv.imshow("img_1", img_1)
    cv.imshow("img_1_fixed", img_1_fixed)

    # Press enter to keep showing other images
    while True:
        if (cv.waitKey(1) & 0xFF == 13):
            cv.destroyAllWindows()
            break

    # Fix image 2
    print("\nFIXING IMAGE 2:")
    img_2 = cv.imread(img_2, 1)
    img_2_fixed = fix_image_type_A(img_2)
    cv.imshow("img_2", img_2)
    cv.imshow("img_2_fixed", img_2_fixed)

    # Press enter to keep showing other images
    while True:
        if (cv.waitKey(1) & 0xFF == 13):
            cv.destroyAllWindows()
            break

    # Fix image 3
    print("\nFIXING IMAGE 3:")
    img_3 = cv.imread(img_3, 1)
    img_3_fixed = fix_image_type_A(img_3)
    cv.imshow("img_3", img_3)
    cv.imshow("img_3_fixed", img_3_fixed)

    # Press enter to keep showing other images
    while True:
        if (cv.waitKey(1) & 0xFF == 13):
            cv.destroyAllWindows()
            break

    # Fix image 4
    print("\nFIXING IMAGE 4:")
    img_4 = cv.imread(img_4, 1)
    img_4_fixed = fix_image_type_B(img_4)
    cv.imshow("img_4", img_4)
    cv.imshow("img_4_fixed", img_4_fixed)

    # Press enter to keep showing other images
    while True:
        if (cv.waitKey(1) & 0xFF == 13):
            cv.destroyAllWindows()
            break

    # Fix image 5
    print("\nFIXING IMAGE 5:")
    img_5 = cv.imread(img_5, 1)
    img_5_fixed = fix_image_type_B(img_5)
    cv.imshow("img_5", img_5)
    cv.imshow("img_5_fixed", img_5_fixed)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
