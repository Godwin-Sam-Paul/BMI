def calculate_bmi(weight, height):
    """Calculates the BMI (Body Mass Index) of a person."""
    if height > 2.4384 or height < 0:
        raise ValueError("Invalid height")
    if weight > 200 or weight < 0:
        raise ValueError("Invalid weight")
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    """Categorizes the BMI based on predefined categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)
print("You are:", categorize_bmi(bmi))
