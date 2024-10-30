from flask import Flask, request, render_template, jsonify
import cv2
import pytesseract
import numpy as np
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        questions, answers = process_image(file_path)
        return jsonify({'questions': questions, 'answers': answers})

def process_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    processed_image = cv2.medianBlur(binary_image, 3)
    text = pytesseract.image_to_string(processed_image)
    
    questions = []
    answers = []
    lines = text.split('\n')
    for line in lines:
        if line.startswith('Q:'):
            questions.append(line[2:].strip())
        elif line.startswith('A:'):
            answers.append(line[2:].strip())
    
    return questions, answers

if __name__ == '__main__':
    app.run(debug=True
