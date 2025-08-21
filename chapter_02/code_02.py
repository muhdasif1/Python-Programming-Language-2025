# String Methods Demonstration in Python

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
