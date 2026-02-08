import joblib
import numpy as np

model = joblib.load("models/diabetes_model.pkl")
scaler = joblib.load("models/diabetes_scaler.pkl")

def predict_diabetes(user_data):
    """
    Returns:
    - prediction (0 or 1)
    - probability (0–100)
    """

    features = np.array([[
        user_data["age"],
        user_data["bmi"],
        user_data["HbA1c_level"],
        user_data["blood_glucose_level"],
        user_data["hypertension"],
        user_data["heart_disease"],
        user_data["smoking_history"]
    ]])

    features_scaled = scaler.transform(features)

    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1] * 100

    return int(pred), round(prob, 2)
