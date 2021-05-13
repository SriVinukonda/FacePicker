from os import read
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import math


def process_image(csv_name,imagename):
    print(csv_name)
    x_min = 0 # X_17 round down
    x_max = 0 # X_21 round up
    y_min = 0 # X_19 round down
    y_max = 0 # X_29 round up
    i = 0
    with open(csv_name,newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ', quotechar='|')

        for row in reader:
            
            x_min = int((row["x_17,"]).split(".")[0])
            x_max = math.ceil(float(row["x_21,"].strip(",")))
            y_min = int(row["y_17,"].split(".")[0])
            y_max = math.ceil(float(row["y_29,"].strip(",")))
    assert type(imagename) == str

    #Read image and convert it to grayscale
    image = cv2.imread(imagename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    
    #                Y-, Y+ : X-, X+
    plt.imshow(image[y_min:y_max,x_min:x_max])
    plt.show()

    

path_to_samples = "../../OpenFace/samples/"
path_to_processed = "../../OpenFace/processed/"
process_image(path_to_processed+"sample4.csv",path_to_samples+"sample4.jpg")
