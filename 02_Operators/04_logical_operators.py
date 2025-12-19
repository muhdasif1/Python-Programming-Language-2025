# ========================================
# Python Logical Operators
# ========================================

# Declare boolean variables
x = True
y = False

# Logical AND
print("x and y:", x and y)  # True only if both are True

# Logical OR
print("x or y:", x or y)    # True if at least one is True

# Logical NOT
print("not x:", not x)      # Reverses the boolean value
print("not y:", not y)      # Reverses the boolean value

# Using logical operators with comparison
a = 10
b = 5
c = 8

# Example: (a > b) and (a > c)
print("(a > b) and (a > c):", (a > b) and (a > c))  # True and True -> True

# Example: (a < b) or (a > c)
print("(a < b) or (a > c):", (a < b) or (a > c))    # False or True -> True

# Example: not(a > b)
print("not(a > b):", not(a > b))                    # not True -> False
