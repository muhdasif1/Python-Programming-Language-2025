# Variables
number1: int = 10
number2: int = 5

# --- Arithmetic Operations ---
print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)
print("Modulus:", number1 % number2)
print("Floor Division:", number1 // number2)
print("Exponentiation:", number1 ** number2)
print()

# --- Dictionary storing results ---
calculation_1: dict = {
    'Addition': number1 + number2,
    'Subtraction': number1 - number2,
    'Multiplication': number1 * number2,
    'Division': number1 / number2,
    'Modulus': number1 % number2,
    'Floor Division': number1 // number2,
    'Exponentiation': number1 ** number2
}

print(calculation_1, type(calculation_1))
print()

# --- List storing results ---
calculation_2: list = [
    "Addition", number1 + number2,
    "Subtraction", number1 - number2,
    "Multiplication", number1 * number2,
    "Division", number1 / number2,
    "Modulus", number1 % number2,
    "Floor Division", number1 // number2,
    "Exponentiation", number1 ** number2
]

print(calculation_2, type(calculation_2))
print()

# --- f-String Printing + Type Display ---
operations = [
    ("Addition", number1 + number2),
    ("Subtraction", number1 - number2),
    ("Multiplication", number1 * number2),
    ("Division", number1 / number2),
    ("Modulus", number1 % number2),
    ("Floor Division", number1 // number2),
    ("Exponentiation", number1 ** number2)
]

for name, result in operations:
    print(f"{name}: {result} (Type: {type(result)})")
print()

# --- Storing results in variables ---
addition_result: int = number1 + number2
subtraction_result: int = number1 - number2
multiplication_result: int = number1 * number2
division_result: float = number1 / number2
modulus_result: int = number1 % number2
floor_division_result: int = number1 // number2
exponentiation_result: int = number1 ** number2

# --- Printing stored results ---
print("Addition Result:", addition_result)
print("Subtraction Result:", subtraction_result)
print("Multiplication Result:", multiplication_result)
print("Division Result:", division_result)
print("Modulus Result:", modulus_result)
print("Floor Division Result:", floor_division_result)
print("Exponentiation Result:", exponentiation_result)
print()

# --- Formatted output with types ---
print(f"Addition Result: {addition_result} (Type: {type(addition_result)})")
print(f"Subtraction Result: {subtraction_result} (Type: {type(subtraction_result)})")
print(f"Multiplication Result: {multiplication_result} (Type: {type(multiplication_result)})")
print(f"Division Result: {division_result} (Type: {type(division_result)})")
print(f"Modulus Result: {modulus_result} (Type: {type(modulus_result)})")
print(f"Floor Division Result: {floor_division_result} (Type: {type(floor_division_result)})")
print(f"Exponentiation Result: {exponentiation_result} (Type: {type(exponentiation_result)})")
print()
print("End of Arithmetic Operations Demonstration")
print("--------------------------------------------------")
print()


print("********** Assignment Operators ************")
number1 : int = 44
number1+=6
print("Add and assign += : ", number1)

number2 : int = 50
number2 -=10
print("Subtract and assign -= : ",number2)
number3 : int = 60
number3 *=2
print("Multiply and assign *= : ",number3)

number4 : int = 80
number4 /=4
print("Divide and assign /= : ",number4)

number5 : int = 60
number5 %=5
print("Modulus and assign %= : ",number5)

number6 :int = 80
number6 **=2
print("Exponent and assign **= : ",number6)

number7 : int = 90
number7 //=3
print("Floor division and assign //= : ",number7)
print("--------------------------------------------------")
print()


print("********** Comparison Operators ************")
a : int = 10
b : int = 20
print("a == b : ",a==b)
print("a != b : ",a!=b)
print("a > b : ",a>b)           
print("a < b : ",a<b)
print("a >= b : ",a>=b)
print("a <= b : ",a<=b)
print("--------------------------------------------------")
print()

print("********** Comparison Operators ************")
name1 : str = "Muhammad Asif"
name2 : str = "Muhammad Asif"
print("name1 is name2 :", name1 == name2)
print("name1 is not name2 :", name1 != name2)

age : int = 25
age2 : int = 30
print("age 25 is age2 30 :",age > age2)
print("age 25 is not age2 30 :",age < age2)
print("age 25 is age2 30 :",age >= age2)
print("age 25 is not age2 30 :",age <= age2)
print("--------------------------------------------------")
print()

print("********** Logical Operators ************")
x : int = 10
y : int = 20
z : int = 30
print("x < y and y < z :", x < y and y < z)
print("x < y or y > z :", x < y or y > z)
print("not(x < y) :", not(x < y))
print("--------------------------------------------------")
print()

print("********** Bitwise Operators ************")
p : int = 5      # Binary: 0101
q : int = 3      # Binary: 0011
print("p & q (AND) :", p & q)   # Binary: 0001 -> Decimal: 1
print("p | q (OR)  :", p | q)   # Binary:
print("p ^ q (XOR) :", p ^ q)   # Binary: 0110 -> Decimal: 6
print("~p (NOT)    :", ~p)      # Binary: 1010
print("p << 1 (Left Shift) :", p << 1)  # Binary: 1010 -> Decimal: 10
print("p >> 1 (Right Shift):", p >> 1)  # Binary
print("--------------------------------------------------")
print()

print("********** Membership Operators ************")
fruits : list = ["apple", "banana", "cherry"]
print("'banana' in fruits :", "banana" in fruits)
print("'grape' not in fruits :", "grape" not in fruits)
print("--------------------------------------------------")
print()

print("********** Identity Operators ************")
m : list = [1, 2, 3]
n : list = m
o : list = [1, 2, 3]
print("m is n :", m is n)
print("m is o :", m is o)
print("m is not o :", m is not o)
print("--------------------------------------------------")
print()
