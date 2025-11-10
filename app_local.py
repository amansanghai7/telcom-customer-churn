"""
LOCAL TESTING APP - Quick Start for Development
================================================
Run this for local testing without Docker setup.

Usage:
    python app_local.py

Then open:
    - Gradio UI: http://localhost:8000/ui
    - API Docs: http://localhost:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
from src.serving.inference_local import predict

app = FastAPI(
    title="Telco Churn Predictor (Local)",
    description="Local testing version",
    version="1.0.0-local"
)

@app.get("/")
def root():
    return {"status": "ok", "mode": "local"}

class CustomerData(BaseModel):
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

@app.post("/predict")
def get_prediction(data: CustomerData):
    try:
        result = predict(data.dict())
        return {"prediction": result}
    except Exception as e:
        return {"error": str(e)}

def gradio_interface(
    gender, Partner, Dependents, PhoneService, MultipleLines,
    InternetService, OnlineSecurity, OnlineBackup, DeviceProtection,
    TechSupport, StreamingTV, StreamingMovies, Contract,
    PaperlessBilling, PaymentMethod, tenure, MonthlyCharges, TotalCharges
):
    data = {
        "gender": gender, "Partner": Partner, "Dependents": Dependents,
        "PhoneService": PhoneService, "MultipleLines": MultipleLines,
        "InternetService": InternetService, "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup, "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport, "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies, "Contract": Contract,
        "PaperlessBilling": PaperlessBilling, "PaymentMethod": PaymentMethod,
        "tenure": int(tenure), "MonthlyCharges": float(MonthlyCharges),
        "TotalCharges": float(TotalCharges)
    }
    result = predict(data)
    return str(result)

demo = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Dropdown(["Male", "Female"], label="Gender", value="Female"),
        gr.Dropdown(["Yes", "No"], label="Partner", value="No"),
        gr.Dropdown(["Yes", "No"], label="Dependents", value="No"),
        gr.Dropdown(["Yes", "No"], label="Phone Service", value="Yes"),
        gr.Dropdown(["Yes", "No", "No phone service"], label="Multiple Lines", value="No"),
        gr.Dropdown(["DSL", "Fiber optic", "No"], label="Internet Service", value="Fiber optic"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Online Security", value="No"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Online Backup", value="No"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Device Protection", value="No"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Tech Support", value="No"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming TV", value="Yes"),
        gr.Dropdown(["Yes", "No", "No internet service"], label="Streaming Movies", value="Yes"),
        gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract", value="Month-to-month"),
        gr.Dropdown(["Yes", "No"], label="Paperless Billing", value="Yes"),
        gr.Dropdown([
            "Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"
        ], label="Payment Method", value="Electronic check"),
        gr.Number(label="Tenure (months)", value=1, minimum=0, maximum=100),
        gr.Number(label="Monthly Charges ($)", value=85.0, minimum=0, maximum=200),
        gr.Number(label="Total Charges ($)", value=85.0, minimum=0, maximum=10000),
    ],
    outputs=gr.Textbox(label="Churn Prediction", lines=2),
    title="🔮 Telco Customer Churn Predictor (Local Testing)",
    description="Quick local testing version. Fill in customer details to predict churn.",
    examples=[
        ["Female", "No", "No", "Yes", "No", "Fiber optic", "No", "No", "No", 
         "No", "Yes", "Yes", "Month-to-month", "Yes", "Electronic check", 
         1, 85.0, 85.0],
        ["Male", "Yes", "Yes", "Yes", "Yes", "DSL", "Yes", "Yes", "Yes",
         "Yes", "No", "No", "Two year", "No", "Credit card (automatic)",
         60, 45.0, 2700.0]
    ],
)

app = gr.mount_gradio_app(app, demo, path="/ui")

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🚀 Starting Local Testing Server...")
    print("="*60)
    print("📍 Gradio UI:        http://localhost:8000/ui")
    print("📍 API Docs:         http://localhost:8000/docs")
    print("📍 Health Check:     http://localhost:8000/")
    print("="*60)
    print("⏹️  Press CTRL+C to stop\n")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
