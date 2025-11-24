# Membership Operator Examples

# List example
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)        # True
print("orange" in fruits)       # False
print("orange" not in fruits)   # True

print("********************************")

# String example
message = "Hello Python"

print("Python" in message)      # True
print("Java" not in message)    # True

print("********************************")

# Dictionary example (checks keys only)
student = {"name": "Ali", "age": 16}

print("name" in student)        # True
print("Ali" in student)         # False  # Because values are not checked
print("age" not in student)     # False
