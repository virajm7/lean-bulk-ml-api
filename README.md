# Lean Bulk Nutrition ML API

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
