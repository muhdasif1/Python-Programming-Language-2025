# ==============================
# String Methods Demonstration in Python
# ==============================
name: str = "muhammad asif"
print("Original:", name)  # Print the original string

print("capitalize():", name.capitalize())     # Capitalize first letter
print("casefold():", name.casefold())         # Convert to lowercase (stronger than lower)
print("center(20, '*'):", name.center(20, '*'))  # Center string in width 20, pad with *
print("count('a'):", name.count('a'))         # Count occurrences of 'a'
print("encode():", name.encode())             # Encode string into bytes
print("endswith('if'):", name.endswith("if")) # Check if string ends with 'if'
print("expandtabs(4):", "muhammad\tasif".expandtabs(4))  # Replace tab with spaces
print("find('asif'):", name.find("asif"))     # Find index of 'asif' (-1 if not found)
print("format():", "My name is {}".format(name)) # Format string with placeholder
print("format_map():", "{first} {last}".format_map({"first": "Muhammad", "last": "Asif"})) # Format using dict
print("index('asif'):", name.index("asif"))   # Index of 'asif' (error if not found)
print("isalnum():", name.isalnum())           # Check if only letters/numbers
print("isalpha():", name.isalpha())           # Check if only letters
print("isascii():", name.isascii())           # Check if only ASCII characters
print("isdecimal():", "123".isdecimal())      # Check if string has only decimals
print("isdigit():", "123".isdigit())          # Check if string has only digits
print("isidentifier():", "myVar".isidentifier()) # Check if valid variable name
print("islower():", name.islower())           # Check if all lowercase
print("isnumeric():", "123".isnumeric())      # Check if numeric
print("isprintable():", name.isprintable())   # Check if all characters are printable
print("isspace():", "   ".isspace())          # Check if only spaces
print("istitle():", "Muhammad Asif".istitle()) # Check if in Title Case
print("isupper():", "ASIF".isupper())         # Check if all uppercase
print("join():", "-".join(["Muhammad", "Asif"])) # Join list with '-'
print("ljust(20, '-'):", name.ljust(20, '-')) # Left align, pad with '-'
print("lower():", name.lower())               # Convert to lowercase
print("lstrip():", "   asif   ".lstrip())     # Remove spaces from left
print("maketrans() + translate():", "abc".translate(str.maketrans("abc", "123"))) # Replace chars using map
print("partition(' '):", name.partition(" ")) # Split into 3 parts (before, sep, after)
print("removeprefix('muh'):", name.removeprefix("muh")) # Remove prefix if it matches
print("removesuffix('if'):", name.removesuffix("if"))   # Remove suffix if it matches
print("replace('asif','ali'):", name.replace("asif", "ali")) # Replace substring
print("rfind('a'):", name.rfind("a"))         # Find last index of 'a'
print("rindex('a'):", name.rindex("a"))       # Last index of 'a' (error if not found)
print("rjust(20, '-'):", name.rjust(20, '-')) # Right align, pad with '-'
print("rpartition(' '):", name.rpartition(" ")) # Partition from right
print("rsplit(' '):", name.rsplit(" "))       # Split from right side
print("rstrip():", "   asif   ".rstrip())     # Remove spaces from right
print("split(' '):", name.split(" "))         # Split into list by spaces
print("splitlines():", "line1\nline2".splitlines()) # Split string into lines
print("startswith('mu'):", name.startswith("mu")) # Check if starts with 'mu'
print("strip():", "   asif   ".strip())       # Remove spaces from both sides
print("swapcase():", "Muhammad Asif".swapcase()) # Swap upper <-> lower
print("title():", name.title())               # Capitalize each word
print("upper():", name.upper())               # Convert to uppercase
print("zfill(15):", name.zfill(15))           # Pad with leading zeros

print("--------------------------------")
# ==============================
# Number Methods Demonstration in Python
# ==============================


# Example integer and float values
num_int: int = 25
num_float: float = 25.5

print("Original Integer:", num_int)
print("Original Float:", num_float)

# Integer and Float Methods

# 1. as_integer_ratio() -> Returns a tuple (numerator, denominator) for a float
print("Float as_integer_ratio():", num_float.as_integer_ratio())  # (51, 2) because 25.5 = 51/2

# 2. bit_count() -> Count the number of ones in binary representation (int only)
print("Integer bit_count():", num_int.bit_count())  # Binary of 25 is 11001 → 3 ones

# 3. bit_length() -> Number of bits required to represent integer in binary
print("Integer bit_length():", num_int.bit_length())  # 25 in binary is 11001 (5 bits)

# 4. conjugate() -> Returns the complex conjugate (works for complex/float/int)
print("Integer conjugate():", num_int.conjugate())   # For int, returns itself (25)
print("Float conjugate():", num_float.conjugate())   # For float, returns itself (25.5)
print("Complex conjugate():", (3+4j).conjugate())    # For complex, returns 3-4j

# 5. denominator -> Denominator of float when expressed as Fraction
print("Float denominator:", num_float.as_integer_ratio()[1])  # Denominator is 2

# 6. from_bytes() -> Convert bytes to integer
print("Integer from_bytes():", int.from_bytes(b'\x19', byteorder='big'))  # b'\x19' = 25

# 7. imag -> Imaginary part (works for float/int/complex)
print("Integer imag:", num_int.imag)     # 0 (int has no imaginary part)
print("Float imag:", num_float.imag)     # 0.0
print("Complex imag:", (3+4j).imag)      # 4.0

# 8. is_integer() -> Check if float is whole number
print("Float is_integer():", num_float.is_integer())     # False (25.5 not whole)
print("Float is_integer() 26.0:", (26.0).is_integer())   # True (26.0 is whole)

# 9. numerator -> Numerator of float when expressed as Fraction
print("Float numerator:", num_float.as_integer_ratio()[0])  # Numerator is 51

# 10. real -> Real part (works for int/float/complex)
print("Integer real:", num_int.real)     # 25
print("Float real:", num_float.real)     # 25.5
print("Complex real:", (3+4j).real)      # 3.0

# 11. to_bytes() -> Convert integer to bytes
print("Integer to_bytes():", num_int.to_bytes(2, byteorder='big'))  # 25 -> b'\x00\x19'

print("--------------------------------")

# ==============================
# LIST METHODS DEMONSTRATION
# ==============================

fruits = ["apple", "banana", "cherry", "apple"]

print("Original List:", fruits)

print("append():", fruits + ["orange"])       # Add element at the end
print("count('apple'):", fruits.count("apple"))  # Count occurrences
print("extend():", fruits + ["mango", "grapes"]) # Extend list
print("index('banana'):", fruits.index("banana")) # Find index
fruits.insert(1, "kiwi")  
print("insert(1,'kiwi'):", fruits)            # Insert at position
fruits.remove("apple")  
print("remove('apple'):", fruits)             # Remove first match
popped = fruits.pop()  
print("pop():", popped, fruits)               # Remove and return last item
fruits.reverse()  
print("reverse():", fruits)                   # Reverse list order
fruits.sort()  
print("sort():", fruits)                      # Sort list alphabetically
fruits.clear()  
print("clear():", fruits)                     # Remove all elements


# ==============================
# TUPLE METHODS DEMONSTRATION
# ==============================

numbers = (1, 2, 3, 1, 4, 1)

print("\nOriginal Tuple:", numbers)
print("count(1):", numbers.count(1))  # Count occurrences of 1
print("index(3):", numbers.index(3))  # Find index of 3


# ==============================
# SET METHODS DEMONSTRATION
# ==============================

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nOriginal Sets:", set1, set2)
set1.add(6)  
print("add(6):", set1)                   # Add element
set1.update([7, 8])  
print("update([7,8]):", set1)            # Add multiple elements
set1.remove(6)  
print("remove(6):", set1)                # Remove element (error if missing)
set1.discard(10)  
print("discard(10):", set1)              # Remove element (no error if missing)
print("union:", set1.union(set2))        # Combine sets
print("intersection:", set1.intersection(set2))  # Common elements
print("difference:", set1.difference(set2))      # Elements in set1 not in set2
print("symmetric_difference:", set1.symmetric_difference(set2)) # Unique to both


# ==============================
# DICTIONARY METHODS DEMONSTRATION
# ==============================

person = {"name": "Asif", "age": 20, "city": "Karachi"}

print("\nOriginal Dictionary:", person)
print("keys():", person.keys())          # Get all keys
print("values():", person.values())      # Get all values
print("items():", person.items())        # Get key-value pairs
print("get('name'):", person.get("name"))# Get value safely
person.update({"age": 21})  
print("update({'age':21}):", person)     # Update key value
person["country"] = "Pakistan"  
print("Add new key:", person)            # Add new key-value
removed = person.pop("city")  
print("pop('city'):", removed, person)   # Remove by key
last = person.popitem()  
print("popitem():", last, person)        # Remove last inserted
person.clear()  
print("clear():", person)                # Empty dictionary
