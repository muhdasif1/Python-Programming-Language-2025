# Topic 1: Variables, Input & Simple Calculations

# 1. Personal Greeting

name = input("Enter your first name: ")
color = input("Enter your favorite color: ")
print("Hello " + name + "!")
print("Your favorite color is " + color + ".")

# 2. Age in Months

age = int(input("Enter your age in years: "))
months = age * 12
print("You are approximately", months, "months old!")

# 3. Weekly Pay Calculator

hours = float(input("Enter hours worked this week: "))
pay_rate = float(input("Enter your hourly pay rate: "))
total_earnings = hours * pay_rate
print("Your total weekly earnings are:", total_earnings)

# 4. Rectangle Area & Perimeter

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

# 5. Leftover Candy

candies = 21
children = 4
full_candies = candies // children
leftover_candies = candies % children
print("Each child gets:", full_candies, "candies")
print("Leftover candies:", leftover_candies)

#**************************************************************************************

# Topic 2: Logical Thinking & Comparisons

# 1. Voting Eligibility Check

age = int(input("Enter your age: "))
print(age >= 18)

# 2. Pass Mark Evaluator

score = int(input("Enter your exam score: "))
print(score >= 50)

# 3. Equal Numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(number1 == number2)

# 4. Even Number Validator

number = int(input("Enter an integer: "))
print(number % 2 == 0)

# 5. Teenager Range

age = int(input("Enter your age: "))
print(age >= 13 and age <= 19)

#**************************************************************************************

# Topic 3: Working with Lists

# 1. Favorite Colors List

colors = ["Red", "Green", "Blue"]
print(colors[0])
print(colors[-1])


# 2. Updating the Menu

foods = ["Pizza", "Burger", "Pasta"]
foods[1] = "Sandwich"
print(foods)


# 3. Adding to the Cart

items = ["Pen", "Notebook"]
new_item = input("Enter one more school item: ")
items.append(new_item)
print(items)

# 4. List Size Evaluation

numbers = [10, 20, 30, 40]
print(len(numbers) > 3)


# 5. First and Last Swapper

fruits = ["Apple", "Banana", "Cherry", "Date"]
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits)

#**************************************************************************************
