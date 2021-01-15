# FIRST APPROACH TO YOLO (YOU ONLY LOOK ONCE) OBJECT DETECTION
# Santiago Garcia Arango
# MLH2021

# --------------------------------------------
# https://www.youtube.com/watch?v=1LCb1PVqzeY
# https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
# https://github.com/pjreddie/darknet
# --------------------------------------------


import cv2 as cv
import numpy as np
import os

# Get main current folder to avoid problems with absolute/relative paths
current_folder = os.path.abspath(os.path.dirname(__file__))


class ObjectDetector:
    """
    Object detector with OpenCV and YOLO-tiny deep neural network
    """
    def __init__(self, img, show_original):
        # Main path to load files
        self.config_path = os.path.join(current_folder, "yolov2-tiny.cfg")
        self.weights_path = os.path.join(current_folder, "yolov2-tiny.weights")
        self.names_path = os.path.join(current_folder, "coco.names")

        # Show original image
        self.img = img
        if show_original is True:
            self.show_img(self.img, "Original Image")

        # We will need it for the de-normalization after the processing
        self.height, self.width, _ = self.img.shape

        # Load deep neural network files
        self.load_files()

        # Apply blob processing with YOLO-tiny dnn
        self.blob_creation()

        # Apply dnn processing using blob as input
        self.apply_dnn_processing()

        # Show result image with dnn predictions marked
        self.show_final_output()

    def load_files(self):
        # Load pre-trained YOLO-tiny deep neural network
        self.net = cv.dnn.readNet(self.weights_path, self.config_path)

        # Load the classes vector for objects from pre-trained YOLO-tiny network
        self.classes = []
        with open(self.names_path, "r") as f:
            self.classes = f.read().splitlines()

    def show_img(self, img, img_name, destroy=False):
        # Show given image
        cv.imshow("{}".format(img_name), img)
        cv.waitKey(0)
        if destroy is True:
            cv.destroyAllWindows()

    def blob_creation(self, show_imgs=False):
        # Create a 4dimensional blob from image with given parameters...
        # ... see OpenCV documentation for deep neural networks functions
        self.blob = cv.dnn.blobFromImage(self.img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        # print(self.blob.shape)

        if show_imgs is True:
            for b in self.blob:
                for n, img_blob in enumerate(b):
                    self.show_img(img_blob, "{}".format(str(n)))

    def apply_dnn_processing(self):
        # Set the created blob as the main input for the dnn
        self.net.setInput(self.blob)

        # Function that uses OpenCV to get the output_layers from dnn
        output_layers = self.net.getUnconnectedOutLayersNames()

        # Apply a forward-pass to the dnn and get the output layers
        layer_outputs = self.net.forward(output_layers)

        # Create bounding boxes, classes_ids and confidences for the predictions
        self.boxes = []
        self.confidences = []
        self.classes_ids = []

        for output in layer_outputs:
            for detection in output:
                # Get values for the detection (scores) of predictions
                # ... (0, 1, 2, 3) are the rectangle positions (don't apply)
                scores = detection[5:]

                # Find maximun scores (confidence) and save it in confidence
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Apply treshold for confidences that are significant
                # ... remember to revert the normalization (scale again)
                if confidence > 0.5:
                    # Get main position of relevant squares
                    center_x = int(detection[0] * self.width)
                    center_y = int(detection[1] * self.height)
                    w = int(detection[2] * self.width)
                    h = int(detection[3] * self.height)

                    # Find specific locations of the square beggining
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Add relevant information to the predictions
                    self.boxes.append([x, y, w, h])
                    self.confidences.append(float(confidence))
                    self.classes_ids.append(class_id)

            # This step is to AVOID repeated items (check OpenCV docs)
            self.indexes = cv.dnn.NMSBoxes(self.boxes, self.confidences, 0.5, 0.4)
            if len(self.indexes) > 0:
                self.indexes = self.indexes.flatten()  # Reduce the indexes dimentions
                # print(self.indexes)

    def show_final_output(self, reduce_repeated=False):
        # Choose OpenCV parameters for the final output
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        colors = np.random.uniform(0, 255, size=(len(self.boxes), 3))
        # print(colors)
        # print(len(self.indexes))
        # print(len(self.boxes))

        if reduce_repeated is True:
            for i in self.indexes:
                x, y, w, h = self.boxes[i]
                label = str(self.classes[self.classes_ids[i]])
                confidence = str(round(self.confidences[i], 2))
                color = colors[i]

                cv.rectangle(self.img, (x, y), (x + w, y + h), color, 2)
                cv.putText(self.img, "{} : {}".format(label, confidence), (x - 2, y - 10), font, 1, color, 1)
        else:
            for i in range(len(self.boxes)):
                x, y, w, h = self.boxes[i]
                label = str(self.classes[self.classes_ids[i]])
                confidence = str(round(self.confidences[i], 2))
                color = colors[i]

                cv.rectangle(self.img, (x, y), (x + w, y + h), color, 2)
                cv.putText(self.img, "{}:{}".format(label, confidence), (x - 2, y - 10), font, 1, color, 1)

        cv.imshow("Final Image", self.img)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

if __name__ == "__main__":
    # ------------------- TESTS -------------------------
    # Load image and resize it to specific shape
    img_path = os.path.join(current_folder, "imgs", "img_01.jpg")
    img = cv.imread(img_path)
    img = cv.resize(img, (700, 500))
    detector = ObjectDetector(img, True)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Load image and resize it to specific shape
    img_path = os.path.join(current_folder, "imgs", "img_02.jpg")
    img = cv.imread(img_path)
    img = cv.resize(img, (700, 500))
    detector = ObjectDetector(img, True)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Load image and resize it to specific shape
    img_path = os.path.join(current_folder, "imgs", "img_03.jpg")
    img = cv.imread(img_path)
    img = cv.resize(img, (700, 500))
    detector = ObjectDetector(img, True)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Load image and resize it to specific shape
    img_path = os.path.join(current_folder, "imgs", "img_04.jpg")
    img = cv.imread(img_path)
    img = cv.resize(img, (700, 500))
    detector = ObjectDetector(img, True)
    cv.waitKey(0)
    cv.destroyAllWindows()
