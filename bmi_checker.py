weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))
bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Category: Healthy weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
