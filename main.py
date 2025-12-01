from fastapi import FastAPI
from trainer import train_model
from predictor import predict
from schemas import TrainRequest,PredictRequest
from registry import list_models
from auth import create_token

app=FastAPI(title="ML Model as a Service")

@app.get("/") 
def home(): return {"message":"MaaS Running"}

@app.post("/login")
def login(): return {"token":create_token({"user":"admin"})}

@app.post("/train")
def train(r:TrainRequest): return train_model(r.model_name,r.csv_path,r.target)

@app.post("/predict")
def do_predict(r:PredictRequest): return predict(r.model_name,r.features)

@app.get("/models")
def models(): return list_models()
