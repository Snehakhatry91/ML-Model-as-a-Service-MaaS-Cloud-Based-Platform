import pickle, os
MODEL_DIR="models"; os.makedirs(MODEL_DIR,exist_ok=True)
def save_model(model,name):
    p=f"{MODEL_DIR}/{name}.pkl"
    with open(p,"wb") as f: pickle.dump(model,f)
    return p
def load_model(name):
    p=f"{MODEL_DIR}/{name}.pkl"
    return pickle.load(open(p,"rb")) if os.path.exists(p) else None
