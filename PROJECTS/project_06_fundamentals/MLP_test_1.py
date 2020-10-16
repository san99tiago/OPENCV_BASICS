# MAIN MULTILAYER PERCEPTRON TO TRAIN NEURAL NET
# Santiago Garcia Arango

from extract_characteristics import extract_characteristics

import numpy as np
import cv2 as cv
import xlrd
from time import time
import os
import glob
import random

#Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, RobustScaler

from sklearn.metrics import accuracy_score
#from sklearn.metrics import confusion_matrix
#from sklearn.model_selection import cross_val_score


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path



def load_xlsx(xlsx):
    
    sh = xlsx.sheet_by_index(0)
    x = np.zeros((sh.nrows,sh.ncols-1))
    y = []
    for i in range(0, sh.nrows):
        for j in range(0, sh.ncols-1):
            x[i,j] = sh.cell_value(rowx=i, colx=j+1)
        #print (sh.cell_value(rowx=i, colx=0))   
        if(sh.cell_value(rowx=i, colx=0)=='0'):
            y.append(0)
        elif(sh.cell_value(rowx=i, colx=0)=='1'):
            y.append(1)
        elif(sh.cell_value(rowx=i, colx=0)=='2'):
            y.append(2)
        elif(sh.cell_value(rowx=i, colx=0)=='3'):
            y.append(3)
        elif(sh.cell_value(rowx=i, colx=0)=='4'):
            y.append(4)
        elif(sh.cell_value(rowx=i, colx=0)=='5'):
            y.append(5)
        elif(sh.cell_value(rowx=i, colx=0)=='6'):
            y.append(6)
        elif(sh.cell_value(rowx=i, colx=0)=='7'):
            y.append(7)
        elif(sh.cell_value(rowx=i, colx=0)=='8'):
            y.append(8)
        elif(sh.cell_value(rowx=i, colx=0)=='9'):
            y.append(9)
    y= np.array(y,np.float32)
    return x, y




if __name__ == '__main__':
    # Read main excel document where the characteristics are located
    path_xlsx = os.path.join(os.path.dirname(__file__), "characteristics.xlsx")
    book_excel = xlrd.open_workbook(path_xlsx)

    # Load main excel file with the X and Y matrices strategically
    X, Y = load_xlsx(book_excel)
    print("[len(x), len(Y)] = [{}, {}]".format(len(X), len(Y)))


    # Separe data into training and validation
    x1, x2, y1, y2 = train_test_split(X, Y, test_size = 0.3)    

    # Declare main MLP classifier with its characteristics
    mlp = MLPClassifier(activation='logistic', hidden_layer_sizes=(50,50), 
                        max_iter=1000, tol=0.0001)

    # Train the model with the training data
    mlp.fit(x1, y1)

    # Get the accuracy of the model with the validationo data
    print ("Accuracy Score: ", mlp.score(x2, y2)*100.0)


    # See actual results from training samples...
    print("ENTER \"F\" TO QUIT")
    while True:
        # Get user input to test the MLP
        user_input = str(input(("\nInsert number to test --> ")))

        # Exit when user presses "F"
        if user_input == "F":
            break

        # Get paths for the folder of imgs of selected number
        current_path = os.path.abspath(os.path.dirname(__file__))
        numbers_path = os.path.join(current_path, "num", user_input)

        # Vector of all possible paths for the images of current number
        possible_paths = glob.glob(os.path.join(numbers_path, "*.png"))

        # Select only one image path to test MLP at a time
        path = random.choice(possible_paths)

        vector_characteristics = extract_characteristics(path, "slow")

        print("\nTESTED NUMBER --> ", path)
        print("PREDICTED NUMBER --> ", mlp.predict([vector_characteristics]))

        cv.destroyAllWindows()
