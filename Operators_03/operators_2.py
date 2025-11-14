# 1: Arithmetic operators 
number1: int = 10
number2: int = 5
addition: int = number1 + number2
print("Addition:", addition)
subtraction: int = number1 - number2
print("Subtraction:", subtraction)
multiplication: int = number1 * number2
print("Multiplication:", multiplication)
division: float = number1 / number2
print("Division:", division)
modulus: int = number1 % number2
print("Modulus:", modulus)
exponentiation: int = number1 ** number2
print("Exponentiation:", exponentiation)
floor_division: int = number1 // number2
print("Floor Division:", floor_division)

# 2: Comparison operators
is_equal: bool = (number1 == number2)
print("Is Equal:", is_equal)
is_not_equal: bool = (number1 != number2)
print("Is Not Equal:", is_not_equal)
is_greater: bool = (number1 > number2)
print("Is Greater:", is_greater)
is_less: bool = (number1 < number2)
print("Is Less:", is_less)
is_greater_equal: bool = (number1 >= number2)
print("Is Greater or Equal:", is_greater_equal)
is_less_equal: bool = (number1 <= number2)
print("Is Less or Equal:", is_less_equal)

# 3: Logical operators
and_result: bool = (number1 > 0 and number2 > 0)
print("Logical AND:", and_result)
or_result: bool = (number1 > 0 or number2 < 0)
print("Logical OR:", or_result)
not_result: bool = not (number1 > number2)
print("Logical NOT:", not_result)

# 4: Assignment operators
a: int = 10
a += 5
print("After += :", a)
a -= 3
print("After -= :", a)
a *= 2
print("After *= :", a)
a /= 4
print("After /= :", a)
a %= 3
print("After %= :", a)

# 5: Bitwise operators
bitwise_and: int = number1 & number2
print("Bitwise AND:", bitwise_and)
bitwise_or: int = number1 | number2
print("Bitwise OR:", bitwise_or)
bitwise_xor: int = number1 ^ number2
print("Bitwise XOR:", bitwise_xor)
bitwise_not: int = ~number1
print("Bitwise NOT:", bitwise_not)
left_shift: int = number1 << 2
print("Left Shift:", left_shift)
right_shift: int = number1 >> 2
print("Right Shift:", right_shift)

# 6: Membership operators
my_list: list[int] = [1, 2, 3, 4, 5]
is_in: bool = 3 in my_list
print("Is 3 in list:", is_in)
is_not_in: bool = 6 not in my_list
print("Is 6 not in list:", is_not_in)

# 7: Identity operators
x: list[int] = [1, 2, 3]
y: list[int] = x
is_identical: bool = (x is y)
print("Is x identical to y:", is_identical)
is_not_identical: bool = (x is not [1, 2, 3])
print("Is x not identical to new list:", is_not_identical)
 