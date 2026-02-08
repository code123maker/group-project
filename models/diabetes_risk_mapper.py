def diabetes_to_risk(prediction, probability):
    """
    Maps diabetes ML output to risk category
    """

    if prediction == 1:
        return "Red"

    if probability >= 60:
        return "Orange"

    if probability >= 30:
        return "Yellow"

    return "Green"
