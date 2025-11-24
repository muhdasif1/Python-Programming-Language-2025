# 5. Identity Operators
print("\nIdentity Operators:\n")

a = 10
b = a
c = 15

print(f"a is b        --> {a is b}")
print(f"a is c        --> {a is c}")
print(f"a is not c    --> {a is not c}")
print("--------------------------------------------------")

number1 : int = 10
number2:int = number1
number3: int = 15
print("number1 is number2:", number1 is number2)
print("number1 is number3:", number1 is number3)
print("number1 is not number3:", number1 is not number3)
print("*******************************************************************")