import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def process_image(imagename):
    assert type(imagename) == str

    #Read image and convert it to grayscale
    image = cv2.imread(imagename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    

    plt.imshow(image[193:279,218:332])
    plt.show()

    


process_image("../../OpenFace/")
