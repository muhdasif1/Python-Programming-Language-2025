
print(" 1. Arithmetic Operators")
a = 10
b = 3
print("a + b =", a + b)       # Addition
print("a - b =", a - b)       # Subtraction
print("a * b =", a * b)       # Multiplication
print("a / b =", a / b)       # Division
print("a // b =", a // b)     # Floor Division
print("a % b =", a % b)       # Modulus
print("a ** b =", a ** b)     # Exponentiation

print("\n 2. Assignment Operators")
x = 5
print("x =", x)
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 4
print("x *= 4:", x)
x /= 3
print("x /= 3:", x)
x %= 2
print("x %= 2:", x)
x = 4
x **= 2
print("x **= 2:", x)
x //= 2
print("x //= 2:", x)

print("\n 3. Comparison Operators")
a = 7
b = 5
print("a == b:", a == b)     # Equal to
print("a != b:", a != b)     # Not equal to
print("a > b:", a > b)       # Greater than
print("a < b:", a < b)       # Less than
print("a >= b:", a >= b)     # Greater or equal
print("a <= b:", a <= b)     # Less or equal

print("\n 4. Logical Operators")
x = True
y = False
print("x and y:", x and y)   # AND
print("x or y:", x or y)     # OR
print("not x:", not x)       # NOT

print("\n 5. Identity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2:", list1 is list2)       # True
print("list1 is list3:", list1 is list3)       # False
print("list1 is not list3:", list1 is not list3)

print("\n 6. Membership Operators")
fruits = ['apple', 'banana', 'cherry']
print("'banana' in fruits:", 'banana' in fruits)
print("'mango' not in fruits:", 'mango' not in fruits)

print("\n 7. Bitwise Operators")
a = 5  # binary: 0101
b = 3  # binary: 0011
print("a & b =", a & b)      # AND: 0101 & 0011 = 0001 (1)
print("a | b =", a | b)      # OR: 0101 | 0011 = 0111 (7)
print("a ^ b =", a ^ b)      # XOR: 0101 ^ 0011 = 0110 (6)
print("~a =", ~a)            # NOT: ~0101 = -(0101 + 1) = -6
print("a << 1 =", a << 1)    # Left shift: 1010 (10)
print("a >> 1 =", a >> 1)    # Right shift: 0010 (2)