# FUNCTION TO SAVE IMAGES CORRECTLY IN OUTPUT FOLDER LOCATED IN SAME DIR
# Santiago Garcia Arango, August 2020

import cv2 as cv
import os

class SaveResult:
    def __init__(self, img, save_name, file_run):
        upper_dir = os.path.dirname(file_run)  # Directory of "file_run"
        output_folder_path = os.path.abspath(os.path.join(upper_dir, "output"))

        # Check if folder already exists (otherwise, create it)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        final_path = os.path.join(output_folder_path, save_name)
        cv.imwrite(final_path, img)  # Save image with opencv built-in function

