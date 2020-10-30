# WRITE CHARACTERISTICS IN EXCEL FILE
# Santiago Garcia Arango

import ExtractCharacteristics as EXCHAR


import cv2 as cv
import numpy as np
import xlsxwriter
import glob
import os


def write_characteristics(xlsx_filename):
    # Create vector to go through each "object" to classify
    vector_folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Create xlsx workbook to add info
    path_xlsx = os.path.join(os.path.dirname(__file__), xlsx_filename)
    workbook = xlsxwriter.Workbook(path_xlsx)
    worksheet = workbook.add_worksheet("chars_for_sudoku")

    # Get main path to the training img folders
    upper_dir = os.path.dirname(__file__)  # Upper dir
    num_path = os.path.abspath(os.path.join(upper_dir, "training_imgs"))

    # Define conditions for the xlsxwriter library (rows and columns)
    row = 0
    col = 0
    i = 1

    # Go to each img in every folder
    for j in range(0, len(vector_folders)):
        current_path = os.path.join(num_path, vector_folders[j])
        for path in glob.glob(current_path + "/*.png"):

            # Call main method to extract all characteristics
            image = cv.imread(path, 0)
            chars = EXCHAR.ExtractCharacteristics(image)
            vector_characteristics = chars.get_characteristics("fast")

            # Sometimes the characteristics can't be achieved... avoid error
            if vector_characteristics is not None:
                # Write characteristics in Excel document
                for charac in (vector_characteristics):
                    worksheet.write(row, col, vector_folders[j])
                    worksheet.write(row, i, charac)
                    i = i + 1
                i = 1
                row = row + 1

    cv.destroyWindow("img")  # Close last image that is shown
    workbook.close()


# ----------------------TEST CHARACTERISTICS WRITING ----------------------

if __name__ == "__main__":
    write_characteristics("characteristics.xlsx")
    cv.waitKey(0)
    cv.destroyAllWindows()
