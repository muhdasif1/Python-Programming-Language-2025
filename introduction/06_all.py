# ==============================
# Python Input and Output
# ==============================

# Simple Output
print("Hello, Python!")

# Input and Output (string)
name = input("Enter your name: ")
print("Hello", name)

# Input and Output (integer)
age = int(input("Enter your age: "))
print("Your age is:", age)

# Input and Output (float)
price = float(input("Enter price: "))
print("Price is:", price)

# Add Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# Using f-string
marks = float(input("Enter marks: "))
print(f"Name: {name}, Marks: {marks}")

# Multiple Outputs
x = 10
y = 5
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)


# ==============================
# Python Comments
# ==============================

# Single-line comment
# This is a comment

"""
Multi-line comment
This can span multiple lines
Used for explanation or documentation
"""


# ==============================
# Python Variables
# ==============================

# Variable declaration and assignment
name = "Asif"
age = 20
marks = 85.5
is_student = True

# Printing variables
print(name)
print(age)
print(marks)
print(is_student)

# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Same value to multiple variables
a = b = c = 100
print(a, b, c)

# Variable reassignment
age = 21
print(age)

# Variable with calculated value
total = x + y + z
print(total)


# ==============================
# Python Data Types
# ==============================

# Text Type
name = "Python"
print(name, type(name))  # <class 'str'>

# Numeric Types
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Sequence Types
fruits = ["apple", "banana", "mango"]  # list
colors = ("red", "green", "blue")      # tuple
numbers = range(1, 5)                  # range
print(fruits, type(fruits))
print(colors, type(colors))
print(list(numbers), type(numbers))  # range converted to list for display

# Mapping Type
student = {"name": "Asif", "age": 20}  # dict
print(student, type(student))

# Set Types
unique_numbers = {1, 2, 3}             # set
fs = frozenset([1, 2, 3])              # frozenset
print(unique_numbers, type(unique_numbers))
print(fs, type(fs))

# Boolean Type
is_active = True                       # bool
print(is_active, type(is_active))

# Binary Types
b = bytes(5)                           # bytes
ba = bytearray(5)                      # bytearray
mv = memoryview(bytes(5))              # memoryview
print(b, type(b))
print(ba, type(ba))
print(mv, type(mv))

# None Type
x = None
print(x, type(x))
