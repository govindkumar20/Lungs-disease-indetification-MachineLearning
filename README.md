# Lungs Disease Detector

An advanced Machine Learning model designed to classify lung diseases from X-ray scans using Convolutional Neural Networks (CNN) and Autoencoders. This project aims to accurately identify conditions such as pneumonia, tuberculosis (TB), COVID-19, and healthy individuals from X-ray images.

## Overview

This project leverages deep learning techniques to analyze X-ray scans for detecting various lung diseases. With a model built using CNNs and Autoencoders, it achieves an impressive 90% accuracy in classifying lung conditions. The model is deployed using Flask for easy integration with web applications and APIs, providing a user-friendly interface for real-time predictions.

## Features

- **High Accuracy**: Achieves 90% accuracy in detecting and classifying lung diseases.
- **Disease Categories**: Classifies X-ray images into categories such as:
  - Pneumonia
  - Tuberculosis (TB)
  - COVID-19
  - Healthy
- **Real-Time Predictions**: Provides real-time disease detection from X-ray scans.
- **Web Interface**: A simple web-based interface built with Flask for easy accessibility.

## Model Architecture

- **Convolutional Neural Networks (CNNs)**: Utilized for feature extraction and image classification.
- **Autoencoders**: Implemented for noise reduction and feature enhancement.
- **Training**: The model was trained on a comprehensive dataset of labeled X-ray images.
- **Evaluation**: Evaluated on test datasets to ensure high accuracy and robustness.

## Dataset

The dataset used for training includes X-ray images categorized into the specified disease conditions. It consists of thousands of labeled X-ray scans for effective model training and evaluation.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/govindkumar20/Lungs-disease-indetification-MachineLearning.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd Lungs-disease-indetification-MachineLearning
    ```

3. **Run the Flask application**:
    ```bash
    python app.py
    ```

4. **Access the web interface**:
    Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- **Upload an X-ray scan**: Use the web interface to upload an X-ray image of the lungs.
- **Receive Diagnosis**: The model analyzes the X-ray and classifies it into one of the disease categories or as healthy.
- **View Results**: The diagnosis, along with confidence levels, will be displayed on the web interface.

## Model Training

The model was trained on Google Colab using the following steps:

1. **Data Preprocessing**: X-ray images were resized, normalized, and augmented to enhance training.
2. **Model Construction**: A CNN architecture was built with additional Autoencoder layers for noise reduction.
3. **Training**: The model was trained using a labeled dataset, with extensive validation to prevent overfitting.
4. **Evaluation**: Performance was evaluated using test datasets, achieving an accuracy of 90%.

## Deployment

The trained model is deployed using Flask, allowing for easy integration with web-based applications and REST APIs. The application is accessible through a user-friendly web interface that accepts X-ray scans and returns predictions in real-time.

## Contributing

Contributions are welcome! If you would like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a Pull Request.


## Contact

For any questions or feedback, feel free to reach out to me at govindp231@gmail.com.

---

