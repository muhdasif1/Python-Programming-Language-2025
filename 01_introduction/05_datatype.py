# Text Type
name = "Python"
print(name, type(name))  # Output: <class 'str'>

# Numeric Types
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Sequence Types
fruits = ["apple", "banana", "mango"]  # list
colors = ("red", "green", "blue")      # tuple
numbers = range(1, 5)                  # range
print(fruits, type(fruits))
print(colors, type(colors))
print(list(numbers), type(numbers))  # range converted to list for display

# Mapping Type
student = {"name": "Asif", "age": 20}  # dict
print(student, type(student))

# Set Types
unique_numbers = {1, 2, 3}             # set
fs = frozenset([1, 2, 3])              # frozenset
print(unique_numbers, type(unique_numbers))
print(fs, type(fs))

# Boolean Type
is_active = True                       # bool
print(is_active, type(is_active))

# Binary Types
b = bytes(5)                           # bytes
ba = bytearray(5)                      # bytearray
mv = memoryview(bytes(5))              # memoryview
print(b, type(b))
print(ba, type(ba))
print(mv, type(mv))

# None Type
x = None
print(x, type(x))
