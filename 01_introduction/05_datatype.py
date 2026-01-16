# Text Type
name = "Python"
print(name, type(name))  # Output: <class 'str'>
print()

# Numeric Types
number1: int = 10          # int
number2: float = 3.14        # float
number3: complex = 2 + 3j      # complex
print(number1, type(number1))
print(number2, type(number2))
print(number3, type(number3))
print()

# Sequence Types
fruits: list = ["apple", "banana", "mango"]  # list
colors: tuple = ("red", "green", "blue")      # tuple
numbers: range = range(1, 5)                  # range
print(fruits, type(fruits))
print(colors, type(colors))
print(list(numbers), type(numbers))  # range converted to list for display
print()

# Mapping Type
student: dict = {"name": "Asif", "age": 20}  # dict
print(student, type(student))
print()

# Set Types
unique_numbers: set = {1, 2, 3}             # set
fs: frozenset = frozenset([1, 2, 3])              # frozenset
print(unique_numbers, type(unique_numbers))
print(fs, type(fs))
print()

# Boolean Type
is_active: bool = True                       # bool
print(is_active, type(is_active))
print()

# Binary Types
b: bytes = bytes(5)        # bytes
ba: bytearray = bytearray(5)                      # bytearray
mv: memoryview = memoryview(bytes(5))              # memoryview
print(b, type(b))
print(ba, type(ba))
print(mv, type(mv))
print()

# None Type
x: None = None
print(x, type(x))
