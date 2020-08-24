# THIRD CHALLENGE (COUNT AMOUNT OF VERTICAL PIECES AND ITS DISTANCES IN PIXELS)
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


def count_pieces_and_distance(img):
    h, w = img.shape[:2]  # Get the shape of the image (height, width)

    h_half = round(h/2)

    vector_of_wi_left_edges = []
    for wi in range(w-4):
        # Condition where two left pixels are white and two right are black
        # This condition is the same as the "beggining of a line"
        if (
            img[h_half, wi]==255
            and img[h_half, wi+1]==255
            and img[h_half, wi+2]==0
            and img[h_half, wi+3]==0):
            vector_of_wi_left_edges.append(wi+2)

    # Create a new vector of differences in positions of lines (pixel's size)
    distances = []
    for pos in range(len(vector_of_wi_left_edges) - 1):
        next_position = vector_of_wi_left_edges[pos+1]
        current_position = vector_of_wi_left_edges[pos]
        current_distance = next_position - current_position
        distances.append(current_distance)

    # Find average of distance vector
    average_distance_between_pieces = np.mean(distances)

    print("VECTOR OF LINE STARTS: ", vector_of_wi_left_edges)
    print("VECTOR OF DISTANCES: ", distances)
    print("TOTAL LINES COUNT: ", len(vector_of_wi_left_edges))
    print("AVERAGE PIXELS BETWEEN LINES: ", average_distance_between_pieces)


def main():
    # Get the paths for the images
    img_path = get_img_path(get_imgs_folder_path(), "barras.png")

    img = cv.imread(img_path, 1)

    # Convert original img to grayscale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply a treshold to binarize the image
    retval, img_binarized = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
    img_binarized = img_binarized[:,:,0]  # Pick only one of the channels

    # Main function to count the amount of vertical pieces (and distance)
    count_pieces_and_distance(img_binarized)

    # Show main imgs to achieve objective
    cv.imshow("img", img)
    cv.imshow("img_gray", img_gray)
    cv.imshow("img_binarized", img_binarized)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
