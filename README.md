# Heart Disease Prediction API

A REST API that predicts the presence of heart disease using a Random Forest
classifier trained on the Heart Disease dataset. Built with FastAPI, containerized
with Docker, and deployed on Render.

---

## Tech Stack

- **FastAPI** — API framework
- **scikit-learn** — Machine learning model
- **Docker** — Containerization
- **Render** — Cloud deployment

---

## Project Structure
heart-disease-api/
├── app/
│   ├── init.py
│   ├── main.py        # API endpoints
│   └── schemas.py     # Pydantic input model
├── model/
│   ├── train.py       # Training script
│   └── heart_model.joblib  # Saved model
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
---

## Endpoints

| Method | Endpoint   | Description                        |
|--------|------------|------------------------------------|
| GET    | /health    | Health check — is the API alive?   |
| GET    | /info      | Model metadata and feature list    |
| POST   | /predict   | Predict heart disease from features|

---

## Run Locally with Docker

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/heart-disease-api.git
cd heart-disease-api
```

**2. Build and run**
```bash
docker-compose up --build
```

**3. Open Swagger UI**
http://localhost:5000/docs
---

## Run Locally Without Docker

**1. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Train the model**
```bash
python model/train.py
```

**4. Start the server**
```bash
uvicorn app.main:app --reload
```

---

## Sample Request

```bash
curl -X POST "http://localhost:5000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 55,
    "sex": 1,
    "cp": 0,
    "trestbps": 130,
    "chol": 250,
    "fbs": 0,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 2,
    "ca": 0,
    "thal": 2
  }'
```

## Sample Response

```json
{
  "heart_disease": true,
  "confidence": 0.97,
  "details": {
    "probability_no_disease": 0.03,
    "probability_disease": 0.97
  }
}
```

---

## Dataset

[Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
on Kaggle — 1025 rows, 13 features, binary target.

---

## Deployment

Live API on Render:
**https://heart-disease-api-re57.onrender.com**