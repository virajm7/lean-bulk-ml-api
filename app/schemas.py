from pydantic import BaseModel

class UserInput(BaseModel):
    age: int
    gender: int          # 1 = Male, 0 = Female
    height_cm: float
    weight_kg: float
    workout_hours: float
    activity_level: int  # 0 = low, 1 = medium, 2 = high


class PredictionOutput(BaseModel):
    protein_g: float
    calories_kcal: float
    fat_loss_rate_kg_per_week: float
