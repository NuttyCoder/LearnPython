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

# Build the CNN Model
model
model = Sequential([ 
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)), Conv2D(64, (3, 3), activation='relu'), 
    MaxPooling2D((2, 2)), 
    Conv2D(128, (3, 3), activation='relu'), 
    MaxPooling2D((2, 2)), 
    Flatten(), 
    Dense(128, activation='relu'), 
    Dense(2, activation='softmax') 
    # Assuming binary classification 
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

                                                 
