import os
import cv2
import glob
import numpy as np


def load_data_small():
    """
        This function loads images form the path: 'data/data_small' and return the training
        and testing dataset. The dataset is a list of tuples where the first element is the 
        numpy array of shape (m, n) representing the image the second element is its 
        classification (1 or 0).

        Parameters:
            None

        Returns:
            dataset: The first and second element represents the training and testing dataset respectively
    """

    # Begin your code (Part 1-1)
    #raise NotImplementedError("To be implemented")
    """
    line 29 : prepare data path
    line 30 ~ 31 : prepare two lists for train dataset and test dataset
    line 32 ~ 46 : use for loop to get the filename in each folder and read the image and append them to the
    dataset they belong to with their labels, and I let face image to be appended first
    """
    path = "data/data_small"
    train_dataset = []
    test_dataset = []
    for filename in os.listdir(f"{path}/train/face"):
        image = cv2.imread(os.path.join(f"{path}/train/face/{filename}"), cv2.IMREAD_GRAYSCALE)
        train_dataset.append((image, 1))

    for filename in os.listdir(f"{path}/train/non-face"):
        image = cv2.imread(os.path.join(f"{path}/train/non-face/{filename}"), cv2.IMREAD_GRAYSCALE)
        train_dataset.append((image, 0))

    for filename in os.listdir(f"{path}/test/face"):
        image = cv2.imread(os.path.join(f"{path}/test/face/{filename}"), cv2.IMREAD_GRAYSCALE)
        test_dataset.append((image, 1))

    for filename in os.listdir(f"{path}/test/non-face"):
        image = cv2.imread(os.path.join(f"{path}/test/non-face/{filename}"), cv2.IMREAD_GRAYSCALE)
        test_dataset.append((image, 0))

    # End your code (Part 1-1)
    
    return train_dataset, test_dataset


def load_data_FDDB(data_idx="01"):
    """
        This function generates the training and testing dataset  form the path: 'data/data_small'.
        The dataset is a list of tuples where the first element is the numpy array of shape (m, n)
        representing the image the second element is its classification (1 or 0).
        
        In the following, there are 4 main steps:
        1. Read the .txt file
        2. Crop the faces using the ground truth label in the .txt file
        3. Random crop the non-faces region
        4. Split the dataset into training dataset and testing dataset
        
        Parameters:
            data_idx: the data index string of the .txt file

        Returns:
            train_dataset: the training dataset
            test_dataset: the testing dataset
    """

    with open("data/data_FDDB/FDDB-folds/FDDB-fold-{}-ellipseList.txt".format(data_idx)) as file:
        line_list = [line.rstrip() for line in file]

    # Set random seed for reproducing same image croping results
    np.random.seed(0)

    face_dataset, nonface_dataset = [], []
    line_idx = 0

    # Iterate through the .txt file
    # The detail .txt file structure can be seen in the README at https://vis-www.cs.umass.edu/fddb/
    while line_idx < len(line_list):
        img_gray = cv2.imread(os.path.join("data/data_FDDB", line_list[line_idx] + ".jpg"), cv2.IMREAD_GRAYSCALE)
        num_faces = int(line_list[line_idx + 1])

        # Crop face region using the ground truth label
        face_box_list = []
        for i in range(num_faces):
            # Here, each face is denoted by:
            # <major_axis_radius minor_axis_radius angle center_x center_y 1>.
            coord = [int(float(j)) for j in line_list[line_idx + 2 + i].split()]
            x, y = coord[3] - coord[1], coord[4] - coord[0]            
            w, h = 2 * coord[1], 2 * coord[0]

            left_top = (max(x, 0), max(y, 0))
            right_bottom = (min(x + w, img_gray.shape[1]), min(y + h, img_gray.shape[0]))
            face_box_list.append([left_top, right_bottom])
            # cv2.rectangle(img_gray, left_top, right_bottom, (0, 255, 0), 2)

            img_crop = img_gray[left_top[1]:right_bottom[1], left_top[0]:right_bottom[0]].copy()
            face_dataset.append((cv2.resize(img_crop, (19, 19)), 1))

        line_idx += num_faces + 2

        # Random crop N non-face region
        # Here we set N equal to the number of faces to generate a balanced dataset
        # Note that we have alreadly save the bounding box of faces into `face_box_list`, you can utilize it for non-face region cropping
        for i in range(num_faces):
            # Begin your code (Part 1-2)
            #raise NotImplementedError("To be implemented")
            """
            line 120 : pick the current face bounding box
            line 122 ~ 125 : define non-face bounding box with small intersection with face box by moving the face box
            with some random offset in x and y, and get the non-face box's left top and right bottom
            line 127 ~ 128 : ensure non-face bounding box is within image bounds
            line 130 : crop non-face region
            """
            face_box = face_box_list[i]
    
            x_offset = np.random.randint(-15, 15)
            y_offset = np.random.randint(-15, 15)
            left_top_nonface = (face_box[0][0] + x_offset, face_box[0][1] + y_offset)
            right_bottom_nonface = (face_box[1][0] + x_offset, face_box[1][1] + y_offset)

            left_top_nonface = (max(left_top_nonface[0], 0), max(left_top_nonface[1], 0))
            right_bottom_nonface = (min(right_bottom_nonface[0], img_gray.shape[1]), min(right_bottom_nonface[1], img_gray.shape[0]))

            img_crop = img_gray[left_top_nonface[1]:right_bottom_nonface[1], left_top_nonface[0]:right_bottom_nonface[0]].copy()

            # End your code (Part 1-2)

            nonface_dataset.append((cv2.resize(img_crop, (19, 19)), 0))

        # cv2.imshow("windows", img_gray)
        # cv2.waitKey(0)

    # train test split
    num_face_data, num_nonface_data = len(face_dataset), len(nonface_dataset)
    SPLIT_RATIO = 0.7

    train_dataset = face_dataset[:int(SPLIT_RATIO * num_face_data)] + nonface_dataset[:int(SPLIT_RATIO * num_nonface_data)]
    test_dataset = face_dataset[int(SPLIT_RATIO * num_face_data):] + nonface_dataset[int(SPLIT_RATIO * num_nonface_data):]

    return train_dataset, test_dataset


def create_dataset(data_type):
    if data_type == "small":
        return load_data_small()
    else:
        return load_data_FDDB()
