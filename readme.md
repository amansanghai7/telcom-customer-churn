# 🔮 Telecom Customer Churn Prediction

An end-to-end machine learning project for predicting customer churn in the telecommunications industry using XGBoost, with production-ready deployment on Render and comprehensive MLOps practices.

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com/)
[![MLflow](https://img.shields.io/badge/MLflow-2.14.1-0194E2.svg)](https://mlflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌐 Live Demo

**🚀 Try it now:** [https://telcom-customer-churn.onrender.com/ui](https://telcom-customer-churn.onrender.com/ui)

> **Note:** The app is hosted on Render's free tier and may take 30-60 seconds to wake up on first request.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [MLOps Pipeline](#mlops-pipeline)
- [Contributing](#contributing)

---

## 🎯 Overview

This project implements a complete machine learning solution to predict customer churn for telecom companies. It identifies customers at risk of leaving, enabling proactive retention strategies. The solution includes data validation, feature engineering, model training with hyperparameter optimization, experiment tracking, and production deployment with both REST API and interactive UI.

### Business Impact
- **82.1% Recall**: Catches 8 out of 10 customers who will churn
- **83.8% ROC-AUC**: Excellent discrimination between churners and non-churners
- **Real-time Predictions**: Sub-second inference time for immediate action
- **Cost Savings**: Early identification enables targeted retention campaigns

---

## ✨ Key Features

### Machine Learning
- ✅ **XGBoost Classifier** with optimized hyperparameters
- ✅ **Automated Feature Engineering** with deterministic transformations
- ✅ **Class Imbalance Handling** using scale_pos_weight
- ✅ **Hyperparameter Tuning** with Optuna (20 trials)
- ✅ **Model Versioning** and experiment tracking with MLflow

### Data Quality
- ✅ **Automated Data Validation** using Great Expectations patterns
- ✅ **22 Quality Checks** including schema, business rules, and consistency
- ✅ **Missing Value Handling** with intelligent imputation strategies
- ✅ **Feature Consistency** between training and serving

### Production Deployment
- ✅ **FastAPI REST API** with automatic OpenAPI documentation
- ✅ **Gradio Web Interface** for interactive predictions
- ✅ **Docker Containerization** for consistent environments
- ✅ **CI/CD Pipeline** with GitHub Actions
- ✅ **Cloud Deployment** on Render (free tier)
- ✅ **Health Checks** and monitoring endpoints

---

## 🏗️ Project Architecture

```
┌─────────────────┐
│   Raw Data      │
│  (7,043 rows)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Validation │ ◄── Great Expectations
│  (22 checks)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Preprocessing   │
│ - Clean data    │
│ - Handle nulls  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Feature Eng.    │
│ - Binary encode │
│ - One-hot encode│
│ - 30 features   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Training  │ ◄── XGBoost + Optuna
│ - Train/Test    │
│ - Evaluation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ MLflow Tracking │
│ - Experiments   │
│ - Metrics       │
│ - Artifacts     │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│      Production Serving      │
├─────────────┬───────────────┤
│  FastAPI    │    Gradio     │
│  REST API   │   Web UI      │
└─────────────┴───────────────┘
         │
         ▼
┌─────────────────┐
│  Render Cloud   │
│  (Deployed)     │
└─────────────────┘
```

---

## 🛠️ Tech Stack

### Core ML & Data Science
- **Python 3.11** - Programming language
- **XGBoost 3.0.3** - Gradient boosting framework
- **scikit-learn 1.5.2** - ML utilities and metrics
- **pandas 2.1.4** - Data manipulation
- **numpy 1.26.4** - Numerical computing

### MLOps & Experiment Tracking
- **MLflow 2.14.1** - Experiment tracking and model registry
- **Optuna 4.4.0** - Hyperparameter optimization
- **Great Expectations 1.5.8** - Data validation

### API & Web Framework
- **FastAPI 0.115.0** - High-performance REST API
- **Gradio 5.49.1** - Interactive web interface
- **Uvicorn 0.30.5** - ASGI server
- **Pydantic 2.8.2** - Data validation

### Deployment & DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Render** - Cloud platform (PaaS)

### Visualization
- **Matplotlib 3.10.5** - Plotting library
- **Seaborn 0.13.2** - Statistical visualization

---

## 📊 Model Performance

### Latest Model (Nov 9, 2025)
- **Model ID**: `m-ec29a6bdcfdd48a4846f878e7fea9d3e`
- **Algorithm**: XGBoost Classifier
- **Training Time**: 1.65 seconds
- **Inference Time**: 0.011 seconds (~91 predictions/second)

### Metrics
| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Recall** | 82.1% | Catches 82% of actual churners |
| **Precision** | 47.7% | 48% of predicted churners actually churn |
| **F1 Score** | 60.4% | Balanced performance measure |
| **ROC-AUC** | 83.8% | Excellent discrimination ability |
| **Accuracy** | 71.4% | Overall correctness |

### Hyperparameters
```python
{
    'n_estimators': 301,
    'learning_rate': 0.034,
    'max_depth': 7,
    'subsample': 0.95,
    'colsample_bytree': 0.98,
    'scale_pos_weight': 2.77  # Handles class imbalance
}
```

### Feature Importance
Top predictors of churn:
1. Contract type (Month-to-month vs long-term)
2. Tenure (months with company)
3. Internet service type (Fiber optic)
4. Monthly charges
5. Payment method (Electronic check)

---

## 🚀 Installation

### Prerequisites
- Python 3.11.0
- Git
- (Optional) Docker for containerized deployment

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/amansanghai7/telcom-customer-churn.git
cd telcom-customer-churn
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirement.txt
```

4. **Train the model** (optional - pre-trained model included)
```bash
python scripts/run_pipeline.py --input data/raw/Telco-Customer-Churn.csv
```

5. **Run the application**
```bash
python app_local.py
```

6. **Access the application**
- Gradio UI: http://localhost:8000/ui
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/

---

## 💻 Usage

### Web Interface (Gradio)

1. Navigate to http://localhost:8000/ui
2. Fill in customer details using the dropdowns and input fields
3. Click "Submit" to get instant churn prediction
4. Try the example customers (high-risk and low-risk profiles)

### REST API

**Python Example:**
```python
import requests

customer_data = {
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

response = requests.post(
    "http://localhost:8000/predict",
    json=customer_data
)

print(response.json())
# Output: {"prediction": "Likely to churn"}
```

**cURL Example:**
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

---

## 📚 API Documentation

### Endpoints

#### `GET /`
Health check endpoint
```json
{
  "status": "ok"
}
```

#### `POST /predict`
Predict customer churn

**Request Body:**
```json
{
  "gender": "string",
  "Partner": "string",
  "Dependents": "string",
  "PhoneService": "string",
  "MultipleLines": "string",
  "InternetService": "string",
  "OnlineSecurity": "string",
  "OnlineBackup": "string",
  "DeviceProtection": "string",
  "TechSupport": "string",
  "StreamingTV": "string",
  "StreamingMovies": "string",
  "Contract": "string",
  "PaperlessBilling": "string",
  "PaymentMethod": "string",
  "tenure": 0,
  "MonthlyCharges": 0.0,
  "TotalCharges": 0.0
}
```

**Response:**
```json
{
  "prediction": "Likely to churn" | "Not likely to churn"
}
```

**Interactive Documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 🌐 Deployment

### Render (Production)

**🌐 Live Application:** [https://telcom-customer-churn.onrender.com/ui](https://telcom-customer-churn.onrender.com/ui)

**API Endpoints:**
- Gradio UI: [https://telcom-customer-churn.onrender.com/ui](https://telcom-customer-churn.onrender.com/ui)
- API Docs: [https://telcom-customer-churn.onrender.com/docs](https://telcom-customer-churn.onrender.com/docs)
- Health Check: [https://telcom-customer-churn.onrender.com/](https://telcom-customer-churn.onrender.com/)

**Deployment Steps:**
1. Fork/clone this repository
2. Create account on [Render](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Configure:
   - **Build Command:** `pip install --upgrade pip && pip install -r requirement.txt`
   - **Start Command:** `uvicorn src.app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variable:** `PYTHON_VERSION=3.11.0`
6. Deploy!

### Docker

**Build and run locally:**
```bash
docker build -t churn-predictor .
docker run -p 8000:8000 churn-predictor
```

**Using Docker Compose:**
```bash
docker-compose up -d
```

**Pre-built scripts:**
- Windows: `build_and_run.bat`
- Linux/Mac: `./build_and_run.sh`

---

## 📁 Project Structure

```
telcom-customer-churn/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # CI/CD pipeline
│
├── data/
│   ├── raw/                       # Original dataset
│   ├── processed/                 # Cleaned data
│   └── external/                  # External data sources
│
├── src/
│   ├── app/
│   │   └── main.py               # FastAPI + Gradio application
│   ├── data/
│   │   ├── load_data.py          # Data loading utilities
│   │   └── preprocess.py         # Data preprocessing
│   ├── features/
│   │   └── build_features.py     # Feature engineering
│   ├── models/
│   │   ├── train.py              # Model training
│   │   ├── tune.py               # Hyperparameter tuning
│   │   └── evaluate.py           # Model evaluation
│   ├── serving/
│   │   ├── inference.py          # Production inference (Docker)
│   │   └── inference_local.py    # Local inference (Render)
│   └── utils/
│       ├── validate_data.py      # Data validation
│       └── utils.py              # Helper functions
│
├── scripts/
│   ├── run_pipeline.py           # Main training pipeline
│   └── prepare_processed_data.py # Data preparation
│
├── mlruns/                        # MLflow experiment tracking
├── artifacts/                     # Model artifacts
│   ├── feature_columns.json      # Feature schema
│   └── preprocessing.pkl         # Preprocessing metadata
│
├── dockerfile                     # Docker configuration
├── docker-compose.yml            # Docker Compose setup
├── requirement.txt               # Python dependencies
├── runtime.txt                   # Python version for Render
├── .gitignore                    # Git ignore rules
└── readme.md                     # This file
```

---

## 🔄 MLOps Pipeline

### 1. Data Validation
- **22 automated checks** using Great Expectations patterns
- Schema validation (column existence, data types)
- Business rule validation (valid categories, ranges)
- Consistency checks (TotalCharges >= MonthlyCharges)

### 2. Feature Engineering
- **Binary encoding** for 2-category features (gender, Partner, etc.)
- **One-hot encoding** for multi-category features (Contract, InternetService)
- **Deterministic transformations** ensuring train/serve consistency
- **30 final features** from 18 input features

### 3. Model Training
- **Train/test split**: 80/20 with stratification
- **Class imbalance handling**: scale_pos_weight = 2.77
- **Hyperparameter optimization**: Optuna with 20 trials
- **Cross-validation**: 3-fold CV for robust evaluation

### 4. Experiment Tracking
- **MLflow integration** for all experiments
- **Metrics logged**: precision, recall, F1, ROC-AUC, training time
- **Artifacts saved**: model, feature schema, preprocessing metadata
- **Model versioning**: Each run gets unique ID

### 5. Model Serving
- **Feature consistency**: Same transformations as training
- **Input validation**: Pydantic schemas
- **Error handling**: Graceful fallbacks
- **Performance**: <15ms inference time

### 6. CI/CD
- **Automated testing** on push to main
- **Docker image building** and pushing to Docker Hub
- **Automatic deployment** to Render on successful build
- **Health checks** to verify deployment

---

## 🎓 Key Learnings & Best Practices

### Data Science
- ✅ Always validate data quality before training
- ✅ Handle class imbalance explicitly
- ✅ Use cross-validation for robust evaluation
- ✅ Track all experiments systematically
- ✅ Optimize for business metric (recall for churn)

### MLOps
- ✅ Ensure feature consistency between training and serving
- ✅ Version everything (data, code, models, environment)
- ✅ Automate the entire pipeline
- ✅ Monitor model performance in production
- ✅ Use containerization for reproducibility

### Software Engineering
- ✅ Write modular, reusable code
- ✅ Document thoroughly
- ✅ Use type hints and validation
- ✅ Implement proper error handling
- ✅ Follow security best practices (secrets management)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Aman Sanghai**

- GitHub: [@amansanghai7](https://github.com/amansanghai7)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/aman-sanghai)

---

## 🙏 Acknowledgments

- Dataset: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle
- MLflow for experiment tracking
- FastAPI and Gradio for serving frameworks
- Render for free cloud hosting

---

## 📞 Support

If you have any questions or issues, please:
1. Check the [documentation](QUICKSTART.md)
2. Search [existing issues](https://github.com/amansanghai7/telcom-customer-churn/issues)
3. Create a [new issue](https://github.com/amansanghai7/telcom-customer-churn/issues/new)

---

**⭐ If you find this project helpful, please give it a star!**
