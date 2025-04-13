import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import os

def create_prediction_image(prediction_text):
    font_path = os.path.join(os.path.dirname(__file__), "Roboto-Regular.ttf")
    font = ImageFont.truetype(font_path, size=30)
    base = Image.open("aviator_logo.png").convert("RGBA")
    draw = ImageDraw.Draw(base)
    text_position = (50, base.height - 80)
    draw.text(text_position, prediction_text, font=font, fill="white")
    output_path = "prediction_result.png"
    base.save(output_path)
    return output_path

# Streamlit UI
st.set_page_config(page_title="Dự Đoán Aviator", layout="centered")

st.title("🛩️ Dự đoán Aviator")

if st.button("Dự đoán ngay"):
    prediction = round(random.uniform(1.00, 40.00), 2)
    prediction_text = f"Kết quả dự đoán: {prediction}x"
    img_path = create_prediction_image(prediction_text)
    st.image(img_path, caption=prediction_text)
