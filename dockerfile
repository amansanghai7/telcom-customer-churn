# ============================================================================
# DOCKERFILE - Telco Customer Churn Prediction API
# ============================================================================
# This Dockerfile creates a production-ready container for serving the
# XGBoost churn prediction model via FastAPI + Gradio interface.
#
# Build: docker build -t churn-predictor .
# Run:   docker run -p 8000:8000 churn-predictor
# ============================================================================

# 1. Base Image - Python 3.11 slim for smaller image size
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file first (leverages Docker layer caching)
# This means dependencies only reinstall if requirement.txt changes
COPY requirement.txt .

# 4. Install Python dependencies
# - Upgrade pip to latest version
# - Install all required packages from requirement.txt
# - Clean up apt cache to reduce image size
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirement.txt

# 5. Copy source code and configuration files
# This includes all Python modules needed for inference
COPY src/ /app/src/
COPY artifacts/ /app/artifacts/

# 6. Copy the trained model artifacts to /app/model
# IMPORTANT: This is the path that inference.py expects in production
# Model ID: m-ec29a6bdcfdd48a4846f878e7fea9d3e (Latest trained model)
# Trained: 2025-11-09 23:04:24
# Performance: Recall=82.1%, ROC-AUC=83.8%
COPY mlruns/449370520553593410/models/m-ec29a6bdcfdd48a4846f878e7fea9d3e/artifacts/ /app/model/

# 7. Set environment variables
# PYTHONUNBUFFERED=1: Ensures logs appear in real-time (no buffering)
# PYTHONPATH=/app: Allows imports like "from src.app.main import app"
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# 8. Expose port 8000 for FastAPI
EXPOSE 8000

# 9. Health check to ensure container is running properly
# Docker will periodically check if the app is responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/')" || exit 1

# 10. Run the FastAPI application with uvicorn
# --host 0.0.0.0: Listen on all network interfaces (required for Docker)
# --port 8000: Port to serve the application
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]