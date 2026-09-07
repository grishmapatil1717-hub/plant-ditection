# 🤖 Plant Detection AI — Backend & Training Architecture

This directory contains the full backend suite for **Plant Detection AI**, including REST API microservices, model training pipelines, and Jupyter training notebooks.

---

## 📁 Directory Structure

```
backend/
├── api/
│   ├── main.py             # FastAPI REST Server (/predict, /plants, /health)
│   ├── schemas.py          # Pydantic Request & Response Data Models
│   └── routes.py           # Endpoint Handlers & Routing
├── training/
│   ├── train_models.py     # Multi-architecture Training Engine (CNN, MobileNet, ResNet)
│   ├── dataset_loader.py   # Augmentation & Batch Generators
│   └── evaluate.py         # Confusion Matrix & Classification Metrics
├── notebooks/              # End-to-End Jupyter Training Notebooks
│   ├── 1_potato_disease_classification.ipynb
│   ├── 2_tomato_disease_classification.ipynb
│   ├── 3_apple_disease_classification.ipynb
│   ├── 4_corn_disease_classification.ipynb
│   └── 5_grape_disease_classification.ipynb
└── requirements.txt        # Backend & Training Dependencies
```

---

## 🚀 Running the FastAPI Backend Server

1. **Install Backend Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Launch the FastAPI Server:**
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Explore Interactive Swagger API Docs:**
   Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

---

## 🏋️ Training Models

To train any crop model using your local dataset:

```bash
python training/train_models.py --crop potato --arch mobilenetv2 --epochs 25 --data_dir ./dataset/potato
```
