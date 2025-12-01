# ML Model as a Service Platform (MaaS)

A cloud-ready **Machine Learning Model as a Service (MaaS)** platform built using **FastAPI**, designed to train, store, version, and serve ML models through simple REST APIs.  
This platform represents a real-world MLOps-style architecture.

---

## 🚀 Overview

This MaaS platform enables:

- Train ML models using CSV datasets  
- Auto-save trained models as `.pkl`  
- Get accuracy score after training  
- Perform predictions using deployed models  
- Maintain model registry with versioning  
- Authenticate using JWT tokens  
- Deploy easily on cloud or Docker  

---

## 📁 Project Structure

ml_maas_platform/
├── main.py # FastAPI entrypoint
├── auth.py # JWT authentication logic
├── schemas.py # Pydantic request models
├── trainer.py # Model training engine
├── predictor.py # Prediction engine
├── preprocessing.py # Feature preprocessing pipeline
├── storage.py # Model save/load handler
├── registry.py # Model registry system
├── requirements.txt # Dependencies
└── README.md # Documentation

markdown
Copy code

---

## ✨ Features

### 🔐 Authentication
- API-level JWT token security  
- Protect model operations  

### 🎯 Train Models (API Based)
- Accept CSV path  
- Auto split training/testing  
- Train Random Forest model  
- Return accuracy  
- Save model to `models/` folder  

### 🤖 Prediction Engine
- Predict using saved model  
- Automatic preprocessing (StandardScaler)  

### 📦 Model Registry
- Store model version  
- Path and timestamp tracking  
- Useful for cloud-based model management  

### ⚙ Modular System
- Trainer  
- Predictor  
- Storage  
- Registry  
- Preprocessing  

---

## 🛠 Installation

### 1️⃣ Clone Project
```bash
git clone <your_repo_url>
cd ml_maas_platform
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
3️⃣ Activate Environment
CMD

bash
Copy code
venv\Scripts\activate
PowerShell

bash
Copy code
.\venv\Scripts\Activate.ps1
4️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
5️⃣ Run API Server
bash
Copy code
uvicorn main:app --reload
6️⃣ Open Interactive API Docs
👉 http://127.0.0.1:8000/docs

🧪 Example API Usage
🔑 Get Token
POST /login

json
Copy code
{
  "token": "<your-jwt-token>"
}
🎯 Train Model
POST /train

json
Copy code
{
  "model_name": "iris_model",
  "csv_path": "data/iris.csv",
  "target": "species"
}
Response

json
Copy code
{
  "model_name": "iris_model",
  "accuracy": 0.94
}
🤖 Predict
POST /predict

json
Copy code
{
  "model_name": "iris_model",
  "features": [5.1, 3.5, 1.4, 0.2]
}
Response

json
Copy code
{
  "model": "iris_model",
  "prediction": "setosa"
}
📚 List All Models
GET /models

json
Copy code
{
  "iris_model": {
    "version": "v1",
    "path": "models/iris_model.pkl",
    "timestamp": "2025-12-01 17:22:00"
  }
}
🐳 Docker Deployment
Build Image
bash
Copy code
docker build -t ml-maas .
Run Container
bash
Copy code
docker run -p 8000:8000 ml-maas
🌩 Cloud Deployment Options
Render

Railway

AWS EC2 / Lambda

Azure App Service

Google Cloud Run

Docker Swarm / Kubernetes

📜 License
Free to use for learning, research, and development.
