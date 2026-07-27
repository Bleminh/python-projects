def bmi_calculator():
    system = input("1. Metric/2. Imperial. Please enter your unit system (1, 2): ")
    if (system == "1"):
        weight = input("Enter your weight in kilogram: ")
        height = input("Enter your height in meter: ")
        bmi = float(weight) / (float(height) ** 2)
    elif (system == "2"):
        weight = input("Enter your weight in pounds: ")
        height = input("Enter your height in inches: ")
        bmi = 703 * float(weight) / (float(height) ** 2)
    else:
        print("Unknown system!")
        return 0;
    if (bmi < 18.5):
        print(f"Your BMI is: {bmi}. You are underweight.")
    elif (18.5 <= bmi <= 24.9):
        print(f"Your BMI is: {bmi}. Your weight is healthy.")
    elif (25.0 <= bmi <= 29.9):
        print(f"Your BMI is: {bmi}. You are overweight.")
    else:
        print(f"Your BMI is: {bmi}. You are obese.")

bmi_calculator()