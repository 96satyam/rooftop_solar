from models.yolo_model import detect_rooftop_area
from utils.area_calc import convert_pixels_to_m2
from utils.solar_calc import solar_estimation
import matplotlib.pyplot as plt

image_path = "assets/sample_images/img_1.png"

# Step 1: Detection
mask, pixels = detect_rooftop_area(image_path)
if pixels > 0:
    area_m2 = convert_pixels_to_m2(pixels)
    print(f"✅ Rooftop Area: {area_m2:.2f} m²")

    # Step 2: Solar Estimation
    results = solar_estimation(area_m2)
    print("⚡ Solar Output & ROI Estimation:")
    for k, v in results.items():
        print(f" - {k}: {v}")

    # Optional: show mask
    plt.imshow(mask, cmap='gray')
    plt.title("Rooftop Mask")
    plt.show()
else:
    print("❌ No rooftop detected.")
