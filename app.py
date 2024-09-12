from flask import Flask, request, render_template, redirect, url_for
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = load_model('my_model.h5')

# Class labels for predictions
class_labels = ["normal", "pnemo", "tb"]

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def preprocess_image(img_path):
    """Preprocess the image to required size and format."""
    img = image.load_img(img_path, target_size=(512, 512))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file is submitted
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        # Save the file to the upload folder
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Preprocess the image and make predictions
            processed_image = preprocess_image(file_path)
            predictions = model.predict(processed_image)
            predicted_class_index = np.argmax(predictions)
            predicted_class_label = class_labels[predicted_class_index]

            # Render the result on a new page
            return render_template('result.html', label=predicted_class_label, image_url=file_path)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
