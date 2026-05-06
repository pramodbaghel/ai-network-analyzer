# app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time
from model import load_model, predict_usage

# Create app
app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = load_model()


# Generate realistic data (for demo)
def generate_data():
    devices = random.randint(1, 7)

    if devices <= 3:
        usage = random.randint(50, 350)
    else:
        usage = random.randint(80, 200)

    return usage, devices


@app.get("/data")
def get_data():
    usage, devices = generate_data()

    alert = predict_usage(model, usage, devices)

    return {
        "usage": usage,
        "devices": devices,
        "alert": alert,
        "time": int(time.time())
    }