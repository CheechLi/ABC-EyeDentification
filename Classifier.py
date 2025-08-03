# app.py
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd
import os
from datetime import datetime

# -------------------------------
# SETUP
# -------------------------------
st.set_page_config(
    page_title="Ocular Disease Classifier",
    page_icon="🧿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -------------------------------
# UI HEADER & SIDEBAR
# -------------------------------
st.markdown("<h1 style='text-align: center;'>ABC Eye-Dentification</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Ocular Disease Classifier</h2>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("### Instructions:")

st.markdown("Select a model from the dropdown below, then upload an eye image to get predictions on its condition. Your eye will be classified into one of the following categories:"
    "\n- Cataract\n- Diabetic Retinopathy\n- Glaucoma\n- Normal")

# -------------------------------
# MODEL SELECTION + LOADING
# -------------------------------
model_choices = {
    "DenseNet201":"DenseNet201.keras",
    "InceptionV3": "InceptionV3.keras",
}

st.markdown("### Choose a Model")
selected_model_name = st.selectbox("Select the deep learning model you'd like to use:", list(model_choices.keys()))
model_file = model_choices[selected_model_name]

@st.cache_resource(show_spinner="Loading selected model...")
def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path, compile=False)
        return model
    except Exception as e:
        st.error(f"Model load failed: {e}")
        return None

model_path = os.path.join("models", model_file)
model = load_model(model_path)
if model is None:
    st.stop()


# -------------------------------
# CATEGORY LABELS
# -------------------------------
categories = {
    0: "Cataract",
    1: "Diabetic Retinopathy",
    2: "Glaucoma",
    3: "Normal",
}


# -------------------------------
# IMAGE UPLOAD & PREDICTION
# -------------------------------
uploaded_file = st.file_uploader("Choose an eye image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load and show image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Save image with timestamped filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    image_name = f"{timestamp}_{uploaded_file.name}"
    os.makedirs("feedback_images", exist_ok=True)
    image_path = os.path.join("feedback_images", image_name)
    image.save(image_path)

    img = image.resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    try:
        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction))
        confidence = float(prediction[0][predicted_class])

        st.markdown("---")
        st.subheader("Model Prediction")
        st.success(f"**{categories[predicted_class]}** ({confidence * 100:.2f}% confidence)")

        st.markdown("### Class Probabilities")
        for i, prob in enumerate(prediction[0]):
            st.write(f"{categories[i]} — {prob * 100:.2f}%")
            st.progress(float(prob))

        # -------------------------------
        # FEEDBACK SECTION
        # -------------------------------
        st.markdown("## Was this prediction helpful?")
        feedback = st.radio("How accurate was the prediction?", ["Correct", "Incorrect", "Not sure"])
        comment = st.text_area("Optional comment or suggestion:")

        if st.button("Submit Feedback"):
            entry = {
                "timestamp": datetime.now().isoformat(),
                "image_name": image_name,
                "prediction": categories[predicted_class],
                "confidence": confidence,
                "feedback": feedback,
                "comment": comment
            }

            file_path = "user_feedback.csv"
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
            else:
                df = pd.DataFrame(columns=entry.keys())

            df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
            df.to_csv(file_path, index=False)

            st.success("Thank you for your feedback! Image and data saved.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")