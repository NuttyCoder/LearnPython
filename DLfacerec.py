import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img = cv2.resize(img, (128, 128))  # Resize to 128x128
            img = img / 255.0  # Normalize pixel values
            images.append(img)
    return np.array(images)

images = load_images_from_folder('path_to_dataset_folder')
