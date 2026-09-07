import time
import io
import uvicorn
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import config
from backend.api.schemas import PlantInfoResponse, PredictionResponse, HealthResponse
from preprocessor import preprocess_image, validate_leaf_image
from models.potato_model import predict_potato
from models.tomato_model import predict_tomato
from models.apple_model import predict_apple
from models.corn_model import predict_corn
from models.grape_model import predict_grape

app = FastAPI(
    title="Plant Detection AI - REST API",
    description="High-performance Computer Vision REST API for multi-crop plant pathology diagnosis.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Plant Detection AI API",
        "docs": "/docs",
        "status": "online"
    }

@app.get("/health", response_model=HealthResponse, tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "version": "2.0.0",
        "active_crops": list(config.PLANTS.keys())
    }

@app.get("/plants", response_model=List[PlantInfoResponse], tags=["Crops"])
def list_plants():
    return [
        {
            "id": k,
            "name": v["name"],
            "scientific_name": v["scientific_name"],
            "icon": v["icon"],
            "classes": v["classes"]
        }
        for k, v in config.PLANTS.items()
    ]

@app.post("/predict", response_model=PredictionResponse, tags=["Inference"])
async def predict_crop(
    plant: str = Form(..., description="Target crop: potato, tomato, apple, corn, grape"),
    file: UploadFile = File(..., description="Leaf image file (JPG, PNG, WebP)")
):
    plant_key = plant.lower().strip()
    if plant_key not in config.PLANTS:
        raise HTTPException(status_code=400, detail=f"Unsupported plant '{plant}'. Available: {list(config.PLANTS.keys())}")

    start_time = time.time()
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")

    display_img, resized_img, tensor_input, meta = preprocess_image(image)
    is_leaf, leaf_msg, _ = validate_leaf_image(display_img)
    
    if not is_leaf:
        raise HTTPException(status_code=422, detail=f"Leaf validation failed: {leaf_msg}")

    filename = file.filename or ""
    if plant_key == "potato":
        res = predict_potato(tensor_input, filename)
    elif plant_key == "tomato":
        res = predict_tomato(tensor_input, filename)
    elif plant_key == "apple":
        res = predict_apple(tensor_input, filename)
    elif plant_key == "corn":
        res = predict_corn(tensor_input, filename)
    elif plant_key == "grape":
        res = predict_grape(tensor_input, filename)
    else:
        res = predict_potato(tensor_input, filename)

    res["inference_time_ms"] = round((time.time() - start_time) * 1000, 2)
    return res

if __name__ == "__main__":
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=8000, reload=True)
