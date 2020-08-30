# Simple challenge: get probability of specific pixel value in image
import time
import cv2 as cv
import numpy as np

time_1 = time.time()

img = cv.imread("atardecer.PNG", 1)


img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

total = np.shape(img)[0]*np.shape(img)[1]


print(total)
zero_conditions = img[img==0]

p0 = len(zero_conditions) / total

total_time = time.time() - time_1

print("P(0) = {}".format(p0*100))
print("time = {}".format(total_time))
