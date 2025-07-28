# 1. IF Statement
age = 20
print("1. IF Statement")
if age >= 18:
    print("You are an adult")  # Runs because 20 >= 18
print()

# 2. IF-ELSE Statement
age = 16
print("2. IF-ELSE Statement")
if age >= 18:
    print("Adult")
else:
    print("Minor")  # Runs because 16 < 18
print()

# 3. IF-ELIF-ELSE Statement
marks = 75
print("3. IF-ELIF-ELSE Statement")
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")  # Runs because 75 >= 70
else:
    print("Fail")
print()

# 4. Nested IF Statement
number = 15
print("4. Nested IF Statement")
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")  # Runs because 15 is odd
else:
    print("Not positive")
print()

# 5. Ternary Operator (Short IF-ELSE)
age = 22
print("5. Ternary Operator")
status = "Adult" if age >= 18 else "Minor"
print("You are:", status)  # Output: Adult
print()

# 6. Checking Even or Odd with IF-ELSE
num = 7
print("6. Even or Odd Check")
if num % 2 == 0:
    print("Even")
else:
    print("Odd")  # Output: Odd
print()

# 7. Comparing Two Numbers
a = 10
b = 20
print("7. Comparing Two Numbers")
if a > b:
    print("a is greater")
elif a < b:
    print("b is greater")  # Output
else:
    print("Both are equal")
print()

# 8. Multiple Conditions using AND / OR
x = 5
print("8. Using AND / OR")
if x > 0 and x < 10:
    print("x is a positive single-digit number")  # Runs
if x < 0 or x > 100:
    print("x is out of range")
else:
    print("x is within normal range")
