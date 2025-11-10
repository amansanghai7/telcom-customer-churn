# 🐳 Docker Deployment Guide

## Overview
This guide explains how to build and deploy the Telco Customer Churn Prediction API using Docker.

## Model Information
- **Model ID**: `m-ec29a6bdcfdd48a4846f878e7fea9d3e`
- **Trained**: 2025-11-09 23:04:24
- **Performance**:
  - Recall: 82.1%
  - Precision: 47.7%
  - F1 Score: 60.4%
  - ROC-AUC: 83.8%

## Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Trained model available in `mlruns/` directory

## Quick Start

### Option 1: Using Build Script (Recommended)

**Windows:**
```bash
build_and_run.bat
```

**Linux/Mac:**
```bash
chmod +x build_and_run.sh
./build_and_run.sh
```

### Option 2: Using Docker Compose

```bash
docker-compose up -d
```

### Option 3: Manual Docker Commands

**Build the image:**
```bash
docker build -t telco-churn-predictor:latest .
```

**Run the container:**
```bash
docker run -d \
  --name churn-predictor-app \
  -p 8000:8000 \
  --restart unless-stopped \
  telco-churn-predictor:latest
```

## Access the Application

Once the container is running, access:

- **Gradio UI**: http://localhost:8000/ui
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/

## Docker Commands

### View Logs
```bash
docker logs -f churn-predictor-app
```

### Stop Container
```bash
docker stop churn-predictor-app
```

### Start Container
```bash
docker start churn-predictor-app
```

### Remove Container
```bash
docker rm -f churn-predictor-app
```

### Remove Image
```bash
docker rmi telco-churn-predictor:latest
```

### Check Container Status
```bash
docker ps -a | grep churn-predictor
```

### Execute Commands Inside Container
```bash
docker exec -it churn-predictor-app bash
```

## Testing the Deployed API

### Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "tenure": 1,
    "MonthlyCharges": 85.0,
    "TotalCharges": 85.0
  }'
```

### Using Python
```python
import requests

data = {
    "gender": "Female",
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "tenure": 1,
    "MonthlyCharges": 85.0,
    "TotalCharges": 85.0
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

## Dockerfile Structure

The Dockerfile includes:

1. **Base Image**: Python 3.11-slim for smaller size
2. **Dependencies**: Installs from `requirement.txt`
3. **Source Code**: Copies `src/` and `artifacts/`
4. **Model Artifacts**: Copies the latest trained model to `/app/model/`
5. **Environment**: Sets `PYTHONUNBUFFERED` and `PYTHONPATH`
6. **Health Check**: Monitors application health
7. **Entry Point**: Runs FastAPI with uvicorn

## Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs churn-predictor-app

# Check if port is already in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Linux/Mac
```

### Model Not Found Error
- Ensure you've trained the model: `python scripts/run_pipeline.py --input data/raw/Telco-Customer-Churn.csv`
- Check that the model path in Dockerfile matches your MLflow runs

### Import Errors
- Verify `PYTHONPATH` is set correctly in Dockerfile
- Check that all source files are copied properly

### Health Check Failing
- Wait 30 seconds after starting (health check has start period)
- Check if the app is responding: `curl http://localhost:8000/`

## Production Deployment

For production deployment, consider:

1. **Use a reverse proxy** (nginx, traefik) for SSL/TLS
2. **Set resource limits**:
   ```bash
   docker run -d \
     --name churn-predictor-app \
     -p 8000:8000 \
     --memory="2g" \
     --cpus="2" \
     telco-churn-predictor:latest
   ```
3. **Use environment variables** for configuration
4. **Set up monitoring** (Prometheus, Grafana)
5. **Configure logging** to external service
6. **Use orchestration** (Kubernetes, Docker Swarm) for scaling

## Image Size Optimization

Current optimizations:
- Using `python:3.11-slim` base image
- `--no-cache-dir` flag for pip
- `.dockerignore` to exclude unnecessary files
- Multi-stage builds (if needed for further optimization)

## Security Considerations

- Container runs as non-root user (can be added)
- No sensitive data in image
- Regular base image updates
- Scan for vulnerabilities: `docker scan telco-churn-predictor:latest`
