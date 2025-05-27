# ☀️ AI-Powered Solar Rooftop Analyzer

This is a Streamlit-based web application that uses AI to detect rooftops from satellite images and estimate their solar potential, installation feasibility, and ROI — designed specifically for homeowners and solar professionals.

>  Built as part of the **Wattmonk Technologies Internship Assessment**

---

##  What It Does
- Detects rooftop areas using YOLOv8 segmentation model
- Estimates solar panel system size, cost, and annual savings
- Calculates ROI and payback period
- Generates expert-level installation recommendations using LLM

---

##  Live Demo (Optional for Hugging Face Spaces)

Try it live on [Hugging Face Spaces](https://huggingface.co/spaces/your-username/solar-rooftop-analyzer) *(link to be added once deployed)*

---

##  How It Works

###  1. **Rooftop Detection (Vision AI)**
We use [Ultralytics YOLOv8-nano segmentation](https://docs.ultralytics.com) model (`yolov8n-seg.pt`) to simulate rooftop detection. 
- In early development, we use a **simulated mask** covering the central 70% of the image.
- This approach helps keep the model lightweight and avoids the need for labeled satellite image datasets.

> 🔄 Future upgrade: fine-tuned YOLOv8 for real rooftop segmentation.

###  2. **Solar System Estimation**
Using detected rooftop area (in m²), we calculate:
- Total system size (kW)
- Annual energy generation (kWh)
- Total installation cost
- Annual savings and payback period

This is handled via simple heuristics in `solar_calc.py` — fully customizable per region or client.

###  3. **LLM Integration for Expert Advice**
We connect to an LLM to generate:
- Recommended panel type
- Optimal tilt/orientation
- Government subsidies
- Value-added installation tips

####  LLM Options
- **OpenAI GPT-3.5**: Recommended if you have credits (default behavior)
- **OpenRouter API**: Free models like `deepseek-chat:free` supported, but limited by credit/quota

>  OpenRouter support is built-in. Due to quota limits, we recommend OpenAI for production use.

---

##  Setup Instructions

```bash
git clone https://github.com/96satyam/solar_ai_assistant.git
cd solar_ai_assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Download YOLO weights:
```bash
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-seg.pt -P models/
```

Add `.env` file:
```env
OPENAI_API_KEY=sk-xxx
# or
OPENROUTER_API_KEY=sk-or-xxx
```

Run the app:
```bash
streamlit run app.py
```

---

##  Example Output
| Component | Sample |
|----------|--------|
| Rooftop Area | 55,216 m² |
| System Size | 8,494.77 kW |
| ROI | 2.4 years |
| LLM Summary | ✅ Monocrystalline panels<br>✅ 27,600 panels<br>✅ South-facing @ 28° tilt |

---

## 📁 Folder Structure
```
solar_ai_assistant/
├── app.py                  # Streamlit app
├── models/                # YOLO logic
├── utils/                 # Area, ROI, prompt, LLM
├── assets/sample_images/  # Test images
├── requirements.txt
├── setup_instructions.md
└── README.md
```

---

##  Deployment on Hugging Face Spaces
To deploy on Hugging Face:
1. Create a new Space (Python + Streamlit)
2. Upload all project files
3. Add `yolov8n-seg.pt` inside `models/`
4. Set environment variables under "Secrets"

---

## 🔮 Future Enhancements
- 🔍 Real rooftop detection using fine-tuned YOLO
- 🌦️ Real irradiance data via Meteo or Google Solar API
- 🗺️ Auto-location inference using coordinates
- 📦 Deploy as a cloud API (FastAPI backend)

---

## 👨‍💻 Author
**Satyam Tiwari**  
AI & Data Science Final Year @ VIPS-TC  
🔗 [LinkedIn](https://www.linkedin.com/in/satyam9695/)  | 📫 [Email](shivt843@gmail.com)

---

Built with ❤️ for the clean energy future.
