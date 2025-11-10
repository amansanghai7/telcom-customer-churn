@echo off
REM ============================================================================
REM Build and Run Script for Docker Container (Windows)
REM ============================================================================
REM This script builds the Docker image and runs the container
REM Usage: build_and_run.bat
REM ============================================================================

echo ==============================================
echo 🐳 Building Docker Image...
echo ==============================================
echo.

docker build -t telco-churn-predictor:latest .

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Docker image built successfully!
    echo.
    echo ==============================================
    echo 🚀 Starting Container...
    echo ==============================================
    echo.
    
    REM Stop and remove existing container if it exists
    docker stop churn-predictor-app 2>nul
    docker rm churn-predictor-app 2>nul
    
    REM Run the container
    docker run -d --name churn-predictor-app -p 8000:8000 --restart unless-stopped telco-churn-predictor:latest
    
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ✅ Container started successfully!
        echo.
        echo ==============================================
        echo 📍 Access Points:
        echo ==============================================
        echo Gradio UI:       http://localhost:8000/ui
        echo API Docs:        http://localhost:8000/docs
        echo Health Check:    http://localhost:8000/
        echo ==============================================
        echo.
        echo 📊 View logs: docker logs -f churn-predictor-app
        echo ⏹️  Stop app:  docker stop churn-predictor-app
        echo.
    ) else (
        echo ❌ Failed to start container
        exit /b 1
    )
) else (
    echo ❌ Failed to build Docker image
    exit /b 1
)
