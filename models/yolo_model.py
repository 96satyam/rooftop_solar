from ultralytics import YOLO
import cv2
import numpy as np

# Using the nano version (yolov8n-seg) for quick inference during development
model = YOLO("yolov8n-seg.pt")

def detect_rooftop_area(image_path):
    """
    Detects rooftop area from a satellite image using a simulated mask.

    Parameters:
        image_path (str): Path to the input satellite image.

    Returns:
        mask (np.ndarray): Simulated binary mask of the rooftop area.
        pixel_area (float): Number of pixels detected as rooftop.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")

    height, width, _ = image.shape

    # Simulate rooftop detection: Mask central 70% area as rooftop for testing
    simulated_mask = np.zeros((height, width), dtype=np.uint8)
    start_y, end_y = int(height * 0.15), int(height * 0.85)
    start_x, end_x = int(width * 0.15), int(width * 0.85)
    simulated_mask[start_y:end_y, start_x:end_x] = 1

    pixel_area = np.sum(simulated_mask)

    return simulated_mask, pixel_area
