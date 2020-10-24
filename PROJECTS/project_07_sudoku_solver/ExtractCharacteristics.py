# EXTRACT CHARACTERISTICS FOR A GIVEN INPUT IMAGE OF A NUMBER
# Santiago Garcia Arango

import cv2 as cv
import numpy as np
import xlsxwriter
import glob
import os


class ExtractCharacteristics:
    def __init__(self, imageBin):
        # Resize given image to default pixels to standarize all imgs
        self.imgBin = cv.resize(imageBin, (30, 60))

        ret, self.imgBin = cv.threshold(self.imgBin, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)


        # Get main BGR (color) image from binary input (be able to draw cnts)
        self.imgColor = cv.cvtColor(self.imgBin, cv.COLOR_GRAY2BGR)

        # cv.imshow("test1", self.imgColor)
        # cv.waitKey(0)

        # Get main contours from given image
        self.contours, self.hie = cv.findContours(self.imgBin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)


    def get_imgs_folder_path(self, folder_name):
        # Get the path for the folder that contains the input and output images
        upper_dir = os.path.dirname(__file__)  # Upper dir
        img_folder_path = os.path.abspath(os.path.join(upper_dir, folder_name))
        return img_folder_path


    def get_characteristics(self, show_images):
        check_correct_contour = 0
        for cont in self.contours:
            x, y, w, h = cv.boundingRect(cont)
            
            if (cv.contourArea(cont) > 100):
                check_correct_contour = check_correct_contour + 1
                # Draw rectangle on top of img
                cv.rectangle(self.imgColor, (x,y), (x+w, y+h), (255, 0, 0), 2)

                if show_images == "fast":
                    # Show current img and contour for a few seconds
                    cv.imshow("img", self.imgColor)
                    cv.waitKey(1)
                elif show_images == "slow":
                    # Show current img and contour for until pressed key
                    cv.imshow("img", self.imgColor)
                    cv.waitKey(0)


                # Extract characteristics
                area = w*h
                areaf = cv.contourArea(cont)
                aspect_relation = w/h
                perim = cv.arcLength(cont, 1)
                M = cv.moments(cont)
                Hu = cv.HuMoments(M)  # Get Hu moments

                # Get centroids
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Get specific amount of white pixels from first vertical half
                pixeles_h_2 = 0
                for h_i in range(h//2):
                    for w_i in range(w):
                        if self.imgBin[h_i, w_i] == 255:
                            pixeles_h_2 = pixeles_h_2 + 1


                # Get specific amount of white pixels from first horizontal half
                pixeles_w_2 = 0
                for h_i in range(h):
                    for w_i in range(w//2):
                        if self.imgBin[h_i, w_i] == 255:
                            pixeles_w_2 = pixeles_w_2 + 1


                # Create vector with this important information
                vector_characteristics = np.array([area, areaf,
                            aspect_relation, perim, Hu[0][0],
                            Hu[1][0], Hu[2][0], Hu[3][0], Hu[4][0],
                            cX, cY,
                            pixeles_h_2, pixeles_w_2], dtype= np.float)

        # Only return vector when the contours got the correct characteristics
        if check_correct_contour == 0:
            return None
        else:
            return vector_characteristics

    def write_characteristics(self, show_images):
        # Create vector to go through each "object" to classify
        vector_folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # Create xlsx workbook to add info
        path_xlsx = os.path.join(os.path.dirname(__file__), "characteristics.xlsx")
        workbook = xlsxwriter.Workbook(path_xlsx)
        worksheet = workbook.add_worksheet("chars_for_sudoku")

        row = 0
        col = 0
        i = 1

        # Get main path to the training img folders
        num_path = self.get_imgs_folder_path("training_imgs")

        # Go to each img in every folder
        for j in range(0, len(vector_folders)):
            current_path = os.path.join(num_path, vector_folders[j])
            for path in glob.glob(current_path + "/*.png"):

                # Call main method to extract all characteristics
                image = cv.imread(path, 0)
                chars = ExtractCharacteristics(image)
                vector_characteristics = chars.get_characteristics(show_images)

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


# ----------------------TEST CHARACTERISTICS EXTRACTION ----------------------

if __name__ == "__main__":
    filename =  os.path.dirname(__file__) + "/training_imgs/1/1 (0).png"
    image = cv.imread(filename, 0)

    chars = ExtractCharacteristics(image)
    result_vector = chars.get_characteristics("fast")

    chars.write_characteristics("fast")
    
    cv.waitKey(0)
    cv.destroyAllWindows()
