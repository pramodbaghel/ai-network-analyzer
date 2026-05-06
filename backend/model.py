# model.py

import joblib

# Load trained model
def load_model():
    return joblib.load("model.pkl")


# Predict function
def predict_usage(model, usage, devices):
    result = model.predict([[usage, devices]])[0]

    if result == 1:
        return "⚠️ Abnormal Usage"
    else:
        return "✅ Normal"