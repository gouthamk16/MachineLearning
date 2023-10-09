### Image Classifier using CIFAR-10 Dataset
This project is an image classifier that uses a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset. It loads a pre-trained model and can predict the class of a given image.

## Table of Contents
Overview
Prerequisites
Usage
Project Structure
License
Overview
The CIFAR-10 dataset is a collection of 60,000 32x32 color images in 10 different classes, with 6,000 images per class. This project utilizes TensorFlow and OpenCV to load the dataset, preprocess the images, and perform image classification. The pre-trained model used in this project has been trained on a subset of the CIFAR-10 dataset.

## Prerequisites
Before you can run the code, ensure you have the following dependencies installed:

Python 3.x
TensorFlow
OpenCV (cv2)
NumPy
Matplotlib
You can install these dependencies using pip:

bash
Copy code
pip install tensorflow opencv-python numpy matplotlib
Usage
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/image-classifier.git
Navigate to the project directory:

bash
Copy code
cd image-classifier
Run the image classifier:

bash
Copy code
python image_classifier.py
This will load a pre-trained model, display an example image, and make a prediction based on that image.

You can replace the example image (scaled_images/resized_plane.jpg) with your own images for classification.

## Project Structure
The project structure is as follows:

image_classifier.py: The main Python script that loads the CIFAR-10 dataset, pre-trained model, and performs image classification.
scaled_images/: Directory containing example images for testing the classifier.
image_classifier.model: Pre-trained CNN model for image classification.
README.md: This documentation file.
Feel free to modify the code and project structure to suit your needs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
