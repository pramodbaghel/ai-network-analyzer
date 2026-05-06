# train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Input features
X = data[["usage", "devices"]]

# Output labels
y = data["label"]

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")