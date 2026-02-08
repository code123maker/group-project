import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import joblib
import os

# ---------------- LOAD DATA ----------------
df = pd.read_csv("DATA/Data.csv")

# ---------------- CLEAN CATEGORICAL DATA ----------------
# Normalize smoking_history
df["smoking_history"] = df["smoking_history"].replace(
    ["No Info", "no info", "Unknown", ""],
    "never"
)

smoking_map = {
    "never": 0,
    "former": 1,
    "current": 2
}
df["smoking_history"] = df["smoking_history"].map(smoking_map)

# ---------------- SELECT FEATURES ----------------
features = [
    "age",
    "bmi",
    "HbA1c_level",
    "blood_glucose_level",
    "hypertension",
    "heart_disease",
    "smoking_history"
]

X = df[features]
y = df["diabetes"]  # target (0/1)

# ---------------- HANDLE MISSING VALUES ----------------
# Impute missing values with median (medical standard)
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# ---------------- SPLIT DATA ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- SCALE ----------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------- TRAIN MODEL ----------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ---------------- EVALUATE ----------------
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Diabetes Model Accuracy: {accuracy:.2f}")

# ---------------- SAVE ARTIFACTS ----------------
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/diabetes_model.pkl")
joblib.dump(scaler, "models/diabetes_scaler.pkl")
joblib.dump(imputer, "models/diabetes_imputer.pkl")

print("✅ Model, scaler, and imputer saved successfully")
