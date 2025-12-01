from storage import load_model
from preprocessing import preprocess

def predict(model,features):
    m=load_model(model)
    if m is None: return {"error":"Model not found"}
    p=preprocess(features)
    return {"model":model,"prediction":str(m.predict([p])[0])}
