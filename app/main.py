from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from typing import List
import joblib
import numpy as np
import os

app = FastAPI()

# ✅ Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, "model", "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.pkl"))

# ✅ Templates (for HTML UI)
templates = Jinja2Templates(directory="app/templates")

# ✅ Home route (opens UI)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
# ✅ Prediction API (used by JavaScript)
@app.post("/predict")
def predict(data: List[float]):

    # Convert input to numpy array
    input_data = np.array(data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    return {"prediction": int(prediction)}