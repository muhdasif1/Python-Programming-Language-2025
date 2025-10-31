# Python Data Types Examples

# 1️ Numeric Types
integer_num = 10
float_num = 3.14
complex_num = 2 + 3j

print("Numeric Types:")
print("int:", integer_num)
print("float:", float_num)
print("complex:", complex_num)
print()

# 2️ String Type
text = "Hello, Python!"
print("String Type:")
print("str:", text)
print()

# 3️ Boolean Type
is_python_fun = True
is_boring = False
print("Boolean Type:")
print("bool:", is_python_fun, is_boring)
print()

# 4️ Sequence Types
numbers_list = [1, 2, 3, 'hi']
numbers_tuple = (4, 5, 6)
numbers_range = range(5)

print("Sequence Types:")
print("list:", numbers_list)
print("tuple:", numbers_tuple)
print("range:", list(numbers_range))  # Convert range to list for display
print()

# 5️ Mapping Type
person = {"name": "Asif", "age": 16}
print("Mapping Type:")
print("dict:", person)
print()

# 6️ Set Types
unique_numbers = {1, 2, 3, 3, 2}
frozen_numbers = frozenset({4, 5, 6})
print("Set Types:")
print("set:", unique_numbers)
print("frozenset:", frozen_numbers)
print()

# 7 Binary Types
byte_data = b"Hello"
byte_array_data = bytearray(5)
memory_view_data = memoryview(bytes(5))

print("Binary Types:")
print("bytes:", byte_data)
print("bytearray:", byte_array_data)
print("memoryview:", memory_view_data)
