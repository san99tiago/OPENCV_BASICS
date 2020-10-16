# MAIN MULTILAYER PERCEPTRON TO TRAIN NEURAL NET
# Santiago Garcia Arango

import numpy as np
import cv2
import xlrd
from time import time

#Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, RobustScaler

from sklearn.metrics import accuracy_score
#from sklearn.metrics import confusion_matrix
#from sklearn.model_selection import cross_val_score


def get_current_folder():
    # Get the path for the folder that this file is located on
    upper_dir = os.path.dirname(__file__)  # Upper dir
    return upper_dir



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
    return x,y


if __name__ == '__main__':
    # Read main excel document where the characteristics are located
    book_excel = xlrd.open_workbook("characteristics.xlsx")



    t0 = time()
    
    # Cargar datos desde un archivo .xlsx
    # la función retornará el número de muestras obtenidas y su respectiva clase
    X, Y = load_xlsx(book_excel)
    print(len(X), len(Y))

    #standard_scaler = StandardScaler()
    #X_SS = standard_scaler.fit_transform(X)
    
    # Se separan los datos: un % para el entrenamiento del modelo y otro
    # para el test
    x1, x2, y1, y2 = train_test_split(X, Y, test_size = 0.3)    

    mlp = MLPClassifier(activation='relu', hidden_layer_sizes=(50,50), max_iter=1000, tol=0.0001)
    
    mlp.fit(x1, y1)    
    

    print ("accuracy_score: ", mlp.score(x2, y2)*100.0)
    
    print ("\n")
    print("done in %0.16fs" % (time() - t0))

