# SCRIPT TO GET THE MATRIX OF NUMBERS FOR A GIVEN SUDOKU IMAGE
# Santiago Garcia Arango

# My other modules
import ExtractCharacteristics as EXCHAR
import MultilayerPerceptron as MyMLP


# Main modules for arrays, excel, image processing, file-handling
import cv2 as cv
import numpy as np 
import xlsxwriter
import glob
import os



class GetSudokuBoard:
    def __init__(self, img_name):
        self.img_folder_path = self.get_imgs_folder_path("sudoku_imgs")
        self.image_path = self.get_img_path(self.img_folder_path, img_name)
        self.img_sudoku = cv.imread(self.image_path, 0)

        # Train and load main Machine Learning model
        model = MyMLP.MulilayerPerceptron("characteristics.xlsx")
        self.mlp = model.train_MLP()


        cv.imshow("original_sudoku", self.img_sudoku)
        self.get_each_square()



    def get_imgs_folder_path(self, folder_name):
        # Get the path for the folder that contains the input and output images
        upper_dir = os.path.dirname(__file__)  # Upper dir
        img_folder_path = os.path.abspath(os.path.join(upper_dir, folder_name))
        return img_folder_path


    def get_img_path(self, img_folder_path, img_name):
        # Get specific path to the images we will use inside the "imgs" folder
        img_path = os.path.join(img_folder_path, img_name)
        return img_path


    def get_each_square(self):
        # Crop new image with the limits found with mouse-clicks
        h, w = self.img_sudoku.shape[:2]
        print(h, w)

        # Get average pixels for each square of the sudoku (to get images)
        avg_h = h // 9
        avg_w = w // 9

        # Variables to go through
        current_h = 0
        current_w = 0

        # Initialize main sudoku matrix to get numbers from each square
        self.number_matrix = np.zeros((9,9))

        # Loop through each square and process the image to get the specific...
        # ... number of that square (to get the matrices of numbers)
        for i in range(9):
            for j in range(9):
                # Specific limits of each square to crop 
                bottom = current_h + avg_h // 4
                top = current_h + avg_h - avg_h // 8
                left = current_w + avg_w // 4
                right = current_w + avg_w - avg_w // 6

                # Crop current square based on limits given
                current_img = self.img_sudoku[bottom:top, left:right]


                cv.imshow("current", current_img)
                cv.waitKey(0)
                cv.destroyWindow("current")



                # Main algorithm for image processing of each number
                self.number_matrix[i][j] = self.obtain_number(current_img)
                print(self.number_matrix)



                current_w = current_w + avg_w

            current_w = 0
            current_h = current_h + avg_h


    def obtain_number(self, current_img):
        chars = EXCHAR.ExtractCharacteristics(current_img)
        vector_characteristics = chars.get_characteristics("slow")

        print(vector_characteristics)

        if vector_characteristics is not None:
            current_number = self.mlp.predict([vector_characteristics])
        else:
            current_number = 0

        return current_number




if __name__ == "__main__":
    s1 = GetSudokuBoard("Sudoku_R2.PNG")
    cv.waitKey(0)
    cv.destroyAllWindows()



