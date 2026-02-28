def generate_personal_plan(user_data, final_color, diab_prob):

    diet_plan = []
    exercise_plan = []
    yoga_plan = []
    precautions = []

    age = user_data["age"]
    bmi = user_data["bmi"]
    hba1c = user_data["HbA1c_level"]
    glucose = user_data["blood_glucose_level"]
    hypertension = user_data["hypertension"]
    heart_disease = user_data["heart_disease"]
    smoking = user_data["smoking_history"]

    # ================= DIABETES BASED =================
    if hba1c >= 6.5 or glucose > 140:
        diet_plan += [
            "Low glycemic index foods (oats, quinoa, brown rice)",
            "Avoid refined sugar and sweet beverages",
            "Increase fiber intake (vegetables, legumes)"
        ]
        exercise_plan += [
            "30 min brisk walking daily",
            "Post-meal light walking (10–15 min)"
        ]
        yoga_plan += [
            "Surya Namaskar (5–7 rounds)",
            "Anulom Vilom (10 mins)"
        ]

    # ================= BMI BASED =================
    if bmi >= 30:
        diet_plan += [
            "Calorie deficit diet (500 kcal reduction)",
            "High protein intake for fat loss"
        ]
        exercise_plan += [
            "Strength training 3x per week",
            "Incline treadmill walking"
        ]

    # ================= HEART DISEASE =================
    if heart_disease == 1:
        diet_plan += [
            "Low sodium diet (<1500 mg/day)",
            "Avoid fried and processed food",
            "Omega-3 rich foods (fish, flax seeds)"
        ]
        exercise_plan = [
            "Low impact walking only (20–30 mins)",
            "Avoid high-intensity workouts"
        ]
        yoga_plan += [
            "Deep breathing exercises",
            "Shavasana relaxation"
        ]
        precautions.append("Avoid high-intensity exercise without medical clearance")

    # ================= HYPERTENSION =================
    if hypertension == 1:
        diet_plan += [
            "DASH diet recommended",
            "Reduce salt intake"
        ]
        yoga_plan += [
            "Bhramari Pranayama",
            "Meditation 15 mins daily"
        ]

    # ================= SMOKING =================
    if smoking != 0:
        precautions.append("Enroll in smoking cessation program")

    # ================= CRITICAL RISK =================
    if final_color == "Red" or diab_prob >= 75:
        precautions.append("Immediate medical consultation required")

    return {
        "diet": list(set(diet_plan)),
        "exercise": list(set(exercise_plan)),
        "yoga": list(set(yoga_plan)),
        "precautions": precautions
    }