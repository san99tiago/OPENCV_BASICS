# EXTRACT CHARACTERISTICS OF EACH NUMBER AND SAVE THEM IN XLSX FILE
# Santiago Garcia Arango

import cv2 as cv
import numpy as np
import xlsxwriter
import glob
import os


def get_imgs_folder_path(folder_name):
    # Get the path for the folder that contains the input and output images
    upper_dir = os.path.dirname(__file__)  # Upper dir
    img_folder_path = os.path.abspath(os.path.join(upper_dir, folder_name))
    return img_folder_path


def get_img_path(img_folder_path, img_name):
    # Get specific path to the images we will use inside the "imgs" folder
    img_path = os.path.join(img_folder_path, img_name)
    return img_path


def extract_characteristics(path):
    img = cv.imread(path, 0)
    imgColor = cv.imread(path, 1)
    img = cv.resize(img, (30, 60))
    imgColor = cv.resize(imgColor, (30, 60))
    ret, imgBin = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    cnt, hie = cv.findContours(imgBin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    check_correct_contour = 0
    for cont in cnt:
        x, y, w, h = cv.boundingRect(cont)
        
        if (cv.contourArea(cont) > 200):
            check_correct_contour = check_correct_contour + 1
            # Draw rectangle on top of img
            cv.rectangle(imgColor, (x,y), (x+w, y+h), (255, 0, 0), 2)

            # Show current img and contour for a few seconds
            cv.imshow("imgColor", imgColor)
            cv.waitKey(1)

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

            pixeles_h_2 = 0
            for h_i in range(h//2):
                for w_i in range(w):
                    if imgBin[h_i, w_i] == 255:
                        pixeles_h_2 = pixeles_h_2 + 1

            pixeles_w_2 = 0
            for h_i in range(h):
                for w_i in range(w//2):
                    if img[h_i, w_i] == 255:
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

def main():
    # Create vector to go through each "object" to classify
    vector_folders = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Create xlsx workbook to add info
    path_xlsx = os.path.join(os.path.dirname(__file__), "characteristics.xlsx")
    workbook = xlsxwriter.Workbook(path_xlsx)
    worksheet = workbook.add_worksheet("chars_1")

    row = 0
    col = 0
    i = 1

    # Get main path to the training img folders
    num_path = get_imgs_folder_path("num")
    print("\n\nPATH" , num_path)

    # Go to each img in every folder
    for j in range(0, len(vector_folders)):
        current_path = os.path.join(num_path, vector_folders[j])
        for path in glob.glob(current_path + "/*.png"):

            # Main function to extract all characteristics
            vector_characteristics = extract_characteristics(path)

            # Sometimes the characteristics can't be achieved... avoid error
            if vector_characteristics is not None:
                # Write characteristics in Excel document
                for charac in (vector_characteristics):
                    worksheet.write(row, col, vector_folders[j])
                    worksheet.write(row, i, charac)
                    i = i + 1
                i = 1
                row = row + 1

    workbook.close()




if __name__ == "__main__":
    main()
    cv.waitKey(0)
    cv.destroyAllWindows()
