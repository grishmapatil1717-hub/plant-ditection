from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class PlantInfoResponse(BaseModel):
    id: str
    name: str
    scientific_name: str
    icon: str
    classes: List[str]

class PredictionResponse(BaseModel):
    plant_id: str
    plant_name: str
    scientific_name: str
    predicted_disease: str
    pathogen: str
    confidence: float
    confidence_percent: str
    is_healthy: bool
    severity: str
    description: str
    causes: str
    symptoms: List[str]
    remedies: Dict[str, List[str]]
    class_probabilities: Dict[str, float]
    inference_time_ms: Optional[float] = None
    is_mock: bool = False

class HealthResponse(BaseModel):
    status: str
    version: str
    active_crops: List[str]
