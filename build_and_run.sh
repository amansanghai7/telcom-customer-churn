#!/bin/bash
# ============================================================================
# Build and Run Script for Docker Container
# ============================================================================
# This script builds the Docker image and runs the container
# Usage: bash build_and_run.sh
# ============================================================================

echo "=============================================="
echo "🐳 Building Docker Image..."
echo "=============================================="

# Build the Docker image
docker build -t telco-churn-predictor:latest .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Docker image built successfully!"
    echo ""
    echo "=============================================="
    echo "🚀 Starting Container..."
    echo "=============================================="
    
    # Stop and remove existing container if it exists
    docker stop churn-predictor-app 2>/dev/null
    docker rm churn-predictor-app 2>/dev/null
    
    # Run the container
    docker run -d \
        --name churn-predictor-app \
        -p 8000:8000 \
        --restart unless-stopped \
        telco-churn-predictor:latest
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Container started successfully!"
        echo ""
        echo "=============================================="
        echo "📍 Access Points:"
        echo "=============================================="
        echo "Gradio UI:       http://localhost:8000/ui"
        echo "API Docs:        http://localhost:8000/docs"
        echo "Health Check:    http://localhost:8000/"
        echo "=============================================="
        echo ""
        echo "📊 View logs: docker logs -f churn-predictor-app"
        echo "⏹️  Stop app:  docker stop churn-predictor-app"
        echo ""
    else
        echo "❌ Failed to start container"
        exit 1
    fi
else
    echo "❌ Failed to build Docker image"
    exit 1
fi
