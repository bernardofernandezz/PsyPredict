from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    # ... all other fields ...

@app.post("/predict")
def predict_churn(data: CustomerData):
    result = predict(data.dict())
    return {"churn": int(result)}
