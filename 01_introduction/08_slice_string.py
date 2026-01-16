"""
Python String Slicing - Complete Tutorial
This file demonstrates all string slicing operations in Python.
Slicing allows you to extract portions of a string using index ranges.
"""

# ============================================================================
# 1. BASIC STRING SLICING
# ============================================================================
# Syntax: string[start:end]
# - start: index where slice begins (included)
# - end: index where slice ends (NOT included)
# - Remember: First character has index 0
# 
# String: "Hello, World!"
# Index:   0123456789...

b = "Hello, World!"
print("Original string:", b)
print("Slice [2:5]:", b[2:5])  # Output: llo
# Explanation: Gets characters at positions 2, 3, 4 (stops before 5)
# Position 2 = 'l', Position 3 = 'l', Position 4 = 'o'
print()


# ============================================================================
# 2. SLICE FROM THE START
# ============================================================================
# Syntax: string[:end]
# If you omit the start index, slicing begins from index 0 (the beginning)
# This extracts characters from the start up to (but not including) the end index

b = "Hello, World!"
print("Original string:", b)
print("Slice [:5]:", b[:5])  # Output: Hello
# Explanation: Gets characters from index 0 to 4 (stops before 5)
# Same as b[0:5]
print()


# ============================================================================
# 3. SLICE TO THE END
# ============================================================================
# Syntax: string[start:]
# If you omit the end index, slicing continues to the end of the string
# This extracts characters from the start index to the last character

b = "Hello, World!"
print("Original string:", b)
print("Slice [2:]:", b[2:])  # Output: llo, World!
# Explanation: Gets all characters from index 2 to the end
# Starts at 'l' and includes everything after
print()


# ============================================================================
# 4. NEGATIVE INDEXING
# ============================================================================
# Negative indexes count from the end of the string
# -1 = last character, -2 = second to last, etc.
# 
# String: "Hello, World!"
# Positive: 0  1  2  3  4  5  6  7  8  9  10 11 12
# Negative: -13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1

b = "Hello, World!"
print("Original string:", b)
print("Slice [-5:-2]:", b[-5:-2])  # Output: orl
# Explanation:
# -5 points to 'o' in "World!"
# -2 points to 'd' in "World!" (not included in result)
# Gets characters: 'o', 'r', 'l'
print()


# ============================================================================
# 5. COMPREHENSIVE SLICING EXAMPLES
# ============================================================================
# Demonstrating various slicing patterns with detailed explanations

text = "Python Programming"
print("Original string:", text)
print(f"Length: {len(text)} characters")
print()

# Get first 6 characters
print("First 6 characters [:6]:", text[:6])  # Output: Python
print()

# Get last 11 characters
print("Last 11 characters [7:]:", text[7:])  # Output: Programming
print()

# Get middle portion
print("Middle portion [7:11]:", text[7:11])  # Output: Prog
print()

# Using negative index to get last 4 characters
print("Last 4 characters [-4:]:", text[-4:])  # Output: ming
print()

# Using negative index to get all except last 4 characters
print("All except last 4 [:-4]:", text[:-4])  # Output: Python Program
print()

# Combining negative and positive indexes
print("From index 0 to -8 [0:-8]:", text[0:-8])  # Output: Python Pro
print()

# Get everything except first and last character
print("Except first & last [1:-1]:", text[1:-1])  # Output: ython Programmin
print()


# ============================================================================
# 6. PRACTICAL USE CASES
# ============================================================================
# Real-world examples of string slicing

# Example 1: Extract domain from email
email = "user@example.com"
domain = email[5:]  # Gets everything after "user@"
print(f"Email: {email}")
print(f"Domain: {domain}")
print()

# Example 2: Get file extension
filename = "document.pdf"
extension = filename[-4:]  # Gets last 4 characters
print(f"Filename: {filename}")
print(f"Extension: {extension}")
print()

# Example 3: Extract first name
full_name = "Muhammad Asif"
first_name = full_name[:8]  # Gets first 8 characters
print(f"Full name: {full_name}")
print(f"First name: {first_name}")
print()

# Example 4: Remove file extension
filename = "report.docx"
name_without_ext = filename[:-5]  # Remove last 5 characters (.docx)
print(f"Filename: {filename}")
print(f"Without extension: {name_without_ext}")
print()

# Example 5: Extract phone number parts
phone = "021-1234567"
area_code = phone[:3]    # First 3 characters
number = phone[4:]       # Everything after the dash
print(f"Phone: {phone}")
print(f"Area code: {area_code}")
print(f"Number: {number}")
print()


# ============================================================================
# 7. ADVANCED SLICING WITH STEP
# ============================================================================
# Syntax: string[start:end:step]
# The step parameter specifies the increment between characters
# Default step is 1

text = "Hello, World!"
print("Original string:", text)

# Every second character
print("Every 2nd character [::2]:", text[::2])  # Output: Hlo ol!
print()

# Reverse string using negative step
print("Reversed string [::-1]:", text[::-1])  # Output: !dlroW ,olleH
print()

# Every 3rd character from index 0 to 10
print("Every 3rd char [0:10:3]:", text[0:10:3])  # Output: Hl,
print()


# ============================================================================
# 8. COMMON SLICING PATTERNS SUMMARY
# ============================================================================
# Quick reference guide for common slicing operations

sample = "ABCDEFGH"
print("String:", sample)
print("s[:3]  - First 3 chars:", sample[:3])      # ABC
print("s[3:]  - From index 3 to end:", sample[3:])  # DEFGH
print("s[-3:] - Last 3 chars:", sample[-3:])      # FGH
print("s[:-3] - All except last 3:", sample[:-3])  # ABCDE
print("s[2:5] - Index 2 to 4:", sample[2:5])      # CDE
print("s[::2] - Every 2nd char:", sample[::2])    # ACEG
print("s[::-1]- Reversed:", sample[::-1])         # HGFEDCBA