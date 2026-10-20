# Creating the FastAPI application
from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Iris Model API")
model = joblib.load(Path(__file__).parent / "models" / "iris_model.pkl")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def health():
    return {"status": "ok", "service": "iris-model-api"}

@app.post("/predict")
def predict(features: IrisFeatures):
    row = [[features.sepal_length, features.sepal_width,
            features.petal_length, features.petal_width]]
    return {"prediction": int(model.predict(row)[0])}
