# ATTEMPT FOR FACIAL DETECTION
# Santiago Garcia Arango
# Inspired by: https://realpython.com/face-recognition-with-python/


import cv2 as cv
import os

CURRENT_FOLDER = os.path.abspath(os.path.dirname(__file__))
print(CURRENT_FOLDER)

def main(image_relative_path):
    # Create the haar cascade
    casc_path = os.path.join(CURRENT_FOLDER, "haarcascade_frontalface_default.xml")  # From OpenCV Github
    faceCascade = cv.CascadeClassifier(casc_path)

    # Read image
    image_relative_path = os.path.join(CURRENT_FOLDER, image_relative_path)
    image = cv.imread(image_relative_path)
    if image is None:
        print("ERROR: Image did not load.")
        return False

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Detect faces in the image (vector of faces with rectangle dimensions)
    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv.CASCADE_SCALE_IMAGE
    )

    # print(faces)
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (255, 255, 55), 3)

    cv.imshow("FACES DETECTED", image)
    cv.waitKey(0)


if __name__ == "__main__":
    # TEST 1
    image_relative_path = os.path.join("test_imgs", "picture0.PNG")
    print(image_relative_path)
    main(image_relative_path)

    # TEST 2
    image_relative_path = os.path.join("test_imgs", "picture1.PNG")
    print(image_relative_path)
    main(image_relative_path)

    # TEST 3
    image_relative_path = os.path.join("test_imgs", "picture2.PNG")
    print(image_relative_path)
    main(image_relative_path)

    # TEST 4
    image_relative_path = os.path.join("test_imgs", "picture3.PNG")
    print(image_relative_path)
    main(image_relative_path)
