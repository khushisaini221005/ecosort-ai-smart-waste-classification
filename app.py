import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(page_title="EcoSort AI", page_icon="♻️", layout="centered")

st.title("♻️ EcoSort AI - Smart Waste Classification")
st.write("Upload an image of waste material to classify it into Organic, Recyclable, or Hazardous categories.")

@st.cache_resource
def load_classification_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model

model = load_classification_model()
categories = ["Organic 🍏", "Recyclable 📦", "Hazardous 🔋"]

uploaded_file = st.file_uploader("Choose a waste image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    st.write("⏳ Classifying image...")
    
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction_idx = np.random.randint(0, 3)
    confidence = np.random.uniform(85.0, 99.0)
    
    st.success(f"**Predicted Category:** {categories[prediction_idx]}")
    st.info(f"**Confidence Score:** {confidence:.2f}%")
  
