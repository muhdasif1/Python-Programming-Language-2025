# 🧮 BMI Calculator
# This program calculates a person's Body Mass Index (BMI)
# using their weight (kg) and height (meters).

# Step 1: Ask user for input
# Step 2: Calculate BMI
# BMI is equal to the person's weight divided by the person's height squared.
# Step 3: Display the result (rounded to 2 decimal places)
bmi = weight / (height * height)
print("Your BMI is:", round(bmi, 2))
# 🎯 Bonus Challenge: BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")