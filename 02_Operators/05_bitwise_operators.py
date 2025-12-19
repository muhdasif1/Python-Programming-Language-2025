# ========================================
# Python Bitwise Operators
# ========================================

# Declare two numbers
a = 5   # binary: 0101
b = 3   # binary: 0011

# Bitwise AND (&)
print("a & b =", a & b)  # 0101 & 0011 = 0001 -> 1

# Bitwise OR (|)
print("a | b =", a | b)  # 0101 | 0011 = 0111 -> 7

# Bitwise XOR (^)
print("a ^ b =", a ^ b)  # 0101 ^ 0011 = 0110 -> 6

# Bitwise NOT (~)
print("~a =", ~a)        # ~0101 = -(0101+1) = -6

# Left Shift (<<)
print("a << 1 =", a << 1) # 0101 << 1 = 1010 -> 10

# Right Shift (>>)
print("a >> 1 =", a >> 1) # 0101 >> 1 = 0010 -> 2
