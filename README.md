## Data-Driven Protein Intake Prediction for Lean Bulking
## Overview

Most online protein calculators use static formulas and provide generic recommendations.
This project builds a machine learning–based nutrition prediction system that adapts protein and calorie recommendations based on individual body metrics and workout behavior, specifically for lean bulking.

The system is fully production-ready and deployed using FastAPI and Render.

## Problem Statement

Traditional nutrition calculators fail to account for variations in training intensity, activity level, and individual body composition. As a result, users with different workout patterns often receive similar protein recommendations.

This project addresses that gap by learning from data and generating personalized nutrition targets using machine learning, with measurable accuracy and explainability.

## Methodology
● Collected and generated a structured fitness dataset with body metrics and training
behavior.
● Performed feature engineering by encoding categorical variables and scaling numeric
inputs.
● Trained a Multiple Linear Regression model using a preprocessing pipeline.
● Applied cross-validation to ensure generalization and avoid overfitting.
● Evaluated the model using MAE, RMSE, and R2 metrics.
● Validated predictions using real-world inputs.
● Exported the trained model for production use.

## Lean Bulk Nutrition ML API

A FastAPI-based machine learning API that predicts personalized nutrition metrics for lean bulking.

## Features
- Protein intake prediction (g/day)
- Daily calorie requirement (kcal/day)
- Expected fat loss rate (kg/week)
- Data-driven predictions using Multiple Linear Regression
- Explainable and interpretable ML model

## Why Multiple Linear Regression?
The relationships between body metrics, training intensity, and nutrition requirements are continuous, interpretable, and largely linear.  
Multiple Linear Regression provides reliable predictions while maintaining full explainability, which is critical in health and fitness applications.

## Tech Stack
- Python
- scikit-learn
- FastAPI
- Joblib
- Render (Deployment)

## Project Structure
lean_bulk_api/
│
├── app/
│ ├── main.py
│ ├── schemas.py
│ └── model/
│ └── lean_bulk_multi_output_model.pkl
│
├── requirements.txt
├── render.yaml
└── README.md

## Deployment

The API is deployed on Render and can be accessed publicly for real-time predictions.

## Future Improvements

Add real user data

Include diet preferences

Add frontend dashboard

Try regularized regression (Ridge/Lasso)

## Author

Viraj Mhadgut
MSc Data Science
