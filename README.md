---
title: Solar Rooftop Analyzer
emoji: ☀️
colorFrom: yellow
colorTo: green
sdk: docker
pinned: false
---

# ☀️ AI-Powered Solar Rooftop Analyzer

This is a Streamlit-based web application that uses AI to detect rooftops from satellite images and estimate their solar potential, installation feasibility, and ROI — designed specifically for homeowners and solar professionals.

> 🔧 Built as part of the **Wattmonk Technologies Internship Assessment**

---

## 🚀 What It Does
- Detects rooftop areas using YOLOv8 segmentation model
- Estimates solar panel system size, cost, and annual savings
- Calculates ROI and payback period
- Generates expert-level installation recommendations using LLM

---

## 🌐 Live Demo (Hugging Face Spaces)
Try it live on [Hugging Face Spaces](https://huggingface.co/spaces/96satyam/solar-rooftop-analyzer) *(replace with your deployed URL)*

---

## 🧠 How It Works

### 1. 🛰️ Rooftop Detection (Vision AI)
We use [Ultralytics YOLOv8-nano segmentation](https://docs.ultralytics.com) model (`yolov8n-seg.pt`) to simulate rooftop detection.
- In early development, we use a **simulated mask** covering the central 70% of the image.
- This helps keep the model lightweight and testable without a large rooftop-labeled dataset.

> 🔄 Future upgrade: fine-tuned YOLOv8 for real rooftop segmentation.

### 2. ☀️ Solar System Estimation
Using the detected rooftop area:
- System size (kW)
- Annual generation (kWh)
- Cost, savings, and payback period

Implemented in `utils/solar_calc.py` with fully adjustable heuristics.

### 3. 🧠 LLM Integration for Expert Summary
We connect to an LLM to provide:
- Panel type & count
- Tilt/orientation
- Subsidy info
- Pro installation advice

#### LLM API Options:
- ✅ **OpenAI GPT-3.5** (preferred — full access with API key)
- ⚠️ **OpenRouter** (`deepseek-chat:free`) — supported, but free tier has strict limits

> OpenRouter integration is built-in to demonstrate flexibility, even though quota limits may restrict real-time usage.

---

## 🛠️ Setup Instructions
```bash
git clone https://github.com/96satyam/solar_ai_assistant.git
cd solar_ai_assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Download YOLO model weights:
```bash
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt -P models/
```

Add your API keys:
```env
OPENAI_API_KEY=sk-xxxxxx
# or
OPENROUTER_API_KEY=sk-or-xxxxxx
```

Run the app:
```bash
streamlit run app.py
```

---

## 🖼️ Example Output
| Component       | Sample Output              |
|----------------|----------------------------|
| Rooftop Area   | 55,216 m²                  |
| System Size    | 8,494.77 kW                |
| ROI            | 2.4 years                  |
| LLM Summary    | ✅ Monocrystalline panels <br> ✅ 27,600 panels <br> ✅ South-facing @ 28° tilt |

---

## 📁 Folder Structure
```
solar_ai_assistant/
├── app.py                  # Streamlit app
├── Dockerfile              # Docker config for Hugging Face deployment
├── models/                # YOLO weights + detection logic
├── utils/                 # Calculations and LLM prompts
├── assets/sample_images/  # Example input images
├── requirements.txt       # Dependencies
├── setup_instructions.md  # Local setup help
└── README.md              # You are here
```

---

## ☁️ Deployment on Hugging Face Spaces (Docker)
1. Create a new Space on Hugging Face (choose `Docker` SDK)
2. Upload all files including the `Dockerfile`
3. Set API keys in **Settings → Secrets**
   - `OPENAI_API_KEY` or `OPENROUTER_API_KEY`
4. Hugging Face builds & hosts your app at:
```
https://<username>-<space-name>.hf.space
```

---

## 🔮 Future Enhancements
- 🧠 Real rooftop detection with fine-tuned YOLOv8
- 🌦️ Real-time irradiance via Meteo/Google Solar API
- 📍 Auto-location & time-zone for regional estimates
- ⚙️ Expose API endpoint (FastAPI backend)

---

## 👨‍💻 Author
**Satyam Tiwari**  
AI & Data Science Final Year @ VIPS-TC  
🔗 [LinkedIn](https://www.linkedin.com/in/satyam9695/) · 📧 [Email](mailto:shivt843@gmail.com)

---
Built with ❤️ for the clean energy future.
