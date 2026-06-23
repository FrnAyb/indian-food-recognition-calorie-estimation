from flask import Flask, render_template, request, jsonify, url_for
import requests
from yolo.yolo import detect_objects
import base64
import os
import uuid
from pathlib import Path
#from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    result_image_path = None
    objects = None

    if 'file' in request.files and request.files['file'].filename != '':
        # Handle file upload
        file = request.files['file']

        image_path = f'static/uploads/{file.filename}'
        file.save(image_path)

        # Perform object detection
        result_image_path, objects = detect_objects(image_path)

    elif 'capturedImage' in request.form:
        # Handle captured image data from the hidden input field
        captured_image_data = request.form['capturedImage']

        # Save the captured image
        with open('static/uploads/captured_image.png', 'wb') as f:
            f.write(base64.b64decode(captured_image_data.split(',')[1]))

        # Perform object detection
        result_image_path, objects = detect_objects('static/uploads/captured_image.png')

    return render_template('index.html', result_image_path=result_image_path, objects = objects)
 
if __name__ == '__main__':
    app.run(debug=True)