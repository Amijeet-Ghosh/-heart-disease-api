from pydantic import BaseModel, Field

class PatientFeatures(BaseModel):
 

    age: int = Field(..., description="Age of the patient in years", example=55)
    
    sex: int = Field(..., description="Sex: 1 = male, 0 = female", example=1)
    
    cp: int = Field(..., description="Chest pain type: 0-3", example=0)
    
    trestbps: int = Field(..., description="Resting blood pressure (mm Hg)", example=130)
    
    chol: int = Field(..., description="Serum cholesterol (mg/dl)", example=250)
    
    fbs: int = Field(..., description="Fasting blood sugar > 120 mg/dl: 1 = true, 0 = false", example=0)
    
    restecg: int = Field(..., description="Resting ECG results: 0-2", example=0)
    
    thalach: int = Field(..., description="Maximum heart rate achieved", example=150)
    
    exang: int = Field(..., description="Exercise induced angina: 1 = yes, 0 = no", example=0)
    
    oldpeak: float = Field(..., description="ST depression induced by exercise", example=1.5)
    
    slope: int = Field(..., description="Slope of peak exercise ST segment: 0-2", example=2)
    
    ca: int = Field(..., description="Number of major vessels colored by fluoroscopy: 0-4", example=0)
    
    thal: int = Field(..., description="Thalassemia: 1 = normal, 2 = fixed defect, 3 = reversible defect", example=2)

    class Config:
        # This makes the Swagger UI show a filled example automatically
        json_schema_extra = {
            "example": {
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
            }
        }