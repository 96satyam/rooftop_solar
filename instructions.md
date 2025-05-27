#  Setup Instructions

These instructions will guide you through setting up and running the Solar Rooftop Analyzer locally on your machine.

---

##  Project Structure

```
solar_ai_assistant/
├── app.py                       # Streamlit web app
├── models/
│   └── yolo_model.py            # Rooftop detection logic using YOLOv8
├── utils/
│   ├── area_calc.py             # Pixel-to-m² conversion
│   ├── solar_calc.py            # Solar system and ROI calculations
│   ├── prompts.py               # Prompt builder for LLM
│   └── llm_agent.py             # LLM response logic (OpenAI/OpenRouter)
├── assets/
│   └── sample_images/           # Test rooftop images
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
└── setup_instructions.md       # You are here
```

---

## ⚙️ Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/96satyam/solar_ai_assistant.git
cd rooftop_solar
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Unix or MacOS
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download YOLOv8 Weights
This app uses the [YOLOv8 segmentation model](https://docs.ultralytics.com). Download weights:
```bash

# Download the segmentation weights
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt -P models/
```
Or place the file manually at `models/yolov8n-seg.pt`.

---

##  API Key Setup

### 1. Create a `.env` file
```bash
touch .env
```
Add your OpenAI or OpenRouter key:
```env
OPENAI_API_KEY=sk-xxxxx
# or
OPENROUTER_API_KEY=sk-or-xxxxx
```


##  Run the App
```bash
streamlit run app.py
```
The app will be available at:
- Local: `http://localhost:8501`
- Network: `http://<your-ip>:8501`

---

##  Test Example
Use the images in `assets/sample_images/` to test rooftop detection, estimation, and LLM summary generation.

---

##  Troubleshooting

| Issue | Fix |
|-------|------|
| No rooftop detected | Try clearer satellite image, increase contrast |
| LLM error | Check API key and internet connection |
| YOLO error | Make sure `yolov8n-seg.pt` exists and path is correct |

---

##  Clean Exit
To deactivate virtual environment:
```bash
deactivate
```

---

##  You're Ready!
Now you're set to analyze rooftops, simulate installations, and generate solar proposals like a pro.

---
Built with ❤️ by Satyam Tiwari for Wattmonk Internship Assessment.
