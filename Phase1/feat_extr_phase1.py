from os import read
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import math


def process_image(csv_name,imagename):
    print(csv_name)
    eye_left_x = 0 # X_17 round down
    eye_right_x = 0 # X_21 round up
    eye_top_y = 0 # X_19 round down
    eye_bot_y = 0 # X_29 round up

    nose_left_x = 0 # X_31 round down
    nose_right_x = 0 # X_21 round up
    nose_top_y = 0 # X_19 round down
    nose_bot_y = 0 # X_29 round up



    i = 0
    with open(csv_name,newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')

        for row in reader:
            
            eye_left_x = int((row["x_17,"]).split(".")[0])
            eye_right_x = math.ceil(float(row["x_27,"].strip(",")))
            eye_top_y = int(row["y_21,"].split(".")[0])
            eye_bot_y = math.ceil(float(row["y_29,"].strip(",")))

            nose_left_x = int((row["x_39,"]).split(".")[0])
            nose_right_x = math.ceil(float(row["x_35,"].strip(",")))
            nose_top_y = int((row["y_38,"]).split(".")[0])
            nose_bot_y = math.ceil(float(row["y_51,"].strip(",")))
    assert type(imagename) == str
    print(nose_top_y,nose_bot_y,nose_left_x,nose_right_x)
    print(eye_top_y,eye_bot_y,eye_left_x,eye_right_x)
    #Read image and convert it to grayscale
    image = cv2.imread(imagename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    
    #                Y-, Y+ : X-, X+
    plt.imshow(image[eye_top_y:eye_bot_y,eye_left_x:eye_right_x])
    plt.show()
    plt.imshow(image[nose_top_y:nose_bot_y,nose_left_x:nose_right_x])
    plt.show()

    

path_to_samples = "../../OpenFace/samples/"
path_to_processed = "../../OpenFace/processed/"
process_image(path_to_processed+"sample1.csv",path_to_samples+"sample1.jpg")
