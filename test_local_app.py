"""
Quick test script to verify the local app works
"""
from src.serving.inference_local import predict

# Test data - high churn risk customer
test_customer = {
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

print("\n" + "="*60)
print("🧪 Testing Local Inference")
print("="*60)
print("\n📋 Test Customer Profile:")
print(f"   - Contract: {test_customer['Contract']}")
print(f"   - Internet: {test_customer['InternetService']}")
print(f"   - Tenure: {test_customer['tenure']} months")
print(f"   - Monthly Charges: ${test_customer['MonthlyCharges']}")

print("\n🔮 Making prediction...")
result = predict(test_customer)

print(f"\n✅ Prediction: {result}")
print("="*60)
print("\n✅ Local inference is working!")
print("\nYou can now run: python app_local.py")
print("="*60 + "\n")
