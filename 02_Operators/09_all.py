# ========================================
# FULL PYTHON OPERATORS DEMO
# ========================================

# ========================================
# 1. ARITHMETIC OPERATORS
# ========================================
print("=== Arithmetic Operators ===")
a = 10
b = 3

print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a // b =", a // b) # Floor division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation

print("\n")

# ========================================
# 2. ASSIGNMENT OPERATORS
# ========================================
print("=== Assignment Operators ===")
x = 5
print("Initial x =", x)

x += 3
print("x += 3 ->", x)

x -= 2
print("x -= 2 ->", x)

x *= 2
print("x *= 2 ->", x)

x /= 4
print("x /= 4 ->", x)

x //= 2
print("x //= 2 ->", x)

x %= 3
print("x %= 3 ->", x)

x **= 3
print("x **= 3 ->", x)

x &= 2
print("x &= 2 ->", x)

x |= 1
print("x |= 1 ->", x)

x ^= 3
print("x ^= 3 ->", x)

x <<= 2
print("x <<= 2 ->", x)

x >>= 1
print("x >>= 1 ->", x)

print("\n")

# ========================================
# 3. COMPARISON OPERATORS
# ========================================
print("=== Comparison Operators ===")
p = 10
q = 5

print("p == q ->", p == q)
print("p != q ->", p != q)
print("p > q ->", p > q)
print("p < q ->", p < q)
print("p >= q ->", p >= q)
print("p <= q ->", p <= q)

print("\n")

# ========================================
# 4. LOGICAL OPERATORS
# ========================================
print("=== Logical Operators ===")
x = True
y = False

print("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not x)

a = 10
b = 5
c = 8

print("(a > b) and (a > c) ->", (a > b) and (a > c))
print("(a < b) or (a > c) ->", (a < b) or (a > c))
print("not(a > b) ->", not(a > b))

print("\n")

# ========================================
# 5. BITWISE OPERATORS
# ========================================
print("=== Bitwise Operators ===")
a = 5   # 0101
b = 3   # 0011

print("a & b ->", a & b)
print("a | b ->", a | b)
print("a ^ b ->", a ^ b)
print("~a ->", ~a)
print("a << 1 ->", a << 1)
print("a >> 1 ->", a >> 1)

print("\n")

# ========================================
# 6. IDENTITY OPERATORS
# ========================================
print("=== Identity Operators ===")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 ->", list1 is list2)
print("list1 is list3 ->", list1 is list3)
print("list1 is not list3 ->", list1 is not list3)

x = 10
y = 10
z = 20

print("x is y ->", x is y)
print("x is z ->", x is z)
print("x is not z ->", x is not z)

print("\n")

# ========================================
# 7. MEMBERSHIP OPERATORS
# ========================================
print("=== Membership Operators ===")
fruits = ["apple", "banana", "cherry"]

print("'apple' in fruits ->", 'apple' in fruits)
print("'mango' in fruits ->", 'mango' in fruits)
print("'mango' not in fruits ->", 'mango' not in fruits)
print("'banana' not in fruits ->", 'banana' not in fruits)

text = "Hello Python"
print("'Python' in text ->", 'Python' in text)
print("'Java' not in text ->", 'Java' not in text)

numbers = (1, 2, 3, 4, 5)
print("3 in numbers ->", 3 in numbers)
print("6 not in numbers ->", 6 not in numbers)

print("\n")

# ========================================
# 8. OPERATOR PRECEDENCE EXAMPLES
# ========================================
print("=== Operator Precedence ===")

result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)

result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)

result3 = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result3)

result4 = 10 + 3 > 12 - 4
print("10 + 3 > 12 - 4 ->", result4)

a = True
b = False
c = False
result5 = a or b and c
print("a or b and c ->", result5)

result6 = (a or b) and c
print("(a or b) and c ->", result6)

x = 5
y = 3
z = 2
result7 = x + y * z > 10 and z != 2
print("x + y * z > 10 and z != 2 ->", result7)
