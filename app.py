import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2

from models.yolo_model import detect_rooftop_area
from utils.area_calc import convert_pixels_to_m2
from utils.solar_calc import solar_estimation
from utils.prompts import generate_prompt
from utils.llm_agent import get_llm_response
st.set_page_config(page_title="☀️ Solar Rooftop Analyzer", layout="centered")
st.title("☀️ AI-Powered Solar Rooftop Analyzer")
st.markdown("""
Upload a satellite image of a rooftop to analyze its solar installation potential, calculate ROI, and get expert installation recommendations.
""")


st.sidebar.header(" Configuration")
tariff = st.sidebar.slider("Electricity Tariff (₹/kWh)", 4.0, 10.0, 7.0)
efficiency = st.sidebar.slider("Panel Efficiency", 0.10, 0.22, 0.18)
irradiance = st.sidebar.slider("Avg. Irradiance (kWh/m²/day)", 3.5, 6.5, 5.5)
scale = st.sidebar.slider("Pixel-to-m² Scale", 0.1, 1.0, 0.25)

# Image Upload Section
st.markdown("---")
st.subheader("📤 Upload a Rooftop Image")
st.caption("Accepts JPG, JPEG, PNG formats. Prefer high-resolution satellite views.")
uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"])

# Process uploaded image

if uploaded_image:
    img_path = "temp_image.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_image.read())

    st.image(img_path, caption="Uploaded Rooftop Image", use_container_width=True)

    st.markdown("---")
    st.subheader("🧠 Rooftop Detection & Analysis")

    # ✅ FIXED: call rooftop detector here, not LLM
    mask, pixel_area = detect_rooftop_area(img_path)


    if pixel_area > 0:
        area_m2 = convert_pixels_to_m2(pixel_area, scale)
        st.success(f" Detected Rooftop Area: **{area_m2:.2f} m²**")

        # Solar Output Estimation
        st.markdown("---")
        st.subheader("⚡ Solar Output & ROI Estimation")
        results = solar_estimation(area_m2, irradiance, efficiency, tariff)

        col1, col2, col3 = st.columns(3)
        col1.metric("System Size (kW)", f"{results['System Size (kW)']:.2f}")
        col2.metric("Annual Output (kWh)", f"{results['Energy Output (kWh/year)']:,}")
        col3.metric("Payback Period", f"{results['Payback Period (yrs)']} yrs")

        st.markdown("#### 💰 Financial Summary")
        st.write(f"- **System Cost:** ₹{results['System Cost (₹)']:,}")
        st.write(f"- **Annual Savings:** ₹{results['Annual Savings (₹)']:,}")

        # Mask display
        st.markdown("---")
        st.subheader(" Detected Rooftop Mask")
        fig, ax = plt.subplots()
        ax.imshow(mask, cmap='gray')
        ax.axis("off")
        st.pyplot(fig)

        # LLM Summary Generation
        st.markdown("---")
        st.subheader("📘 Expert Installation Summary")
        with st.spinner("Generating personalized solar recommendations..."):
            prompt = generate_prompt(
                area=area_m2,
                kwh=results["Energy Output (kWh/year)"],
                roi=results["Payback Period (yrs)"],
                location="Delhi"
            )
            try:
                summary = get_llm_response(prompt)
                st.markdown(summary)
            except Exception as e:
                st.error(" LLM response failed. Check your API key or internet connection.")
                st.exception(e)
    else:
        st.error(" No rooftop detected in the image. Please upload a clearer or different image.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ by [Satyam Tiwari](https://www.linkedin.com/in/your-link) for Wattmonk Technologies Internship Assessment.")