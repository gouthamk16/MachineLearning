Image Classification using Artificial Neural Networks (ANN)
===========================================================

This repository contains code for a project on image classification using Artificial Neural Networks (ANN). The code uses the CIFAR-10 dataset to train and test an image classification model. Additionally, it demonstrates how to make predictions on new images using a pre-trained model.

Getting Started
---------------

Follow the instructions below to set up the project on your local machine.

### Prerequisites

Make sure you have the following libraries installed on your system:

-   [OpenCV](https://pypi.org/project/opencv-python/)
-   [NumPy](https://numpy.org/)
-   [Matplotlib](https://matplotlib.org/)
-   [TensorFlow](https://www.tensorflow.org/)

You can install them using `pip`:

`pip install opencv-python numpy matplotlib tensorflow`

### Installation

1.  Clone this repository to your local machine:

`git clone https://github.com/your-username/image-classification-ann.git`

1.  Navigate to the project directory:

`cd image-classification-ann`

1.  Run the provided code by executing the `image_classification.py` file:

`python image_classification.py`

Project Overview
----------------

The code in `image_classification.py` does the following:

1.  Imports the necessary libraries for image processing and deep learning.

2.  Loads the CIFAR-10 dataset, which consists of images and labels for 10 different classes.

3.  Normalizes pixel values of the images to be in the range [0, 1].

4.  Defines class names for the CIFAR-10 dataset.

5.  Plots the first 16 training images with their corresponding labels.

6.  Reduces the size of the training and testing datasets for faster training (optional).

7.  Loads a pre-trained image classification model (you should provide your own model file).

8.  Reads and preprocesses an image to be classified (you should provide your own image file).

9.  Displays the preprocessed image.

10. Makes a prediction using the pre-trained model and prints the predicted class name.

Customization
-------------

You can customize this code by:

-   Replacing the pre-trained model file (`image_classifier.model`) with your own trained model for specific tasks.

-   Replacing the image file (`scaled_images/resized_plane.jpg`) with the image you want to classify.

-   Modifying the code to use different datasets or adjust hyperparameters for training.

License
-------

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

Acknowledgments
---------------

-   This code is based on the CIFAR-10 dataset and uses TensorFlow for deep learning.

-   The project structure and readme template are inspired by best practices for creating GitHub repositories.

Feel free to contribute, report issues, or provide feedback to improve this project. Happy image classification!
