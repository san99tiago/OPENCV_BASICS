#READ AN IMAGE WITH 
#Santiago Garcia Arango, June 2020

import cv2
import os

#Get the path for the folder that contains the images (two directories up, and folder "imgs")
img_folder_path =  os.path.dirname( os.path.dirname( __file__ ) ) + "\\imgs\\" 
print( img_folder_path )


print("This is how we read an image!!!")
img = cv2.imread(img_folder_path + "astronaut.jpg")
img = cv2.resize(img, (int(300),int(500)) )

cv2.imshow('Original' , img)

#Allow image to show up and will be there until a key is pressed
cv2.waitKey(0)

#Final operation in process that collapses all images when is executed (always at the end)
cv2.destroyAllWindows()


