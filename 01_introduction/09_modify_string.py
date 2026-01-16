"""
Python String Modification Methods - Complete Guide
This file demonstrates built-in methods for modifying and manipulating strings.
Note: Strings are immutable in Python, so these methods return new strings.
"""

# ============================================================================
# 1. UPPER CASE - upper() method
# ============================================================================
# The upper() method converts all characters in a string to uppercase
# Original string remains unchanged (strings are immutable)
# Useful for: case-insensitive comparisons, formatting output

a = "Hello, World!"
print("Original string:", a)
print("Upper case:", a.upper())  # Output: HELLO, WORLD!
print("Original unchanged:", a)  # Output: Hello, World!
print()


# ============================================================================
# 2. LOWER CASE - lower() method
# ============================================================================
# The lower() method converts all characters in a string to lowercase
# Commonly used for: normalizing user input, case-insensitive searching

a = "Hello, World!"
print("Original string:", a)
print("Lower case:", a.lower())  # Output: hello, world!
print()


# ============================================================================
# 3. REMOVE WHITESPACE - strip() method
# ============================================================================
# Whitespace includes: spaces, tabs, newlines at the beginning or end
# strip() removes whitespace from BOTH beginning AND end
# lstrip() removes from left (beginning) only
# rstrip() removes from right (end) only

a = "   Hello, World!   "
print("Original string with spaces:", f"'{a}'")
print("After strip():", f"'{a.strip()}'")  # Output: 'Hello, World!'
print()

# Additional strip methods
text = "   Python Programming   "
print("Original:", f"'{text}'")
print("strip()  - both sides:", f"'{text.strip()}'")   # Removes from both
print("lstrip() - left only:", f"'{text.lstrip()}'")   # Removes from left
print("rstrip() - right only:", f"'{text.rstrip()}'")  # Removes from right
print()


# ============================================================================
# 4. REPLACE STRING - replace() method
# ============================================================================
# Syntax: string.replace(old, new, count)
# - old: substring to be replaced
# - new: substring to replace with
# - count (optional): number of occurrences to replace
# Replaces ALL occurrences by default

a = "Hello, World!"
print("Original string:", a)
print("Replace 'H' with 'J':", a.replace("H", "J"))  # Output: Jello, World!
print()

# Multiple replacements
text = "I like apples, apples are my favorite"
print("Original:", text)
print("Replace 'apples' with 'oranges':", text.replace("apples", "oranges"))
# Output: I like oranges, oranges are my favorite
print()

# Replace with count parameter (limit replacements)
sentence = "one one one one"
print("Original:", sentence)
print("Replace first 2 'one' with 'two':", sentence.replace("one", "two", 2))
# Output: two two one one
print()


# ============================================================================
# 5. SPLIT STRING - split() method
# ============================================================================
# Syntax: string.split(separator, maxsplit)
# - separator: delimiter to split on (default is whitespace)
# - maxsplit (optional): maximum number of splits
# Returns a LIST of substrings

a = "Hello, World!"
print("Original string:", a)
print("Split by comma:", a.split(","))  # Output: ['Hello', ' World!']
# Note: Creates a list with 2 elements
print()

# Split by space (default separator)
text = "Python is awesome"
print("Original:", text)
print("Split by space:", text.split())  # Output: ['Python', 'is', 'awesome']
print()

# Split with maxsplit parameter
sentence = "one-two-three-four-five"
print("Original:", sentence)
print("Split all:", sentence.split("-"))
# Output: ['one', 'two', 'three', 'four', 'five']
print("Split max 2 times:", sentence.split("-", 2))
# Output: ['one', 'two', 'three-four-five']
print()


# ============================================================================
# 6. ADDITIONAL USEFUL STRING METHODS
# ============================================================================

# capitalize() - First character uppercase, rest lowercase
text = "hello WORLD"
print("capitalize():", text.capitalize())  # Output: Hello world
print()

# title() - First character of each word uppercase
text = "hello world python"
print("title():", text.title())  # Output: Hello World Python
print()

# swapcase() - Swap uppercase to lowercase and vice versa
text = "Hello World"
print("swapcase():", text.swapcase())  # Output: hELLO wORLD
print()

# count() - Count occurrences of substring
text = "banana"
print("Count 'a' in 'banana':", text.count("a"))  # Output: 3
print()

# startswith() - Check if string starts with substring
text = "Hello, World!"
print("Starts with 'Hello':", text.startswith("Hello"))  # Output: True
print("Starts with 'World':", text.startswith("World"))  # Output: False
print()

# endswith() - Check if string ends with substring
text = "document.pdf"
print("Ends with '.pdf':", text.endswith(".pdf"))  # Output: True
print("Ends with '.doc':", text.endswith(".doc"))  # Output: False
print()

# find() - Find index of first occurrence (returns -1 if not found)
text = "Hello, World!"
print("Find 'World':", text.find("World"))  # Output: 7
print("Find 'Python':", text.find("Python"))  # Output: -1
print()


# ============================================================================
# 7. PRACTICAL USE CASES
# ============================================================================
# Real-world examples combining multiple string methods

# Example 1: Clean and normalize user input
user_input = "  MUHAMMAD ASIF  "
cleaned = user_input.strip().title()
print(f"User input: '{user_input}'")
print(f"Cleaned: '{cleaned}'")  # Output: 'Muhammad Asif'
print()

# Example 2: Process CSV data
csv_line = "John,Doe,john@example.com"
data = csv_line.split(",")
print("CSV line:", csv_line)
print("Split data:", data)  # Output: ['John', 'Doe', 'john@example.com']
print(f"First name: {data[0]}")
print(f"Last name: {data[1]}")
print(f"Email: {data[2]}")
print()

# Example 3: Email validation and formatting
email = "  USER@EXAMPLE.COM  "
formatted_email = email.strip().lower()
print(f"Original: '{email}'")
print(f"Formatted: '{formatted_email}'")  # Output: 'user@example.com'
print()

# Example 4: URL formatting
url = "www.example.com/page"
if not url.startswith("https://"):
    url = "https://" + url
print("Formatted URL:", url)  # Output: https://www.example.com/page
print()

# Example 5: Password masking
password = "MyPassword123"
masked = password.replace(password[:-2], "*" * len(password[:-2]))
print("Original:", password)
print("Masked:", masked)  # Output: ***********23
print()

# Example 6: Word count in a sentence
sentence = "Python is a powerful programming language"
word_count = len(sentence.split())
print("Sentence:", sentence)
print("Word count:", word_count)  # Output: 6
print()

# Example 7: Replace multiple spaces with single space
messy_text = "Hello    World    Python"
clean_text = " ".join(messy_text.split())
print("Messy text:", messy_text)
print("Clean text:", clean_text)  # Output: Hello World Python
print()


# ============================================================================
# 8. METHOD CHAINING
# ============================================================================
# You can chain multiple string methods together
# Methods are executed from left to right

text = "  HELLO, WORLD!  "
result = text.strip().lower().replace("hello", "hi")
print("Original:", f"'{text}'")
print("After chaining:", result)  # Output: hi, world!
print()

# Step-by-step breakdown of above
print("Step 1 - strip():", f"'{text.strip()}'")
print("Step 2 - lower():", f"'{text.strip().lower()}'")
print("Step 3 - replace():", f"'{text.strip().lower().replace('hello', 'hi')}'")
print()


# ============================================================================
# 9. COMMON STRING METHODS SUMMARY
# ============================================================================
print("=" * 60)
print("COMMON STRING METHODS QUICK REFERENCE")
print("=" * 60)
print("upper()      - Convert to uppercase")
print("lower()      - Convert to lowercase")
print("strip()      - Remove whitespace from both ends")
print("replace()    - Replace substring with another")
print("split()      - Split string into list")
print("capitalize() - First char uppercase")
print("title()      - Title case (each word)")
print("count()      - Count substring occurrences")
print("find()       - Find substring index")
print("startswith() - Check if starts with substring")
print("endswith()   - Check if ends with substring")
print("=" * 60) 