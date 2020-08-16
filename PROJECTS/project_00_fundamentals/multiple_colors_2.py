# PROJECT TO SHOW AN IMAGE WITH MULTIPLE COLORS BASED ON SUB-SQUARES
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# This way we can access upper package to save images in output folder
os.sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from SaveImg import save_img

# Get the path for the folder that contains the input and output images
upper_dir = os.path.dirname(__file__)  # Upper dir
img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))

# Get specific path to the images we will use inside the "imgs" folder
path_delfin = os.path.join(img_folder_path, "delfin.jpg")

# Loading our image with its path and parameter to change format
imgColor = cv.imread(path_delfin, 1)

h, w = imgColor.shape[:2]  # Get the shape of the image (height, width, c)


# Let the user insert "h" and "w" percentage where the colors change
h_user = int(input("Insert height percentage to cut image"))
w_user = int(input("Insert width percentage to cut image"))

# Convert the user's input percentages into valid "h" and "w" values
h_user = (h_user * h)/100
w_user = (w_user * w)/100

# Now we play to generate 3 new images with Blue, Green, Red backgrounds
new_img = np.zeros((h, w, 3), np.uint8)

for i in range(0, h):
    for j in range(0, w):
        # Check upper left portion (keep original format)
        if (i < h_user and j < w_user):
            new_img[i, j] = imgColor[i, j]  # Same original pixels

        # Check upper right portion (change to blue pixels only)
        if (i < h_user and j > w_user):
            new_img[i, j] = [imgColor[i, j][0], 0, 0]  # Blue pixels only

        # Check lower left portion (change to green pixels only)
        if (i > h_user and j < w_user):
            new_img[i, j] = [0, imgColor[i, j][1], 0]  # Green pixels only

        # Check lower right portion
        if (i > h_user and j > w_user):
            new_img[i, j] = [0, 0, imgColor[i, j][2]]  # Red pixels only



cv.imshow("Original", imgColor)
cv.imshow("New Image", new_img)


# Save obtained images
try:
    # save_img.SaveResult(new_img, "Multi_colors_65_25.jpg", __file__)
    pass
except:
    pass

cv.waitKey(0)  # Show image until a key is pressed
cv.destroyAllWindows()  # (always at the end)
