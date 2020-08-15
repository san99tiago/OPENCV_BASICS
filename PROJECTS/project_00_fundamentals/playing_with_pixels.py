# PLAYING WITH PIXELS IN IN OPENCV
# Santiago Garcia Arango, August 2020

import cv2 as cv
import os

# Get the path for the folder that contains the images
upper_dir = os.path.dirname(__file__)  # Upper dir
img_folder_path = os.path.abspath(os.path.join(upper_dir, "imgs"))
print("\nPATH TO IMAGES: ", img_folder_path)

# Get specific path to images with their names
path_delfin = os.path.join(img_folder_path, "delfin.jpg")

# Loading our image with its path and parameter to change format
imgColor = cv.imread(path_delfin, 1)
imgGray = cv.imread(path_delfin, 2)

# Change size of the images
imgGray = cv.resize(imgGray, (20, 20))

h, w = imgColor.shape[:2]  # Get the shape of the image (height, width, c)
print("Height of image: ", h)
print("Width of image: ", w)

cv.imshow("My first color image", imgColor)
cv.imshow("My first gray image", imgGray)

print("First row info: ", imgColor[0])
print("First pixel info: ", imgColor[0, 0])

cv.waitKey(0)  # Show image until a key is pressed
cv.destroyAllWindows()  # (always at the end)
