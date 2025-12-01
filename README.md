 ML Model as a Service (MaaS) – Cloud-Based Platform

**FastAPI • Python • Docker • JWT Secured**  
A complete **Machine Learning as a Service** platform that lets you train, version, store, and serve ML models using simple, secure REST APIs — full MLOps experience in one lightweight project!

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Secured-success?style=for-the-badge&logo=jsonwebtokens)

---

## Features

- Secure JWT Authentication for all endpoints  
- Train Random Forest models from CSV with a single API call  
- Automatic train/test split & accuracy reporting  
- Auto-save trained models as `.pkl` with versioning  
- Real-time prediction API with built-in preprocessing  
- StandardScaler pipeline applied automatically  
- Full model registry (name → version → path → timestamp)  
- Clean, modular, production-ready code structure  
- Docker support out of the box  
- Ready for cloud deployment (Render, Railway, AWS, GCP, Azure, etc.)

---

## Project Structure

```bash
ml_maas_platform/
├── main.py              # FastAPI application entrypoint
├── auth.py              # JWT authentication & token management
├── schemas.py           # Pydantic models for request/response validation
├── trainer.py           # Model training logic (Random Forest)
├── predictor.py         # Inference engine
├── preprocessing.py     # StandardScaler pipeline
├── storage.py           # Save/load model utilities
├── registry.py          # Model registry & versioning system
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation

Quick Start (Runs in 2 minutes)
Bashgit clone https://github.com/yourusername/ml_maas_platform.git
cd ml_maas_platform

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
Open interactive docs → http://127.0.0.1:8000/docs

API Endpoints
1. Get JWT Token
httpPOST /login
{
  "username": "admin",
  "password": "admin"
}
2. Train a Model
httpPOST /train
Authorization: Bearer <your-token>

{
  "model_name": "iris_model",
  "csv_path": "data/iris.csv",
  "target": "species"
}
3. Predict
httpPOST /predict
Authorization: Bearer <your-token>

{
  "model_name": "iris_model",
  "features": [5.1, 3.5, 1.4, 0.2]
}
4. List All Models
httpGET /models
Authorization: Bearer <your-token>

Docker Deployment
Bashdocker build -t ml-maas .
docker run -d -p 8000:8000 ml-maas
API available at → http://localhost:8000

One-Click Cloud Deployment

Render (free tier)
Railway (free tier)
Google Cloud Run
AWS ECS / EC2 / Lambda + Container
Azure Container Apps
Kubernetes


License
Completely free for learning, research, personal projects, and commercial use — no restrictions!
