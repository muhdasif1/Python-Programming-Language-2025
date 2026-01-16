"""
Python Strings - Complete Tutorial with Examples
This file demonstrates all fundamental string operations in Python.
"""

# ============================================================================
# 1. BASIC STRING CREATION
# Strings can be created using either single quotes ('') or double quotes ("")
# Both methods are equivalent in Python
# ============================================================================
 
print("Hello")  # Using double quotes
print('Hello')  # Using single quotes - produces same output
print()


# ============================================================================
# 2. QUOTES INSIDE QUOTES
# You can use quotes inside a string as long as they don't match 
# the surrounding quotes. This allows you to include apostrophes and quotes
# in your text without causing syntax errors
# ============================================================================

print("It's alright")              # Single quote (apostrophe) inside double quotes
print("He is called 'Johnny'")     # Single quotes inside double quotes
print('He is called "Johnny"')     # Double quotes inside single quotes
print()


# ============================================================================
# 3. ASSIGN STRING TO A VARIABLE
# You can store strings in variables using the assignment operator (=)
# This allows you to reuse the string throughout your code
# ============================================================================

a = "Hello"
print(a)  # Output: Hello
print()


# ============================================================================
# 4. MULTILINE STRINGS
# For strings that span multiple lines, use triple quotes (""" or ''')
# Line breaks in your code will appear in the actual string output
# ============================================================================

# Using triple double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print()

# Using triple single quotes (works the same way)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print()


# ============================================================================
# 5. STRINGS ARE ARRAYS
# In Python, strings are arrays of bytes representing unicode characters
# Python doesn't have a character data type - a single character is just
# a string with length 1
# You can access individual characters using square brackets [index]
# IMPORTANT: Index counting starts at 0, not 1
# ============================================================================

a = "Hello, World!"
print(a[1])  # Output: e (character at position 1, which is the 2nd character)
# Index positions: H=0, e=1, l=2, l=3, o=4, comma=5, space=6, W=7, etc.
print()


# ============================================================================
# 6. LOOPING THROUGH A STRING
# Since strings are arrays, you can iterate through each character
# using a for loop. This goes through each character one at a time
# ============================================================================

for x in "banana":
    print(x)  # Prints each letter on a new line: b, a, n, a, n, a
print()


# ============================================================================
# 7. STRING LENGTH
# The len() function returns the number of characters in a string
# This includes spaces, punctuation, and all characters
# ============================================================================

a = "Hello, World!"
print(len(a))  # Output: 13 (counts all characters including comma and space)
print()


# ============================================================================
# 8. CHECK IF STRING/PHRASE EXISTS IN STRING (IN keyword)
# The 'in' keyword checks if a substring exists within a string
# Returns True if found, False if not found
# This check is case-sensitive
# ============================================================================

txt = "The best things in life are free!"
print("free" in txt)  # Output: True (because "free" exists in txt)
print()

# Using 'in' with an if statement for conditional execution
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")  # This will execute because condition is True
print()


# ============================================================================
# 9. CHECK IF STRING/PHRASE DOES NOT EXIST (NOT IN keyword)
# The 'not in' keyword checks if a substring does NOT exist in a string
# Returns True if NOT found, False if found
# Useful for validation and error checking
# ============================================================================

txt = "The best things in life are free!"
print("expensive" not in txt)  # Output: True (because "expensive" is NOT in txt)
print()

# Using 'not in' with an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")  # This executes because condition is True
print()


# ============================================================================
# ADDITIONAL PRACTICAL EXAMPLES
# Combining multiple string operations for real-world scenarios
# ============================================================================


# Example 1: User input validation
username = "AsifDev123"
if "@" not in username:
    print(f"'{username}' is a valid username (no @ symbol)")
print()

# Example 2: Checking file extensions
filename = "document.pdf"
if ".pdf" in filename:
    print(f"'{filename}' is a PDF file")
print()

# Example 3: Email validation (basic check)
email = "user@example.com"
if "@" in email and "." in email:
    print(f"'{email}' appears to be a valid email format")
print()

# Example 4: Password strength check
password = "MyPassword123"
if len(password) >= 8:
    print(f"Password length is sufficient: {len(password)} characters")
else:
    print("Password is too short")
print()

# Example 5: Iterating and counting specific characters
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(f"The letter 'a' appears {count} times in '{word}'")