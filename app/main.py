from fastapi import FastAPI
import joblib
import pandas as pd

from app.schemas import UserInput, PredictionOutput

app = FastAPI(
    title="Lean Bulk Nutrition Prediction API",
    description="Predict protein intake, calories, and fat loss rate using ML",
    version="1.0"
)

# Load trained model
model = joblib.load("app/model/final2_lean_bulk_multi_output_model.pkl")


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: UserInput):
    input_df = pd.DataFrame([{
        "age": data.age,
        "gender": data.gender,
        "height_cm": data.height_cm,
        "weight_kg": data.weight_kg,
        "workout_hours": data.workout_hours,
        "activity_level": data.activity_level
    }])

    prediction = model.predict(input_df)[0]

    return {
        "protein_g": round(prediction[0], 1),
        "calories_kcal": round(prediction[1]),
        "fat_loss_rate_kg_per_week": round(prediction[2], 2)
    }
