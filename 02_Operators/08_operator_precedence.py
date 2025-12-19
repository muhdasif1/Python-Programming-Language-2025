# ========================================
# Python Operator Precedence Examples
# ========================================

# Example 1: Arithmetic precedence
result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)  # Multiplication before addition -> 2 + 12 = 14

# Example 2: Using parentheses to override precedence
result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)  # Parentheses first -> 5 * 4 = 20

# Example 3: Exponentiation precedence
result3 = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result3)  # Right-associative: 3**2=9 then 2**9=512

# Example 4: Combination of arithmetic and comparison
result4 = 10 + 3 > 12 - 4
print("10 + 3 > 12 - 4 ->", result4)  # 13 > 8 -> True

# Example 5: Logical operators precedence
a = True
b = False
c = False
result5 = a or b and c
print("a or b and c ->", result5)  
# AND has higher precedence than OR
# b and c -> False, then a or False -> True

# Example 6: Using parentheses to change logical precedence
result6 = (a or b) and c
print("(a or b) and c ->", result6)  
# Parentheses first: a or b -> True, then True and c -> False

# Example 7: Combined arithmetic, comparison, and logical
x = 5
y = 3
z = 2
result7 = x + y * z > 10 and z != 2
print("x + y * z > 10 and z != 2 ->", result7)
# Step by step:
# y * z = 6, x + 6 = 11
# 11 > 10 -> True
# z != 2 -> False
# True and False -> False
