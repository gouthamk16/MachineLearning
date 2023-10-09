<!DOCTYPE html>
<html>
<head>
    <title>Image Classifier using CIFAR-10 Dataset</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
        }

        h1 {
            font-size: 28px;
        }

        h2 {
            font-size: 24px;
        }

        h3 {
            font-size: 20px;
        }

        ul {
            list-style-type: disc;
            padding-left: 20px;
        }

        code {
            background-color: #f4f4f4;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: monospace;
        }

        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: monospace;
            overflow-x: auto;
        }

        .code-block {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Image Classifier using CIFAR-10 Dataset</h1>
    
    <p>This project is an image classifier that uses a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset. It loads a pre-trained model and can predict the class of a given image.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>The CIFAR-10 dataset is a collection of 60,000 32x32 color images in 10 different classes, with 6,000 images per class. This project utilizes TensorFlow and OpenCV to load the dataset, preprocess the images, and perform image classification. The pre-trained model used in this project has been trained on a subset of the CIFAR-10 dataset.</p>

    <h2 id="prerequisites">Prerequisites</h2>
    <p>Before you can run the code, ensure you have the following dependencies installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>TensorFlow</li>
        <li>OpenCV (cv2)</li>
        <li>NumPy</li>
        <li>Matplotlib</li>
    </ul>

    <p>You can install these dependencies using pip:</p>
    <pre><code>pip install tensorflow opencv-python numpy matplotlib</code></pre>

    <h2 id="usage">Usage</h2>
    <p>Clone this repository to your local machine:</p>
    <pre><code>git clone https://github.com/your-username/image-classifier.git</code></pre>

    <p>Navigate to the project directory:</p>
    <pre><code>cd image-classifier</code></pre>

    <p>Run the image classifier:</p>
    <pre><code>python image_classifier.py</code></pre>

    <p>This will load a pre-trained model, display an example image, and make a prediction based on that image.</p>

    <p>You can replace the example image (scaled_images/resized_plane.jpg) with your own images for classification.</p>

    <h2 id="project-structure">Project Structure</h2>
    <p>The project structure is as follows:</p>
    <ul>
        <li>image_classifier.py: The main Python script that loads the CIFAR-10 dataset, pre-trained model, and performs image classification.</li>
        <li>scaled_images/: Directory containing example images for testing the classifier.</li>
        <li>image_classifier.model: Pre-trained CNN model for image classification.</li>
        <li>README.md: This documentation file.</li>
    </ul>

    <p>Feel free to modify the code and project structure to suit your needs.</p>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
