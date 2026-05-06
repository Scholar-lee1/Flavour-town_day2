# BMI CALCULATOR
# 1. Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# 2. Calculate BMI
bmi = weight / (height ** 2)

# 3. Output the result
print(f"\n===== BMI RESULT =====")
print(f"Your calculated BMI is: {bmi:.2f}")
print("======================")