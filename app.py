from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

app = FastAPI()

# Load your pre-trained pipeline
pipeline = joblib.load("diabetes_pipeline.pkl")

# Static files & templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    age: float = Form(...),
    height_cm: float = Form(...),
    weight_kg: float = Form(...),
    waist_cm: float = Form(...),
    hip_cm: float = Form(...),
    male: int = Form(...),
    fasting_glucose: float = Form(...),
    hdl_cholesterol: float = Form(...),
    hba1c: float = Form(...),
    systolic_bp: float = Form(...),
    diastolic_bp: float = Form(...)
):
    # Auto-calculate BMI and waist-to-hip ratio
    bmi = weight_kg / (height_cm / 100) ** 2
    waist_hip_ratio = waist_cm / hip_cm

    # Prepare input as DataFrame (pipeline expects column names)
    input_df = pd.DataFrame([{
        "fasting_glucose": fasting_glucose,
        "hdl_cholesterol": hdl_cholesterol,
        "hba1c": hba1c,
        "age": age,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "waist_cm": waist_cm,
        "hip_cm": hip_cm,
        "male": male,
        "bmi": bmi,
        "waist_hip_ratio": waist_hip_ratio
    }])

    # Predict probability
    prob = pipeline.predict_proba(input_df)[0][1]
    prob_percent = round(prob * 100, 2)

    # Friendly message + risk class for styling
    if prob_percent < 30:
        message = "Great! Your diabetes risk is low. Keep a healthy lifestyle!"
        risk_class = "low"
    elif prob_percent < 60:
        message = "Moderate risk. Consider monitoring your diet, exercise, and glucose."
        risk_class = "moderate"
    else:
        message = "High risk! Please consult your doctor for proper evaluation."
        risk_class = "high"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "probability": prob_percent,
            "message": message,
            "risk_class": risk_class
        }
    )
