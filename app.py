# app.py

import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2

from models.yolo_model import detect_rooftop_area
from utils.area_calc import convert_pixels_to_m2
from utils.solar_calc import solar_estimation

# Page settings
st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")
st.title("☀️ AI-Powered Solar Rooftop Analyzer")

st.markdown("Upload a satellite image of a rooftop to analyze its solar potential and ROI.")

# Sidebar inputs
st.sidebar.header("Configuration")
tariff = st.sidebar.slider("Electricity Tariff (₹/kWh)", 4.0, 10.0, 7.0)
efficiency = st.sidebar.slider("Panel Efficiency", 0.10, 0.22, 0.18)
irradiance = st.sidebar.slider("Avg. Irradiance (kWh/m²/day)", 3.5, 6.5, 5.5)
scale = st.sidebar.slider("Pixel-to-m² Scale", 0.1, 1.0, 0.25)

# Image upload
uploaded_image = st.file_uploader("Upload a rooftop image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    img_path = os.path.join("temp_image.jpg")
    with open(img_path, "wb") as f:
        f.write(uploaded_image.read())

    st.image(img_path, caption="Uploaded Image", use_container_width=True)


    # Detection
    mask, pixel_area = detect_rooftop_area(img_path)

    if pixel_area > 0:
        area_m2 = convert_pixels_to_m2(pixel_area, scale)
        st.success(f"Detected Rooftop Area: {area_m2:.2f} m²")

        # Estimation
        results = solar_estimation(area_m2, irradiance, efficiency, tariff)

        st.subheader("⚡ Solar System Estimation")
        for key, value in results.items():
            st.write(f"**{key}:** {value}")

        # Show mask
        st.subheader("🖼️ Detected Rooftop Mask")
        fig, ax = plt.subplots()
        ax.imshow(mask, cmap='gray')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.error("❌ No rooftop detected in the image. Try a different one.")
