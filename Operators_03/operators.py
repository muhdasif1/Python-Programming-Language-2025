# ============================================
#            PYTHON OPERATORS EXAMPLES
# ============================================

print("============================================")
print("1. ARITHMETIC OPERATORS")
print("============================================")

a : int = 10
b : int = 3

print("a + b :", a + b)      # Addition
print("a - b :", a - b)      # Subtraction
print("a * b :", a * b)      # Multiplication
print("a / b :", a / b)      # Division
print("a // b :", a // b)    # Floor Division
print("a % b :", a % b)      # Modulus
print("a ** b :", a ** b)    # Exponent


print("\n============================================")
print("2. COMPARISON OPERATORS")
print("============================================")

x : int = 10
y : int = 5
print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)


print("\n============================================")
print("3. LOGICAL OPERATORS")
print("============================================")

p = True
q = False

print("p and q :", p and q)
print("p or q  :", p or q)
print("not p   :", not p)


print("\n============================================")
print("4. ASSIGNMENT OPERATORS")
print("============================================")

num : int = 10

print("num =", num)

num += 5
print("num += 5 :", num)

num -= 3
print("num -= 3 :", num)

num *= 2
print("num *= 2 :", num)

num /= 4
print("num /= 4 :", num)

num %= 3
print("num %= 3 :", num)

num = 10
num //= 3
print("num //= 3 :", num)

num : int = 2
num **= 3
print("num **= 3 :", num)


print("\n============================================")
print("5. IDENTITY OPERATORS")
print("============================================")

list1 = [1, 2, 3]
list2 = list1

print("list1 is list2 :", list1 is list2)
print("list1 is not list2 :", list1 is not list2)


print("\n============================================")
print("6. MEMBERSHIP OPERATORS")
print("============================================")

my_list : list[int] = [10, 20, 30, 40]

print("20 in my_list :", 20 in my_list)
print("50 not in my_list :", 50 not in my_list)


print("\n============================================")
print("7. BITWISE OPERATORS")
print("============================================")

a : int = 5   # 0101
b : int = 3   # 0011
print("a & b :", a & b)   # AND
print("a | b :", a | b)   # OR
print("a ^ b :", a ^ b)   # XOR
print("~a    :", ~a)      # NOT
print("a << 1:", a << 1)  # Left shift
print("a >> 1:", a >> 1)  # Right shift
print("============================================")