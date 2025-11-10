"""
Quick Start Script for Local Testing
Run this to start the FastAPI + Gradio app locally
"""
import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Telco Churn Prediction App...")
    print("📍 API Documentation: http://localhost:8000/docs")
    print("🎨 Gradio UI: http://localhost:8000/ui")
    print("💚 Health Check: http://localhost:8000/")
    print("\n⏹️  Press CTRL+C to stop\n")
    
    uvicorn.run(
        "src.app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
