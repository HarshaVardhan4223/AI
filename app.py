import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("skin_disease_model.h5")

# Define class labels (update this based on your dataset)
class_labels = ['Acne', 'Eczema', 'Melanoma', 'Psoriasis']  # Example classes

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to match model input size
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Expand dimensions for model
    return image

# Streamlit UI
st.title("🩺 Dermatologist AI - Skin Disease Detection")
st.write("Upload an image to detect skin disease.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process and predict
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = class_labels[np.argmax(prediction)]

    # Show the result
    st.success(f"Prediction: **{predicted_class}**")
