from ultralytics import YOLO
import cv2
import numpy as np

# Load model once (on import)
model = YOLO("yolov8n-seg.pt")  # You can swap to 'yolov8m-seg.pt' later for more accuracy

def detect_rooftop_area(image_path):
    
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Simulate detection: mask 70% of the image
    simulated_mask = np.zeros((height, width))
    simulated_mask[int(height*0.15):int(height*0.85), int(width*0.15):int(width*0.85)] = 1

    pixel_area = np.sum(simulated_mask)
    return simulated_mask, pixel_area

