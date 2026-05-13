from fastapi import FastAPI, HTTPException
from app.schemas import PatientFeatures
import joblib
import numpy as np
import os

# ── App setup ────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predicts presence of heart disease using a Random Forest classifier trained on the Heart Disease dataset.",
    version="1.0.0"
)

# ── Load model at startup ────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "heart_model.joblib")

try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from: {MODEL_PATH}")
except FileNotFoundError:
    print(f"ERROR: Model not found at {MODEL_PATH}")
    print("Run 'python model/train.py' first to generate the model file.")
    model = None

# The exact feature order matters — must match how the model was trained
FEATURE_LIST = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal"
]

# ── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/health", tags=["Monitoring"])
def health():
    """
    Simple health check.
    Returns 'ok' if the API is running and the model is loaded.
    Render uses this to know your service is alive.
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.get("/info", tags=["Monitoring"])
def info():
    """
    Returns metadata about the model.
    Useful for knowing what version/type of model is running in production.
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {
        "model_type": type(model).__name__,
        "model_version": "1.0.0",
        "features": FEATURE_LIST,
        "feature_count": len(FEATURE_LIST),
        "description": "Random Forest classifier trained on the Heart Disease dataset",
        "output": "heart_disease: true (disease present) or false (no disease)"
    }


@app.post("/predict", tags=["Prediction"])
def predict(patient: PatientFeatures):
    """
    Takes patient features and returns a heart disease prediction.

    - **true** = heart disease likely present
    - **false** = heart disease likely absent
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")


    features = np.array([[
        patient.age,
        patient.sex,
        patient.cp,
        patient.trestbps,
        patient.chol,
        patient.fbs,
        patient.restecg,
        patient.thalach,
        patient.exang,
        patient.oldpeak,
        patient.slope,
        patient.ca,
        patient.thal
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]

    return {
        "heart_disease": bool(prediction),
        "confidence": round(float(max(probability)), 4),
        "details": {
            "probability_no_disease": round(float(probability[0]), 4),
            "probability_disease": round(float(probability[1]), 4)
        }
    }