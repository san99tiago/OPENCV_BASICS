# READ AN IMAGE WITH 
# Santiago Garcia Arango, June 2020

import cv2
import os

# Get the path for the folder that contains the images
upper_dir = os.path.dirname(os.path.dirname(__file__))  # Two dirs up
img_folder_path =  os.path.abspath(os.path.join(upper_dir, "imgs"))
print("\nPATH TO IMAGES: ", img_folder_path)


print("\nTHIS IS HOW WE READ AN IMAGE :)")
img = cv2.imread(os.path.join(img_folder_path, "astronaut.jpg"))
img = cv2.resize(img, (int(300),int(500)) )

cv2.imshow('Original' , img)

# Allow image to show up and will be there until a key is pressed
cv2.waitKey(0)

# Final operation in process that collapses all images when is executed 
cv2.destroyAllWindows()  # (always at the end)
