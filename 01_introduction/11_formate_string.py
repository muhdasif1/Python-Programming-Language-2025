"""
Python String Formatting - Complete Guide
This file demonstrates various methods to format strings in Python,
with focus on f-strings (the modern and preferred method).
"""

# ============================================================================
# 1. THE PROBLEM: CANNOT CONCATENATE STRINGS AND NUMBERS
# ============================================================================
# This will produce a TypeError because you cannot directly concatenate
# a string with a number using the + operator

age = 36

# This would cause an error (commented out to avoid breaking the code):
# txt = "My name is John, I am " + age  # TypeError: can only concatenate str to str
# print(txt)

# Solution: Convert number to string or use formatting methods
txt = "My name is John, I am " + str(age)  # Manual conversion
print("Using str() conversion:", txt)
print()


# ============================================================================
# 2. F-STRINGS - BASIC USAGE (PYTHON 3.6+)
# ============================================================================
# F-strings are the MODERN and PREFERRED way to format strings
# Syntax: f"text {variable} more text"
# Simply prefix the string with 'f' and use {} for placeholders

age = 36
txt = f"My name is John, I am {age}"
print("Basic f-string:", txt)  # Output: My name is John, I am 36
print()


# ============================================================================
# 3. F-STRINGS WITH MULTIPLE VARIABLES
# ============================================================================
# You can include multiple variables in a single f-string
# Each variable goes inside its own curly brackets {}

name = "John"
age = 36
city = "New York"
txt = f"My name is {name}, I am {age} years old, and I live in {city}."
print("Multiple variables:", txt)
print()


# ============================================================================
# 4. PLACEHOLDERS WITH MODIFIERS
# ============================================================================
# Modifiers format the value displayed in the placeholder
# Syntax: {variable:modifier}
# Common modifiers: .2f (2 decimal places), .3f (3 decimals), etc.

# Example 1: Simple price display
price = 59
txt = f"The price is {price} dollars"
print("Without modifier:", txt)  # Output: The price is 59 dollars
print()

# Example 2: Price with 2 decimal places
price = 59
txt = f"The price is {price:.2f} dollars"
print("With .2f modifier:", txt)  # Output: The price is 59.00 dollars
print()

# Example 3: More decimal examples
pi = 3.14159265359
print(f"Pi with 2 decimals: {pi:.2f}")  # Output: 3.14
print(f"Pi with 4 decimals: {pi:.4f}")  # Output: 3.1416
print(f"Pi with 6 decimals: {pi:.6f}")  # Output: 3.141593
print()


# ============================================================================
# 5. PYTHON CODE IN PLACEHOLDERS
# ============================================================================
# You can perform operations, calculations, and call functions
# directly inside the curly brackets {}

# Example 1: Math operations
txt = f"The price is {20 * 59} dollars"
print("Math in placeholder:", txt)  # Output: The price is 1180 dollars
print()

# Example 2: Multiple operations
quantity = 5
price_per_item = 25
total = f"Total cost: ${quantity * price_per_item}"
print(total)  # Output: Total cost: $125
print()

# Example 3: Using expressions
x = 10
y = 20
print(f"{x} + {y} = {x + y}")        # Output: 10 + 20 = 30
print(f"{x} * {y} = {x * y}")        # Output: 10 * 20 = 200
print(f"{y} / {x} = {y / x}")        # Output: 20 / 10 = 2.0
print()


# ============================================================================
# 6. CALLING FUNCTIONS IN F-STRINGS
# ============================================================================
# You can call functions directly inside f-string placeholders

name = "asif"
print(f"Uppercase: {name.upper()}")      # Output: Uppercase: ASIF
print(f"Capitalized: {name.capitalize()}")  # Output: Capitalized: Asif
print(f"Length: {len(name)}")            # Output: Length: 4
print()

# Using built-in functions
numbers = [10, 20, 30, 40, 50]
print(f"Sum: {sum(numbers)}")            # Output: Sum: 150
print(f"Max: {max(numbers)}")            # Output: Max: 50
print(f"Min: {min(numbers)}")            # Output: Min: 10
print()


# ============================================================================
# 7. ADVANCED F-STRING MODIFIERS
# ============================================================================

print("=" * 60)
print("ADVANCED F-STRING FORMATTING")
print("=" * 60)

# Number formatting
number = 1234567.89

print(f"Default: {number}")                    # 1234567.89
print(f"Comma separator: {number:,}")          # 1,234,567.89
print(f"Two decimals: {number:.2f}")           # 1234567.89
print(f"Comma + 2 decimals: {number:,.2f}")    # 1,234,567.89
print()

# Percentage formatting
score = 0.95
print(f"Percentage: {score:.2%}")              # 95.00%
print()

# Padding and alignment
text = "Python"
print(f"Left aligned: |{text:<10}|")           # |Python    |
print(f"Right aligned: |{text:>10}|")          # |    Python|
print(f"Center aligned: |{text:^10}|")         # |  Python  |
print()

# Number padding with zeros
number = 42
print(f"Padded with zeros: {number:05}")       # 00042
print()

# Scientific notation
large_number = 1500000
print(f"Scientific: {large_number:.2e}")       # 1.50e+06
print()


# ============================================================================
# 8. FORMAT() METHOD (ALTERNATIVE TO F-STRINGS)
# ============================================================================
# The format() method is an older way to format strings
# Still valid but f-strings are more readable and preferred

age = 36
txt = "My name is John, I am {}".format(age)
print("format() method:", txt)
print()

# Multiple placeholders
name = "John"
age = 36
txt = "My name is {}, I am {} years old".format(name, age)
print("Multiple placeholders:", txt)
print()

# Indexed placeholders
txt = "My name is {0}, I am {1} years old, {0} is my name".format(name, age)
print("Indexed placeholders:", txt)
print()

# Named placeholders
txt = "My name is {n}, I am {a} years old".format(n=name, a=age)
print("Named placeholders:", txt)
print()


# ============================================================================
# 9. PRACTICAL USE CASES
# ============================================================================

print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Creating a report
student_name = "Muhammad Asif"
math_score = 92
english_score = 88
science_score = 95
average = (math_score + english_score + science_score) / 3

report = f"""
Student Report Card
==================
Name: {student_name}
Math: {math_score}%
English: {english_score}%
Science: {science_score}%
Average: {average:.2f}%
"""
print(report)

# Example 2: Financial statement
balance = 15432.50
transaction = -250.75
new_balance = balance + transaction

statement = f"""
Account Statement
Previous Balance: ${balance:,.2f}
Transaction: ${transaction:,.2f}
New Balance: ${new_balance:,.2f}
"""
print(statement)

# Example 3: Product listing
product = "Laptop"
price = 899.99
discount = 0.15
final_price = price * (1 - discount)

listing = f"""
Product: {product}
Original Price: ${price:.2f}
Discount: {discount:.0%}
You Save: ${price * discount:.2f}
Final Price: ${final_price:.2f}
"""
print(listing)

# Example 4: Table formatting
print("Product Inventory")
print(f"{'Item':<15} {'Quantity':>10} {'Price':>10}")
print("-" * 37)
print(f"{'Laptop':<15} {10:>10} ${899.99:>9.2f}")
print(f"{'Mouse':<15} {50:>10} ${15.99:>9.2f}")
print(f"{'Keyboard':<15} {30:>10} ${45.50:>9.2f}")
print()


# ============================================================================
# 10. F-STRINGS VS OTHER METHODS COMPARISON
# ============================================================================

print("=" * 60)
print("COMPARISON: DIFFERENT FORMATTING METHODS")
print("=" * 60)

name = "Asif"
age = 25
salary = 50000.50

# Method 1: String concatenation (NOT RECOMMENDED)
result1 = "Name: " + name + ", Age: " + str(age) + ", Salary: $" + str(salary)
print("Concatenation:", result1)

# Method 2: % operator (OLD STYLE)
result2 = "Name: %s, Age: %d, Salary: $%.2f" % (name, age, salary)
print("%% operator:", result2)

# Method 3: format() method
result3 = "Name: {}, Age: {}, Salary: ${:.2f}".format(name, age, salary)
print("format():", result3)

# Method 4: f-strings (MODERN & RECOMMENDED)
result4 = f"Name: {name}, Age: {age}, Salary: ${salary:.2f}"
print("f-strings:", result4)

print()
print("RECOMMENDATION: Use f-strings for clean, readable code!")
print("=" * 60)
print()


# ============================================================================
# 11. FORMATTING REFERENCE GUIDE
# ============================================================================

print("=" * 60)
print("F-STRING FORMATTING QUICK REFERENCE")
print("=" * 60)
print(f"{'Format':<20} {'Example':<25} {'Description'}")
print("-" * 60)
print(f"{'{value}':<20} {'{age}':<25} Basic placeholder")
print(f"{'{value:.2f}':<20} {'{price:.2f}':<25} 2 decimal places")
print(f"{'{value:,}':<20} {'{number:,}':<25} Comma separator")
print(f"{'{value:.2%}':<20} {'{rate:.2%}':<25} Percentage")
print(f"{'{value:<10}':<20} {'{text:<10}':<25} Left align")
print(f"{'{value:>10}':<20} {'{text:>10}':<25} Right align")
print(f"{'{value:^10}':<20} {'{text:^10}':<25} Center align")
print(f"{'{value:05}':<20} {'{num:05}':<25} Zero padding")
print(f"{'{value:.2e}':<20} {'{big:.2e}':<25} Scientific notation")
print("=" * 60)