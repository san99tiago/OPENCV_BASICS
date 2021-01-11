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

            # Validate big area contour and NOT EDGE OF SUDOKU contour
            if ((cv.contourArea(cont) > 10) and (cont[0, 0, 0]>2) and 
                (cont[0, 0, 0]<27) and (cont[0, 0, 1]>2) and
                (cont[0, 0, 1]<27)):

                # Only get real image when finding "correct number"
                img_cropped = self.imgBin[y:y+h,x:x+w]
                img_cropped = cv.resize(img_cropped, (30, 60))
                img_cropped_color = cv.cvtColor(img_cropped, cv.COLOR_GRAY2BGR)


                # Now that it's a real number contour, find new contours
                new_contours, new_hie = cv.findContours(img_cropped, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
                for new_cont in new_contours:
                    x_new, y_new, w_new, h_new = cv.boundingRect(new_cont)
                    if (cv.contourArea(new_cont) > 40):

                        check_correct_contour = check_correct_contour + 1

                        # Draw rectangle on top of img
                        cv.rectangle(self.imgColor, (x,y), (x+w, y+h), (255, 0, 0), 2)
                        cv.rectangle(img_cropped_color, (x_new,y_new), (x_new+w_new, y_new+h_new), (255, 0, 0), 2)

                        if show_images == "fast":
                            # Show current img and contour for a few seconds
                            cv.imshow("img", self.imgColor)
                            cv.waitKey(100)
                            cv.destroyWindow("img")
                            cv.imshow("img_new", img_cropped_color)
                            cv.waitKey(100)
                            cv.destroyWindow("img_new")

                        elif show_images == "slow":
                            # Show current img and contour for until pressed key
                            cv.imshow("img", self.imgColor)
                            cv.waitKey(0)
                            cv.destroyWindow("img")
                            cv.imshow("img_new", img_cropped_color)
                            cv.waitKey(0)
                            cv.destroyWindow("img_new")


                        # Extract characteristics
                        area = w_new*h_new
                        areaf = cv.contourArea(new_cont)
                        aspect_relation = w_new/h_new
                        perim = cv.arcLength(new_cont, 1)
                        M = cv.moments(new_cont)
                        Hu = cv.HuMoments(M)  # Get Hu moments

                        # Get centroids
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])

                        # Get specific amount of white pixels from first vertical half
                        pixeles_h_2 = 0
                        for h_i in range(h_new//2):
                            for w_i in range(w_new):
                                if img_cropped[h_i, w_i] == 255:
                                    pixeles_h_2 = pixeles_h_2 + 1

                        # Get specific amount of white pixels from first horizontal half
                        pixeles_w_2 = 0
                        for h_i in range(h_new):
                            for w_i in range(w_new//2):
                                if img_cropped[h_i, w_i] == 255:
                                    pixeles_w_2 = pixeles_w_2 + 1

                        # Get extra characteristics for more differences
                        vertical_pixels_middle_left = 0
                        for w_i in range(w_new):
                            if img_cropped[h_new//2 - 3, w_i] == 255:
                                vertical_pixels_middle_left = vertical_pixels_middle_left + 1

                        # Get extra characteristics for more differences
                        vertical_pixels_middle_right = 0
                        for w_i in range(w_new):
                            if img_cropped[h_new//2 + 3, w_i] == 255:
                                vertical_pixels_middle_right = vertical_pixels_middle_right + 1

                        # Get extra characteristics for more differences
                        horizontal_pixels_middle_up = 0
                        for h_i in range(h_new):
                            if img_cropped[h_i, w_new//2 - 10] == 255:
                                horizontal_pixels_middle_up = horizontal_pixels_middle_up + 1

                        # Get extra characteristics for more differences
                        horizontal_pixels_middle_down = 0
                        for h_i in range(h_new):
                            if img_cropped[h_i, w_new//2 + 10] == 255:
                                horizontal_pixels_middle_down = horizontal_pixels_middle_down + 1

                        if img_cropped[50,10] == 255:
                            strategic_pixel_1 = 1
                        else:
                            strategic_pixel_1 = 0




                        # Create vector with this important information
                        vector_characteristics = np.array([areaf,
                                    perim, Hu[0][0],
                                    Hu[1][0], Hu[2][0], Hu[3][0],
                                    cX, cY,
                                    pixeles_h_2, pixeles_w_2,
                                    vertical_pixels_middle_left,
                                    vertical_pixels_middle_right,
                                    horizontal_pixels_middle_up,
                                    horizontal_pixels_middle_down,
                                    strategic_pixel_1], dtype= np.float)

                # Only return vector when the contours got the correct characteristics
                if check_correct_contour == 0:
                    return None
                else:
                    return vector_characteristics


# ----------------------TEST CHARACTERISTICS EXTRACTION ----------------------

if __name__ == "__main__":
    filename =  os.path.dirname(__file__) + "/training_imgs/1/1 (0).png"
    image = cv.imread(filename, 0)

    chars = ExtractCharacteristics(image)
    result_vector = chars.get_characteristics("slow")
    print(result_vector)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
