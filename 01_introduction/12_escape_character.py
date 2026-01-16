"""
Python Escape Characters - Complete Guide
This file demonstrates all escape characters and their usage in Python strings.
An escape character is a backslash (\) followed by a character that has special meaning.
"""

# ============================================================================
# 1. THE PROBLEM: ILLEGAL CHARACTERS IN STRINGS
# ============================================================================
# This will cause a SyntaxError because double quotes inside double quotes
# create ambiguity about where the string begins and ends

# This would cause an error (commented out to avoid breaking the code):
# txt = "We are the so-called "Vikings" from the north."
# SyntaxError: invalid syntax

print("THE PROBLEM:")
print("Cannot use: txt = \"We are the so-called \"Vikings\" from the north.\"")
print("This causes a SyntaxError!\n")


# ============================================================================
# 2. THE SOLUTION: ESCAPE CHARACTERS
# ============================================================================
# Use backslash (\) before the character you want to include literally
# The escape character tells Python to treat the following character specially

txt = "We are the so-called \"Vikings\" from the north."
print("SOLUTION - Using escape character (\\\"): ")
print(txt)
print()


# ============================================================================
# 3. SINGLE QUOTE ESCAPE (\')
# ============================================================================
# Use \' to insert a single quote inside a single-quoted string
# Although you can also use double quotes to avoid this

txt1 = 'It\'s a beautiful day!'
txt2 = "It's a beautiful day!"  # Alternative: use double quotes

print("SINGLE QUOTE ESCAPE (\\'):")
print(txt1)
print(txt2)
print("Both produce the same result!\n")


# ============================================================================
# 4. BACKSLASH ESCAPE (\\)
# ============================================================================
# Use \\ to insert a literal backslash in your string
# This is needed because \ is the escape character itself

txt = "This is a backslash: \\"
print("BACKSLASH ESCAPE (\\\\):")
print(txt)

# Example: File path (Windows style)
file_path = "C:\\Users\\Asif\\Documents\\file.txt"
print("Windows file path:", file_path)
print()


# ============================================================================
# 5. NEW LINE (\n)
# ============================================================================
# \n creates a line break (moves to next line)
# This is the most commonly used escape character

txt = "Hello\nWorld"
print("NEW LINE (\\n):")
print(txt)
print()

# Multiple new lines
txt = "Line 1\nLine 2\nLine 3"
print("Multiple new lines:")
print(txt)
print()


# ============================================================================
# 6. CARRIAGE RETURN (\r)
# ============================================================================
# \r moves the cursor to the beginning of the line
# In many systems, it works similar to \n
# On Windows, line breaks are typically \r\n

txt = "Hello\rWorld"
print("CARRIAGE RETURN (\\r):")
print(txt)
print("Note: Behavior may vary by operating system\n")


# ============================================================================
# 7. TAB (\t)
# ============================================================================
# \t inserts a horizontal tab (typically 4 or 8 spaces)
# Useful for formatting text, tables, and indentation

txt = "Name:\tAsif\nAge:\t25\nCity:\tKarachi"
print("TAB CHARACTER (\\t):")
print(txt)
print()

# Creating a simple table
print("Simple table using tabs:")
print("Product\t\tPrice\t\tQuantity")
print("Laptop\t\t$899\t\t5")
print("Mouse\t\t$15\t\t20")
print("Keyboard\t$45\t\t10")
print()


# ============================================================================
# 8. BACKSPACE (\b)
# ============================================================================
# \b moves the cursor one position back, potentially overwriting
# the previous character (behavior varies by environment)

txt = "Hello\bWorld"
print("BACKSPACE (\\b):")
print(txt)
print("Note: May appear as 'HellWorld' in some environments\n")


# ============================================================================
# 9. FORM FEED (\f)
# ============================================================================
# \f is a page break character (rarely used in modern programming)
# Was originally used for printer control

txt = "Page 1\fPage 2"
print("FORM FEED (\\f):")
print(txt)
print("Note: Rarely used in modern applications\n")


# ============================================================================
# 10. OCTAL VALUE (\ooo)
# ============================================================================
# \ooo represents a character by its octal (base-8) value
# ooo is a sequence of up to 3 octal digits

txt = "\101"  # Octal for 'A' (65 in decimal, 101 in octal)
print("OCTAL VALUE (\\ooo):")
print(f"\\101 = {txt}")

txt = "\110\145\154\154\157"  # "Hello" in octal
print(f"\\110\\145\\154\\154\\157 = {txt}")
print()


# ============================================================================
# 11. HEXADECIMAL VALUE (\xhh)
# ============================================================================
# \xhh represents a character by its hexadecimal (base-16) value
# hh is exactly 2 hexadecimal digits

txt = "\x41"  # Hex for 'A' (65 in decimal, 41 in hex)
print("HEXADECIMAL VALUE (\\xhh):")
print(f"\\x41 = {txt}")

txt = "\x48\x65\x6C\x6C\x6F"  # "Hello" in hex
print(f"\\x48\\x65\\x6C\\x6C\\x6F = {txt}")
print()


# ============================================================================
# 12. UNICODE ESCAPE SEQUENCES
# ============================================================================
# \uxxxx represents a Unicode character (4 hex digits)
# \Uxxxxxxxx represents a Unicode character (8 hex digits)

txt = "\u0041"  # Unicode for 'A'
print("UNICODE ESCAPE (\\uxxxx):")
print(f"\\u0041 = {txt}")

# Special characters and symbols
heart = "\u2764"  # Heart symbol
star = "\u2B50"   # Star symbol
smiley = "\u263A" # Smiley face

print(f"Heart: {heart}")
print(f"Star: {star}")
print(f"Smiley: {smiley}")
print()


# ============================================================================
# 13. RAW STRINGS (AVOIDING ESCAPE CHARACTERS)
# ============================================================================
# Prefix string with 'r' to treat backslashes as literal characters
# Useful for regular expressions, file paths, and regex patterns

# Normal string (backslashes need escaping)
normal = "C:\\Users\\Asif\\Documents"
print("Normal string:", normal)

# Raw string (backslashes are literal)
raw = r"C:\Users\Asif\Documents"
print("Raw string (r'...'):", raw)
print()

# Raw strings are especially useful for regex patterns
import re
pattern = r"\d+\.\d+"  # Pattern to match decimal numbers
print("Regex pattern:", pattern)
print()


# ============================================================================
# 14. COMBINING MULTIPLE ESCAPE CHARACTERS
# ============================================================================
# You can use multiple escape characters in a single string

message = "Name:\t\"John Doe\"\nAge:\t30\nQuote:\t\"It's a great day!\""
print("COMBINING ESCAPE CHARACTERS:")
print(message)
print()


# ============================================================================
# 15. PRACTICAL USE CASES
# ============================================================================

print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: JSON-like string
json_like = "{\"name\": \"Asif\", \"age\": 25, \"city\": \"Karachi\"}"
print("JSON-like string:")
print(json_like)
print()

# Example 2: Multi-line address
address = "Muhammad Asif\n123 Main Street\nKarachi, Pakistan\nPostal Code: 75500"
print("Multi-line address:")
print(address)
print()

# Example 3: Code snippet with indentation
code = "def greet():\n\tprint(\"Hello, World!\")\n\treturn True"
print("Code with tabs:")
print(code)
print()

# Example 4: Quoted dialogue
dialogue = "He said, \"She replied, 'I don\\'t know'.\""
print("Nested quotes:")
print(dialogue)
print()

# Example 5: File path handling
windows_path = "C:\\Program Files\\Python\\python.exe"
linux_path = "/usr/bin/python3"
print("Windows path:", windows_path)
print("Linux path:", linux_path)
print()


# ============================================================================
# 16. ESCAPE CHARACTERS REFERENCE TABLE
# ============================================================================

print("=" * 70)
print("ESCAPE CHARACTERS QUICK REFERENCE")
print("=" * 70)
print(f"{'Escape':<15} {'Description':<30} {'Example'}")
print("-" * 70)
print(f"{'\\\"':<15} {'Double quote':<30} {'He said \"Hi\"'}")
print(f"{'\\\\':<15} {'Backslash':<30} {'Path: C:\\\\Users'}")
print(f"{'\\n':<15} {'New line':<30} {'Line 1\\nLine 2'}")
print(f"{'\\r':<15} {'Carriage return':<30} {'Hello\\rWorld'}")
print(f"{'\\t':<15} {'Tab':<30} {'Name:\\tValue'}")
print(f"{'\\b':<15} {'Backspace':<30} {'Hello\\bWorld'}")
print(f"{'\\f':<15} {'Form feed':<30} {'Page1\\fPage2'}")
print(f"{'\\ooo':<15} {'Octal value':<30} {'\\101 = A'}")
print(f"{'\\xhh':<15} {'Hex value':<30} {'\\x41 = A'}")
print(f"{'\\uxxxx':<15} {'Unicode (4 digits)':<30} {'\\u2764 = ❤'}")
print("=" * 70)
print()


# ============================================================================
# 17. COMMON MISTAKES AND HOW TO AVOID THEM
# ============================================================================

print("=" * 60)
print("COMMON MISTAKES")
print("=" * 60)

# Mistake 1: Forgetting to escape backslash in file paths
print("❌ Wrong: path = 'C:\\Users\\Asif' (only works if raw string)")
print("✓ Right: path = 'C:\\\\Users\\\\Asif' or r'C:\\Users\\Asif'")
print()

# Mistake 2: Mixing quote types unnecessarily
print("❌ Wrong: txt = 'He said, \\'Hi\\''")
print("✓ Right: txt = \"He said, 'Hi'\" (use different quotes)")
print()

# Mistake 3: Not using raw strings for regex
print("❌ Wrong: pattern = '\\d+\\\\w+' (too many backslashes)")
print("✓ Right: pattern = r'\\d+\\w+' (raw string)")
print()

print("=" * 60)
print("\nRECOMMENDATION:")
print("- Use raw strings (r'...') for file paths and regex patterns")
print("- Mix quote types (' and \") to avoid excessive escaping")
print("- Use triple quotes (''' or \"\"\") for multi-line strings")
print("=" * 60)