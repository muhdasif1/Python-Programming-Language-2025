# ========================================
# Python Membership Operators
# ========================================

# Create a list
fruits = ["apple", "banana", "cherry"]

# Membership operator: in
print("'apple' in fruits:", 'apple' in fruits)     # True, 'apple' exists in the list
print("'mango' in fruits:", 'mango' in fruits)     # False, 'mango' does not exist

# Membership operator: not in
print("'mango' not in fruits:", 'mango' not in fruits)  # True, 'mango' is not in the list
print("'banana' not in fruits:", 'banana' not in fruits) # False, 'banana' is in the list

# Membership operator with a string
text = "Hello Python"

print("'Python' in text:", 'Python' in text)       # True
print("'Java' not in text:", 'Java' not in text)   # True

# Membership operator with a tuple
numbers = (1, 2, 3, 4, 5)
print("3 in numbers:", 3 in numbers)             # True
print("6 not in numbers:", 6 not in numbers)     # True
