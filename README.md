# 🌿 Plant Detection AI — Crop Pathology & Disease Diagnosis System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://plant-ditection-ycvcyfawmtyacitg5q3uyq.streamlit.app/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

**Plant Detection AI** is a production-grade Deep Learning web application for plant disease detection and treatment recommendations across **Potato, Tomato, Apple, Corn, and Grape** crops.

🌐 **Live Streamlit Web Application:**  
👉 **[https://plant-ditection-ycvcyfawmtyacitg5q3uyq.streamlit.app/](https://plant-ditection-ycvcyfawmtyacitg5q3uyq.streamlit.app/)**

---

## 🚀 Key Features

1. **🌱 Multi-Crop Deep Learning Diagnostics:**
   - 🥔 **Potato (*Solanum tuberosum*):** Early Blight, Late Blight, Healthy Foliage.
   - 🍅 **Tomato (*Solanum lycopersicum*):** Early Blight, Late Blight, Septoria Leaf Spot, Healthy Foliage.
   - 🍎 **Apple (*Malus domestica*):** Apple Scab, Cedar Apple Rust, Healthy Foliage.
   - 🌽 **Corn / Maize (*Zea mays*):** Common Rust, Northern Leaf Blight, Cercospora (Gray) Leaf Spot, Healthy Foliage.
   - 🍇 **Grape (*Vitis vinifera*):** Black Rot, Esca (Black Measles), Leaf Blight, Healthy Foliage.

2. **📷 Flexible Input Modes & Leaf Validation:**
   - Upload image files (JPG, PNG, WebP, BMP, TIFF) or capture live photos with the built-in camera (`st.camera_input`).
   - Anti-spoofing leaf verification ensuring non-foliage (faces, objects, plain backgrounds) is rejected before inference.
   - 1-click test samples pre-configured for every crop condition.

3. **💡 Comprehensive Agronomic Prescriptions:**
   - Severity indicators (🟢 Healthy, 🟡 Moderate, 🔴 Severe / Critical).
   - **🌿 Organic Remedies** (Neem extract, bio-fungicides, canopy pruning).
   - **🧪 Chemical Fungicides** (Precise active ingredients and dilution dosages).
   - **🛡️ Preventative Measures** (Crop rotation, drip irrigation, resistant cultivars).

4. **🗄️ Supabase Cloud Database & Storage:**
   - Real-time cloud persistence for user authentication, scan history, and high-resolution leaf image storage.
   - Automatic offline SQLite fallback when offline.

5. **📊 Analytics & Performance Curves:**
   - Scan volume breakdowns, health ratios, and disease frequency rankings.
   - Epoch-by-epoch training/validation accuracy and loss curves for each deep learning architecture.

6. **📄 PDF Diagnostic Health Reports:**
   - 1-click generation of professional agronomic reports formatted with timestamps, symptoms, and prescriptions.

7. **🎨 Modern Theme Engine:**
   - Seamless toggle between Dark Slate and Light Clean UI themes.

---

## 🛠️ Tech Stack

- **Frontend & Web Framework:** [Streamlit](https://streamlit.io/)
- **Deep Learning & Computer Vision:** TensorFlow, Keras, NumPy, Pillow
- **Cloud Database & Storage:** Supabase (PostgreSQL + Object Storage)
- **Data Visualizations:** Plotly Express
- **Report Generation:** FPDF2

---

## 💻 Local Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/grishmapatil1717-hub/plant-ditection.git
cd plant-ditection
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux / macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Streamlit Application
```bash
streamlit run App.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## ☁️ Streamlit Community Cloud Deployment

The application is deployed directly on **Streamlit Community Cloud**:
- **Repository:** `grishmapatil1717-hub/plant-ditection`
- **Main Module:** `App.py`
- **Python Version:** 3.11+
- **Live URL:** [https://plant-ditection-ycvcyfawmtyacitg5q3uyq.streamlit.app/](https://plant-ditection-ycvcyfawmtyacitg5q3uyq.streamlit.app/)
