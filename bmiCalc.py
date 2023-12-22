def calculate_bmi(weight, height):
    """Calculates the BMI (Body Mass Index) of a person."""
    
    bmi = weight / (height ** 2)
    return bmi, categorize_bmi(bmi)

def categorize_bmi(bmi):
    """Categorizes the BMI based on predefined categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"
