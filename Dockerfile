# Use the official Python 3.9 slim image
FROM python:3.9-slim

# Set environment variables to prevent .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Install system dependencies for OpenCV and Streamlit
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev \
    wget git && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Download YOLOv8 model weights (place it inside /models)
RUN mkdir -p models && \
    wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt -P models/

# Expose Streamlit default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
