from models.yolo_model import detect_rooftop_area
import matplotlib.pyplot as plt

image_path = "assets/sample_images/img_1.png"
mask, area = detect_rooftop_area(image_path)

if area > 0:
    print(f"✅ Detected rooftop area: {area:.0f} pixels")
    plt.imshow(mask, cmap='gray')
    plt.title("Predicted Rooftop Mask")
    plt.show()
else:
    print("❌ No rooftop detected.")
