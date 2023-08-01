from flask import Flask, render_template, request, jsonify, json
import os
import cv2
import numpy as np
from keras.models import load_model
import imutils

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi'}

# Load the saved model
model = load_model("saved_model.h5")


# Function to calculate mean squared loss
def mean_squared_loss(x1, x2):
    difference = x1 - x2
    a, b, c, d, e = difference.shape
    n_samples = a * b * c * d * e
    sq_difference = difference**2
    Sum = sq_difference.sum()
    distance = np.sqrt(Sum)
    mean_distance = distance / n_samples
    return mean_distance



# Function to perform video analysis
def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    results = []

    while cap.isOpened():
        imagedump = []
        ret, frame = cap.read()

        if frame is None:
            break

        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        for i in range(10):
            ret, frame = cap.read()
            if frame is None:
                break

            image = imutils.resize(frame, width=700, height=600)
            frame = cv2.resize(frame, (227, 227), interpolation=cv2.INTER_AREA)
            gray = 0.2989 * frame[:, :, 0] + 0.5870 * frame[:, :, 1] + 0.1140 * frame[:, :, 2]
            gray = (gray - gray.mean()) / gray.std()
            gray = np.clip(gray, 0, 1)
            imagedump.append(gray)


        if frame is None:
            break

        imagedump = np.array(imagedump)
        imagedump.resize(227, 227, 10)
        imagedump = np.expand_dims(imagedump, axis=0)
        imagedump = np.expand_dims(imagedump, axis=4)
        output = model.predict(imagedump)
        loss = mean_squared_loss(imagedump, output)

        a = 'abnormal' if loss > 0.000735 else 'normal'

        results.append({'time': timestamp, 'results': a})

    cap.release()

    return results


# Check if the file has allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'video' not in request.files:
            return jsonify({'error': 'No video file found'})

        video = request.files['video']

        # Check if the file has allowed extension
        if not allowed_file(video.filename):
            return jsonify({'error': 'Invalid file format'})

        # Save the uploaded video to the uploads directory
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)

        # Perform video analysis
        result = analyze_video(video_path)

        # Convert the result list to a JSON-serializable format
        result_json = json.dumps(result)

        # Delete the uploaded video
        os.remove(video_path)
        return jsonify({'result': result_json})

    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
