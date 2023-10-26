# Image to Text Web App by Goutham

**Image to Text** is a web application that allows users to upload images and convert them into text using Optical Character Recognition (OCR). The converted text can be copied for further use.

## Features

- Image upload from your local drive.
- Image paste functionality.
- Real-time conversion of images to text using Tesseract OCR.
- Output text can be copied with the click of a button.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/gk-image-to-text.git `

   ```

1. Install the required Python packages:

   ```bash

   `pip install -r requirements.txt`

   ```

1. Run the Flask web app:

   ```bash

   `python app.py`
   ```

The web app will be accessible at [http://localhost:5000](http://localhost:5000/).

## Usage

1.  Access the web app through your browser.
2.  Upload an image by clicking the "Upload and Convert" button.
3.  Alternatively, paste an image directly.
4.  The converted text will be displayed in a non-resizable output container.
5.  Click the "Copy Text" button to copy the text to your clipboard.

## Technologies Used

- Python
- Flask (for the backend)
- HTML/CSS/JavaScript (for the frontend)
- Tesseract OCR
- OpenCV

## Contributing

We welcome contributions from the community. Feel free to open issues and pull requests if you have any suggestions or improvements.

## Acknowledgments

Special thanks to the developers of the following libraries and tools that were used in this project:

- [Flask](https://flask.palletsprojects.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
