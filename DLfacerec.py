import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os import tensorflow as tf from tensorflow.keras.models 
import Sequential from tensorflow.keras.layers  
import Conv2D, MaxPooling2D, Flatten, Dense from sklearn.model_selection 
import train_test_split 
import sys

#Function to load and preprocess image from a folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img = cv2.resize(img, (128, 128))  # Resize to 128x128
            img = img / 255.0  # Normalize pixel values
            images.append(img)
    return np.array(images)
# Load dataset
images = load_images_from_folder('path_to_dataset_folder')
labels = np.array([0] * len(images)) # Replace with the actual labels

# Split data into training and validation sets
X_train, X_val, y_train,y_val = train_test_split(images, labels, test_size:

