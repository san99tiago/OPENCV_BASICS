# PROJECT TO REFLECT AN IMAGE BASED ON A VERTICAL AND HORIZONTAL AXES
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

# Now we play to generate 3 new images with Blue, Green, Red backgrounds
x_reflection = np.zeros((h, w, 3), np.uint8)
y_reflection = np.zeros((h, w, 3), np.uint8)


for i in range(0, h):
    for j in range(0, w):
        x_reflection[i, j] = imgColor[h-1-i, j]  # The "-1" is because index 0
        y_reflection[i, j] = imgColor[i, w-1-j]  # The "-1" is because index 0

cv.imshow("Original", imgColor)
cv.imshow("X_reflected", x_reflection)
cv.imshow("Y_reflected", y_reflection)


# Save obtained images
try:
    save_img.SaveResult(x_reflection, "X_reflection.jpg", __file__)
    save_img.SaveResult(y_reflection, "Y_reflection.jpg", __file__)
except:
    pass

cv.waitKey(0)  # Show image until a key is pressed
cv.destroyAllWindows()  # (always at the end)
