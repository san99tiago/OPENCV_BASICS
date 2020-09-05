# SOLUTION 2 (NEW ALGORITHM TO ZOOM IN FOR HOSPITAL X-RAY MACHINE)
# Santiago Garcia Arango, September 2020

import numpy as np
import cv2 as cv
import os

def get_imgs_folder_path():
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, "fractures"))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


# Main function to work with mouse-clicks for image zoom specifications
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

        # Create a copy of original image (to show it with zoomed one)
        img_copy = img.copy()

        # Draw zoomed rectangle on img (to show zoom to user)
        cv.rectangle(img_copy,
                (w_min, h_min),
                (w_max, h_max),
                (0, 255, 0),
                thickness=2)

        # Crop img with the limits found with mouse-clicks
        cropped_img = img_copy[h_min:h_max,w_min:w_max,:]

        # Function to zoom 10x an specific image
        zoomed_in_img = zoom_img(cropped_img)

        # Function to create final img results with original and zoomed imgs
        final_result = create_results(img_copy, zoomed_in_img)

        # After selected zoomed zone, show it until "s" key is pressed
        print("\n\nPress 's' key to exit")
        while True:
            cv.namedWindow("results", cv.WINDOW_NORMAL)
            cv.imshow("results", final_result)

            # If "s" key is pressed
            if (cv.waitKey(1) & 0xFF == ord('s')):
                cv.destroyWindow("results")
                break


def zoom_img(img):
    # recieve img and zoom-in in a rate of 1:10

    h, w = img.shape[:2]  # Get the shape of the image (height, width, c)

    zoomed_in_img = cv.resize(img, (int(w*10), int(h*10)))

    return zoomed_in_img


def create_results(img_copy, zoomed_in_img):
    # Get new h,w values to concatenate original image
    h_zoomed, w_zoomed = zoomed_in_img.shape[:2]

    # Resize original img to fit to zoomed in size (could change proportions)
    original_img_left = cv.resize(img_copy, (w_zoomed, h_zoomed))

    # Create a new img with both of them in one (original and zoomed in)
    final_result = np.concatenate(
        (original_img_left, zoomed_in_img), axis=1
        )

    return final_result


def main():
    # Get the path for the image to be analized
    img_path = get_img_path(get_imgs_folder_path(), "fractura.jpg")

    global img
    img = cv.imread(img_path, 1)

    # Add window that allows a callback-function for events (clicks)
    cv.namedWindow("ZoomWindow", cv.WINDOW_NORMAL)
    cv.setMouseCallback("ZoomWindow", mouse_click)

    # Explain the user the procedure (in a pop-up text on image)
    cv.putText(img, "select section to zoom:", (10, 10),
        cv.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (255, 255, 55), 1)


    while (True):
        # Exit if "q" key is pressed
        if (cv.waitKey(1) & 0xFF == ord("q")):
            cv.destroyAllWindows()
            break

        # Keep showing original image
        cv.imshow("ZoomWindow", img)


if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
