import os
import numpy as np

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed Extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Load Model
MODEL_PATH = "DenseNet121_Pneumonia.keras"

model = load_model(MODEL_PATH)

IMG_SIZE = (224, 224)


# ==========================================
# Check File Extension
# ==========================================

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


# ==========================================
# Predict Function
# ==========================================

def predict_disease(img_path):

    img = image.load_img(img_path, target_size=IMG_SIZE)

    img = image.img_to_array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:

        disease = "PNEUMONIA"

        confidence = prediction * 100

    else:

        disease = "NORMAL"

        confidence = (1 - prediction) * 100

    return disease, round(confidence,2)


# ==========================================
# Home Page
# ==========================================

@app.route("/")

def home():

    return render_template("index.html")


# ==========================================
# Predict Route
# ==========================================

@app.route("/predict", methods=["POST"])

def predict():

    if "file" not in request.files:

        return render_template(
            "index.html",
            error="No File Selected"
        )

    file = request.files["file"]

    if file.filename == "":

        return render_template(
            "index.html",
            error="Please Upload an Image"
        )

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        disease, confidence = predict_disease(filepath)

        return render_template(
            "index.html",
            prediction=disease,
            confidence=confidence,
            image_path=filepath
        )

    return render_template(
        "index.html",
        error="Invalid Image Format"
    )


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
