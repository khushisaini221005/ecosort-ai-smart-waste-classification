# ♻️ EcoSort AI - Smart Waste Classification System

An AI-powered Deep Learning web application designed to automatically classify waste items into categories (e.g., Organic, Recyclable, Hazardous) using **Transfer Learning (MobileNetV2)** and **Streamlit**.

---

## ✨ Features
* 🧠 **Deep Learning Model:** Powered by MobileNetV2 for fast and accurate image classification.
* 📸 **Real-Time Upload:** Upload waste images to instantly view classification results and confidence scores.
* ⚡ **Interactive UI:** Simple, mobile-responsive web interface built with Streamlit.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Deep Learning:** TensorFlow / Keras, NumPy, Pillow
* **Web Framework:** Streamlit

---

## 🚀 How to Run Locally

1. **Clone the Repository:**
   ```bash
git clone https://github.com/khushisaini221005/ecosort-ai-smart-waste-classification.git
```
 ```bash
 cd ecosort-ai-smart-waste-classification
   ```
 2. **Install Dependencies:**

   ```bash
pip install -r requirements.txt
```
3. **Train Model:**
```bash

python train_model.py
```
4. **Run Streamlit App:**
```bash

streamlit run app.py
```
---
## 📁 Repository Structure
```text


ecosort-ai-smart-waste-classification/
│-- app.py                # Streamlit Web Interface
│-- train_model.py        # DL Model Training Script
│-- requirements.txt     # Project Dependencies
│-- README.md            # Project Documentation
```
