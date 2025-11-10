"""
LOCAL INFERENCE - For Quick Testing Without Docker
"""
import os
import pandas as pd
import mlflow
import glob

# === LOCAL MODEL LOADING ===
print("🔍 Looking for trained model...")

# Try to load from MLflow models registry
model_paths = glob.glob("./mlruns/*/models/*/artifacts")
if model_paths:
    # Get the most recent model
    latest_model_dir = max(model_paths, key=os.path.getmtime)
    MODEL_DIR = latest_model_dir
    print(f"📦 Found model at: {MODEL_DIR}")
else:
    raise Exception("❌ No trained model found. Please run scripts/run_pipeline.py first!")

try:
    model = mlflow.pyfunc.load_model(MODEL_DIR)
    print(f"✅ Model loaded successfully!")
except Exception as e:
    raise Exception(f"❌ Failed to load model: {e}")

# Load feature columns
try:
    feature_file = os.path.join("artifacts", "feature_columns.json")
    import json
    with open(feature_file) as f:
        FEATURE_COLS = json.load(f)
    print(f"✅ Loaded {len(FEATURE_COLS)} feature columns")
except Exception as e:
    raise Exception(f"❌ Failed to load feature columns: {e}")

# === FEATURE TRANSFORMATION ===
BINARY_MAP = {
    "gender": {"Female": 0, "Male": 1},
    "Partner": {"No": 0, "Yes": 1},
    "Dependents": {"No": 0, "Yes": 1},
    "PhoneService": {"No": 0, "Yes": 1},
    "PaperlessBilling": {"No": 0, "Yes": 1},
}

NUMERIC_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]

def _serve_transform(df: pd.DataFrame) -> pd.DataFrame:
    """Apply same transformations as training"""
    df = df.copy()
    df.columns = df.columns.str.strip()
    
    # Numeric conversion
    for c in NUMERIC_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    
    # Binary encoding
    for c, mapping in BINARY_MAP.items():
        if c in df.columns:
            df[c] = (
                df[c].astype(str).str.strip()
                .map(mapping).astype("Int64")
                .fillna(0).astype(int)
            )
    
    # One-hot encoding
    obj_cols = [c for c in df.select_dtypes(include=["object"]).columns]
    if obj_cols:
        df = pd.get_dummies(df, columns=obj_cols, drop_first=True)
    
    # Boolean to int
    bool_cols = df.select_dtypes(include=["bool"]).columns
    if len(bool_cols) > 0:
        df[bool_cols] = df[bool_cols].astype(int)
    
    # Align with training features
    df = df.reindex(columns=FEATURE_COLS, fill_value=0)
    
    return df

def predict(input_dict: dict) -> str:
    """Make prediction from customer data"""
    df = pd.DataFrame([input_dict])
    df_enc = _serve_transform(df)
    
    try:
        preds = model.predict(df_enc)
        if hasattr(preds, "tolist"):
            preds = preds.tolist()
        if isinstance(preds, (list, tuple)) and len(preds) == 1:
            result = preds[0]
        else:
            result = preds
    except Exception as e:
        raise Exception(f"Prediction failed: {e}")
    
    return "Likely to churn" if result == 1 else "Not likely to churn"
