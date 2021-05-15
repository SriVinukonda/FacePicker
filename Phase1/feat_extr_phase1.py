from os import read
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import math


def process_image(csv_name,imagename):
    
    eye_left_x = 0 # X_17 round down
    eye_right_x = 0 # X_21 round up
    eye_top_y = 0 # X_19 round down
    eye_bot_y = 0 # X_29 round up

    nose_left_x = 0 # X_31 round down
    nose_right_x = 0 # X_21 round up
    nose_top_y = 0 # X_19 round down
    nose_bot_y = 0 # X_29 round up

    mouth_left_x = 0 # X_48 round down
    mouth_right_x = 0 # X_54 round up
    mouth_top_y = 0 # X_51 round down
    mouth_bot_y = 0 # X_57 round up

    feature_list = []


    i = 0
    with open(csv_name,newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')

        for row in reader:
            
            eye_left_x = int((row["x_17,"]).split(".")[0])
            eye_right_x = math.ceil(float(row["x_27,"].strip(",")))
            eye_top_y = (int(row["y_20,"].split(".")[0])+int(row["y_38,"].split(".")[0]))//2
            eye_bot_y = math.ceil(float(row["y_29,"].strip(",")))
            feature_list.append([eye_left_x,eye_right_x,eye_top_y,eye_bot_y])
            
            nose_left_x = int((row["x_20,"]).split(".")[0])
            nose_right_x = math.ceil(float(row["x_23,"].strip(",")))
            nose_top_y = int((row["y_38,"]).split(".")[0])
            nose_bot_y = math.ceil(float(row["y_33,"].strip(",")))
            feature_list.append([nose_left_x,nose_right_x,nose_top_y,nose_bot_y])
            
            mouth_left_x = int((row["x_48,"]).split(".")[0])
            mouth_right_x = math.ceil(float(row["x_54,"].strip(",")))
            mouth_top_y = (int((row["y_51,"]).split(".")[0])+int((row["y_33,"]).split(".")[0]))//2
            mouth_bot_y = math.ceil(float(row["y_57,"].strip(","))*0.75+float(row["y_8,"].strip(","))*0.25)
            feature_list.append([mouth_left_x,mouth_right_x,mouth_top_y,mouth_bot_y])

    assert type(imagename) == str

    # Read image and convert it to grayscale
    image = cv2.imread(imagename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 
    i = 1
    for each in feature_list:
        #                Y-, Y+ : X-, X+
        # plt.imshow(image[each[2]:each[3],each[0]:each[1]])
        cv2.imwrite("./feature{}.jpg".format(i),image[each[2]:each[3],each[0]:each[1]])
        i+=1
        # plt.show()
    

    

path_to_samples = "../../OpenFace/samples/"
path_to_processed = "../../OpenFace/processed/"
process_image(path_to_processed+"MySample.csv",path_to_samples+"MySample.jpg")
