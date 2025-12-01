from pydantic import BaseModel
class TrainRequest(BaseModel):
    model_name:str
    csv_path:str
    target:str
class PredictRequest(BaseModel):
    model_name:str
    features:list
