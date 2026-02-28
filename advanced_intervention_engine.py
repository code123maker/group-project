import math

def calculate_bmr(user_data):

    weight = user_data["bmi"] * (1.7 ** 2)  # approx if height 1.7m
    age = user_data["age"]
    gender = user_data["gender"]

    if gender == 1:  # male
        bmr = 10 * weight + 6.25 * 170 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * 170 - 5 * age - 161

    return round(bmr, 2)


def estimate_body_fat(user_data):

    bmi = user_data["bmi"]
    age = user_data["age"]
    gender = user_data["gender"]

    body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender) - 5.4
    return round(body_fat, 2)


def protein_target(weight, goal="fat_loss"):

    if goal == "fat_loss":
        return round(weight * 1.8, 1)
    return round(weight * 1.2, 1)


def generate_weekly_workout(final_color, heart_disease):

    if heart_disease == 1:
        return {
            "Mon": "30 min slow walking",
            "Tue": "Breathing exercises",
            "Wed": "Light yoga",
            "Thu": "30 min walking",
            "Fri": "Rest + stretching",
            "Sat": "Light yoga",
            "Sun": "Meditation"
        }

    if final_color == "Red":
        return {"Note": "Medical clearance required before exercise."}

    return {
        "Mon": "Strength training",
        "Tue": "Cardio 30 min",
        "Wed": "Yoga",
        "Thu": "Strength training",
        "Fri": "Cardio",
        "Sat": "Core workout",
        "Sun": "Active recovery"
    }


def ramadan_adjustment():

    return {
        "Suhoor": "High protein + slow carbs",
        "Iftar": "Break fast with dates + water",
        "Post-Iftar": "Light walk 20 min",
        "Hydration": "2.5–3L water between Iftar & Suhoor"
    }