import os
from unittest import result
import cv2
import utils
import numpy as np
import matplotlib.pyplot as plt


def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:A
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    #raise NotImplementedError("To be implemented")
    """
    line 31 ~ 33 : prepare data structure to store filename, current file, and box region
    line 34 ~ 45 : read the txt and store the filename and their box region
    line 47 ~ 49 : for each filename, read the image in RGB and grayscale, RGB image is to show while gray image is to get the box
    line 51 ~ 58 : for each box region, crop the region on the gray image and resize into 19 x 19, and check whether it's face or 
    non-face by classifier, and use rectangle to show the box in red or green on the RGB image
    line 60 ~ 61 : show the result and wait
    """
    filename = []
    current_file = ""
    rectangleRegion = dict()
    with open(dataPath) as file:
        for lines in file:
            line = lines.split(' ')
            if len(line) == 2:
                current_file = line[0]
                filename.append(current_file)
                rectangleRegion[current_file] = []
            else:
                new_region = []
                for x in line:
                    new_region.append(int(x))
                rectangleRegion[current_file].append(new_region)

    for file in filename:
        image = cv2.imread(os.path.join(f"data/detect/{file}"), cv2.IMREAD_UNCHANGED)
        original_image = cv2.imread(os.path.join(f"data/detect/{file}"), cv2.IMREAD_GRAYSCALE)

        for region in rectangleRegion[file]:
            x, y, w, h = region
            face = original_image[y : y + h, x : x + w]
            face = cv2.resize(face, (19, 19), interpolation = cv2.INTER_CUBIC)
            if clf.classify(face) == 1:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("windows", image)
        cv2.waitKey(0)

    # End your code (Part 4)
