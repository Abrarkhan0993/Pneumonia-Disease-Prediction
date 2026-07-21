# 🫁 PneumoAI: Pneumonia Detection Using Deep Learning

An AI-powered web application that detects **Pneumonia** from **Chest X-ray images** using the **DenseNet121** deep learning model. The application is built with **TensorFlow/Keras** and deployed using **Flask**, providing a simple and user-friendly interface for image-based prediction.

---

## 📌 Project Overview

PneumoAI is a binary image classification system that analyzes chest X-ray images and predicts whether the patient is:

* ✅ **NORMAL**
* 🦠 **PNEUMONIA**

The project uses **Transfer Learning** with the pre-trained **DenseNet121** architecture to achieve high classification performance.

---

## ✨ Features

* 🩻 Chest X-ray image classification
* 🤖 Deep Learning model using DenseNet121
* 📤 Upload and analyze X-ray images
* 📊 Displays prediction with confidence score
* 🌐 Flask-based web application
* 📱 Responsive and modern user interface

---

## 🛠️ Tech Stack

| Category             | Technologies      |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Deep Learning        | TensorFlow, Keras |
| Model                | DenseNet121       |
| Backend              | Flask             |
| Frontend             | HTML5, CSS3       |
| Image Processing     | Pillow            |
| Data Handling        | NumPy             |

---

## 📂 Project Structure

```text
Pneumonia_Detection/
│
├── app.py
├── DenseNet121_Pneumonia.keras
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
├── templates/
│   └── index.html
│
└── dataset/
    ├── train/
    ├── val/
    └── test/
```

---

## 📊 Dataset

**Dataset:** Chest X-Ray Images (Pneumonia)

* **Classes:** NORMAL, PNEUMONIA
* **Image Size:** 224 × 224
* **Training Method:** Transfer Learning with DenseNet121

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Pneumonia_Detection.git
```

### Move to the project directory

```bash
cd Pneumonia_Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 Model Workflow

1. Upload Chest X-ray Image
2. Image Preprocessing (224 × 224)
3. DenseNet121 Model Prediction
4. Classification (NORMAL / PNEUMONIA)
5. Display Prediction with Confidence Score

---

## 📸 Application Preview

> Add screenshots of your application here after running it.

### Home Page

```
screenshots/home.png
```

### Prediction Result

```
screenshots/result.png
```

---

## 📈 Future Improvements

* Grad-CAM heatmap visualization
* Multi-class lung disease classification
* PDF medical report generation
* Cloud deployment (Render/AWS)
* User authentication
* Prediction history
* REST API integration

---

## 👨‍💻 Author

**Abrar Khan**

B.Tech – Artificial Intelligence & Data Science

---

## 📜 License

This project is licensed under the **MIT License**.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
