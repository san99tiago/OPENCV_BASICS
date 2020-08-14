# PROJECT TO SHOW AN IMAGE IN THE RED, GREEN AND BLUE FORMATS
# Santiago Garcia Arango, August 2020

import numpy as np
import cv2 as cv
import os

# Get the path for the folder that contains the images
upper_dir = os.path.dirname(os.path.dirname(__file__))  # Two dirs up
img_folder_path =  os.path.abspath(os.path.join(upper_dir, "imgs"))
print("\nPATH TO IMAGES: ", img_folder_path)

# Get specific path to the images we will use inside the "imgs" folder
path_delfin = os.path.join(img_folder_path, "delfin.jpg")

# Loading our image with its path and parameter to change format
imgColor = cv.imread(path_delfin, 1)

h,w = imgColor.shape[:2]  # Get the shape of the image (height, width, c)

# Now we play to generate 3 new images with Blue, Green, Red backgrounds
blue_copy = np.zeros((h,w,3), np.uint8)
red_copy = np.zeros((h,w,3), np.uint8)
green_copy = np.zeros((h,w,3), np.uint8)


for i in range(0, h):
    for j in range(0, w):
        # blue_copy[i,j] = [imgColor[i,j][0], 0, 0]  # Only save Blue data
        green_copy[i,j] = [0, imgColor[i,j][1], 0]  # Only save Green data
        red_copy[i,j] = [0, 0, imgColor[i,j][2]]  # Only save Red data

# blue_copy[:] = 

print(imgColor)
print(imgColor[0, 0])

# print(imgColor[10, 30])
# print(blue_copy[10, 30])
# print(red_copy[10, 30])

cv.imshow("My color image", imgColor)
cv.imshow("My blue copy", blue_copy)
cv.imshow("My red copy", red_copy)
cv.imshow("My green copy", green_copy)

cv.waitKey(0)  # Show image until a key is pressed
cv.destroyAllWindows()  # (always at the end)