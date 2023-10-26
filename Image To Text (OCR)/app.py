from flask import Flask, render_template, request, jsonify
import pytesseract
from PIL import Image
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    myconfig = r"--psm 6 --oem 3"
    
    if 'image' in request.files:
        image = request.files['image']
        img = Image.open(image)
        text = pytesseract.image_to_string(img, config=myconfig)
        return jsonify({'text': text})
    else:
        return jsonify({'text': ''})

if __name__ == '__main__':
    app.run(debug=True)
