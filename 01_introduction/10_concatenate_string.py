"""
Python String Concatenation - Complete Guide
This file demonstrates various methods to combine (concatenate) strings in Python.
"""

# ============================================================================
# 1. BASIC STRING CONCATENATION USING + OPERATOR
# ============================================================================
# The + operator joins two or more strings together
# This is the most straightforward method for combining strings

a = "Hello"
b = "World"
c = a + b
print("String a:", a)
print("String b:", b)
print("Concatenated (a + b):", c)  # Output: HelloWorld
print()


# ============================================================================
# 2. CONCATENATION WITH SPACE
# ============================================================================
# To add a space between concatenated strings, include a space string " "
# This prevents words from joining without separation

a = "Hello"
b = "World"
c = a + " " + b
print("String a:", a)
print("String b:", b)
print("With space (a + ' ' + b):", c)  # Output: Hello World
print()


# ============================================================================
# 3. CONCATENATING MULTIPLE STRINGS
# ============================================================================
# You can concatenate as many strings as needed using multiple + operators
# Useful for building longer sentences or phrases

first_name = "Muhammad"
middle_name = "Asif"
last_name = "Khan"
full_name = first_name + " " + middle_name + " " + last_name
print("Full name:", full_name)  # Output: Muhammad Asif Khan
print()


# ============================================================================
# 4. CONCATENATION WITH VARIABLES AND LITERALS
# ============================================================================
# You can mix variables and string literals (direct text in quotes)
# This is helpful for creating formatted messages

name = "Asif"
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Asif!
print()

age = "25"
message = "My name is " + name + " and I am " + age + " years old."
print(message)  # Output: My name is Asif and I am 25 years old.
print()


# ============================================================================
# 5. CONCATENATION IN LOOPS
# ============================================================================
# Building strings incrementally using concatenation
# Useful for generating dynamic content

result = ""
for i in range(1, 6):
    result = result + str(i) + " "
print("Numbers concatenated:", result)  # Output: 1 2 3 4 5
print()


# ============================================================================
# 6. USING JOIN() METHOD (MORE EFFICIENT)
# ============================================================================
# For concatenating multiple strings, join() is more efficient than +
# Syntax: separator.join(list_of_strings)
# This is the preferred method for combining many strings

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Using join():", sentence)  # Output: Python is awesome
print()

# Join with different separators
fruits = ["apple", "banana", "orange"]
print("Comma separated:", ", ".join(fruits))  # Output: apple, banana, orange
print("Dash separated:", "-".join(fruits))    # Output: apple-banana-orange
print("No separator:", "".join(fruits))       # Output: applebananaorange
print()


# ============================================================================
# 7. F-STRINGS (FORMATTED STRING LITERALS) - PYTHON 3.6+
# ============================================================================
# F-strings provide a clean and readable way to embed expressions
# Prefix the string with 'f' and use {} to include variables
# This is the MOST MODERN and RECOMMENDED approach

name = "Asif"
age = 25
city = "Karachi"

# Using f-strings
message = f"My name is {name}, I am {age} years old, and I live in {city}."
print("F-string:", message)
print()

# F-strings with expressions
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")  # Output: The sum of 10 and 20 is 30
print()


# ============================================================================
# 8. FORMAT() METHOD
# ============================================================================
# The format() method inserts values into placeholders {}
# This was the standard before f-strings were introduced

name = "Asif"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print("format() method:", message)
print()

# Named placeholders
message = "My name is {n} and I am {a} years old.".format(n=name, a=age)
print("Named placeholders:", message)
print()


# ============================================================================
# 9. % OPERATOR (OLD STYLE - LEGACY)
# ============================================================================
# The % operator is an older method for string formatting
# Still works but f-strings are preferred in modern Python

name = "Asif"
age = 25
message = "My name is %s and I am %d years old." % (name, age)
print("% operator:", message)
# %s = string, %d = integer, %f = float
print()


# ============================================================================
# 10. CONCATENATION WITH +=  OPERATOR
# ============================================================================
# The += operator appends to an existing string
# Shorthand for: variable = variable + new_string

text = "Hello"
print("Initial:", text)

text += " World"
print("After += ' World':", text)  # Output: Hello World

text += "!"
print("After += '!':", text)  # Output: Hello World!
print()


# ============================================================================
# 11. PRACTICAL USE CASES
# ============================================================================

# Example 1: Building a file path
folder = "documents"
subfolder = "reports"
filename = "sales_2024.pdf"
file_path = folder + "/" + subfolder + "/" + filename
print("File path:", file_path)  # Output: documents/reports/sales_2024.pdf
print()

# Example 2: Creating an email
username = "asif"
domain = "example.com"
email = username + "@" + domain
print("Email:", email)  # Output: asif@example.com
print()

# Example 3: Building a URL
base_url = "https://www.example.com"
page = "products"
product_id = "12345"
full_url = base_url + "/" + page + "/" + product_id
print("URL:", full_url)  # Output: https://www.example.com/products/12345
print()

# Example 4: Creating a CSV line
name = "John Doe"
age = "30"
city = "New York"
csv_line = name + "," + age + "," + city
print("CSV:", csv_line)  # Output: John Doe,30,New York
print()

# Example 5: Building SQL query (use with caution - prefer parameterized queries)
table = "users"
username = "admin"
query = "SELECT * FROM " + table + " WHERE username = '" + username + "'"
print("Query:", query)
print()


# ============================================================================
# 12. PERFORMANCE COMPARISON
# ============================================================================
# Different concatenation methods have different performance characteristics

print("=" * 60)
print("CONCATENATION METHODS - BEST PRACTICES")
print("=" * 60)
print("1. For 2-3 strings: Use + operator")
print("   Example: first + ' ' + last")
print()
print("2. For many strings: Use join()")
print("   Example: ' '.join([str1, str2, str3, ...])")
print()
print("3. For formatted output: Use f-strings")
print("   Example: f'Name: {name}, Age: {age}'")
print()
print("4. Avoid concatenation in loops (use join instead)")
print("=" * 60)
print()


# ============================================================================
# 13. IMPORTANT NOTES ABOUT STRING CONCATENATION
# ============================================================================

# Note 1: Strings are immutable - each concatenation creates a new string
original = "Hello"
original_id = id(original)
original = original + " World"
new_id = id(original)
print("String immutability demonstration:")
print(f"Original memory address: {original_id}")
print(f"New memory address: {new_id}")
print("Different addresses mean a new string was created")
print()

# Note 2: Cannot concatenate string with non-string types directly
# This will cause an error: "Hello" + 123
# Must convert to string first
number = 123
text = "Number: " + str(number)  # Convert number to string first
print("String with number:", text)
print()

# Note 3: Using f-strings automatically converts types
number = 456
text = f"Number: {number}"  # No need for str() conversion
print("F-string auto-conversion:", text)
print()


# ============================================================================
# 14. CONCATENATION COMPARISON - ALL METHODS
# ============================================================================
print("=" * 60)
print("SAME OUTPUT, DIFFERENT METHODS")
print("=" * 60)

name = "Asif"
age = 25

# Method 1: + operator
result1 = "Name: " + name + ", Age: " + str(age)
print("+ operator:  ", result1)

# Method 2: join()
result2 = "".join(["Name: ", name, ", Age: ", str(age)])
print("join():      ", result2)

# Method 3: f-string
result3 = f"Name: {name}, Age: {age}"
print("f-string:    ", result3)

# Method 4: format()
result4 = "Name: {}, Age: {}".format(name, age)
print("format():    ", result4)

# Method 5: % operator
result5 = "Name: %s, Age: %d" % (name, age)
print("%% operator: ", result5)

print("=" * 60)
print("RECOMMENDATION: Use f-strings for modern Python code!")