# Bitwise Operator Examples in Python

a: int = 10    # Binary: 1010
b: int = 4     # Binary: 0100

print("a =", a, "-> binary:", bin(a))
print("b =", b, "-> binary:", bin(b))
print("****************************************")

# 1. Bitwise AND (&)
print("a & b =", a & b)
print("Binary:", bin(a & b))
print("----------------------------------------")

# 2. Bitwise OR (|)
print("a | b =", a | b)
print("Binary:", bin(a | b))
print("----------------------------------------")

# 3. Bitwise XOR (^)
print("a ^ b =", a ^ b)
print("Binary:", bin(a ^ b))
print("----------------------------------------")

# 4. Bitwise NOT (~)
print("~a =", ~a)
print("Binary:", bin(~a))
print("----------------------------------------")

# 5. Left Shift (<<)
print("a << 1 =", a << 1)
print("Binary:", bin(a << 1))
print("----------------------------------------")

# 6. Right Shift (>>)
print("a >> 1 =", a >> 1)
print("Binary:", bin(a >> 1))
print("----------------------------------------")
print("********** End of Bitwise Operators Demonstration ************")