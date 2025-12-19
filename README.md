Data-Driven Protein Intake Prediction for Lean Bulking
Overview

Most online protein calculators use static formulas and provide generic recommendations.
This project builds a machine learning–based nutrition prediction system that adapts protein and calorie recommendations based on individual body metrics and workout behavior, specifically for lean bulking.

The system is fully production-ready and deployed using FastAPI and Render.

Problem Statement

Traditional nutrition calculators fail to account for variations in training intensity, activity level, and individual body composition. As a result, users with different workout patterns often receive similar protein recommendations.

This project addresses that gap by learning from data and generating personalized nutrition targets using machine learning, with measurable accuracy and explainability.

Machine Learning Approach

Algorithm: Multiple Linear Regression

Why this algorithm?

Nutritional requirements scale linearly with body metrics and training load

Highly interpretable coefficients

Stable and explainable predictions

Suitable for continuous outputs like protein and calories

Input Features

Age

Gender

Height (cm)

Weight (kg)

Workout hours per day

Activity level (low / medium / high)

Model Outputs

Daily protein intake (g/day)

Daily calorie intake (kcal/day)

Expected fat loss rate (kg/week)

Model Evaluation

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score and Adjusted R²

5-fold Cross Validation

The model achieved:

Protein R² ≈ 0.93

Calories R² ≈ 0.99

Stable cross-validation performance

Tech Stack

Python

Pandas, NumPy

Scikit-learn

FastAPI

Joblib

Render (Deployment)

API Usage
Endpoint
POST /predict

Request Body
{
  "age": 20,
  "gender": 1,
  "height_cm": 164,
  "weight_kg": 62.5,
  "workout_hours": 2.0,
  "activity_level": 2
}

Response
{
  "protein_g_per_day": 114.7,
  "calories_kcal_per_day": 2832,
  "fat_loss_rate_kg_per_week": 0.34
}

Deployment

The API is deployed on Render and can be accessed publicly for real-time predictions.

Future Improvements

Add real user data

Include diet preferences

Add frontend dashboard

Try regularized regression (Ridge/Lasso)

Author

Viraj Mhadgut
MSc Data Science