# Import necessary libraries
import cv2 as cv              # OpenCV for image processing
import numpy as np            # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for plotting
from tensorflow.keras import datasets, layers, models  # TensorFlow for deep learning

# Load the CIFAR-10 dataset, which contains images and labels for 10 different classes
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

# Normalize pixel values of the images to be in the range [0, 1]
training_images, testing_images = training_images / 255, testing_images / 255

# Define class names for CIFAR-10 dataset
class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# Plot the first 16 training images with their corresponding labels
for i in range(16):
    plt.subplot(4, 4, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i][0]])

plt.show()

# Reduce the size of the training and testing datasets to save resources and train faster
training_images = training_images[:20000]
training_labels = training_labels[:20000]
testing_images = testing_images[:4000]
testing_labels = testing_labels[:4000]

# Load a pre-trained image classification model
model = models.load_model('image_classifier.model')

# Read and preprocess an image to be classified
img = cv.imread('scaled_images/resized_plane.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Display the image
plt.imshow(img, cmap=plt.cm.binary)

# Make a prediction using the pre-trained model
prediction = model.predict(np.array([img])/255)
index = np.argmax(prediction)

# Print the predicted class name
print(f'Prediction is {class_names[index]}')
