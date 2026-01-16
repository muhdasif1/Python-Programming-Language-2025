"""
Python String Methods - Complete Reference Guide
This file demonstrates ALL built-in string methods in Python.

IMPORTANT: All string methods return NEW values. 
They do NOT change the original string (strings are immutable).
"""

# ============================================================================
# CASE CONVERSION METHODS
# ============================================================================

print("=" * 70)
print("CASE CONVERSION METHODS")
print("=" * 70)

text = "hello world PYTHON"

# capitalize() - First character uppercase, rest lowercase
print(f"Original: {text}")
print(f"capitalize(): {text.capitalize()}")  # Hello world python

# casefold() - Converts to lowercase (more aggressive than lower())
print(f"casefold(): {text.casefold()}")  # hello world python

# lower() - Converts to lowercase
print(f"lower(): {text.lower()}")  # hello world python

# upper() - Converts to uppercase
print(f"upper(): {text.upper()}")  # HELLO WORLD PYTHON

# swapcase() - Swaps uppercase to lowercase and vice versa
print(f"swapcase(): {text.swapcase()}")  # HELLO WORLD python

# title() - First character of each word uppercase
print(f"title(): {text.title()}")  # Hello World Python

print()


# ============================================================================
# ALIGNMENT AND PADDING METHODS
# ============================================================================

print("=" * 70)
print("ALIGNMENT AND PADDING METHODS")
print("=" * 70)

text = "Python"

# center() - Centers string with specified width
print(f"center(20): |{text.center(20)}|")  # |      Python      |
print(f"center(20, '*'): |{text.center(20, '*')}|")  # |*******Python*******|

# ljust() - Left aligns string with specified width
print(f"ljust(20): |{text.ljust(20)}|")  # |Python              |
print(f"ljust(20, '-'): |{text.ljust(20, '-')}|")  # |Python--------------|

# rjust() - Right aligns string with specified width
print(f"rjust(20): |{text.rjust(20)}|")  # |              Python|
print(f"rjust(20, '-'): |{text.rjust(20, '-')}|")  # |--------------|Python|

# zfill() - Pads string with zeros on the left
number = "42"
print(f"zfill(5): {number.zfill(5)}")  # 00042

print()


# ============================================================================
# TRIMMING METHODS
# ============================================================================

print("=" * 70)
print("TRIMMING METHODS")
print("=" * 70)

text = "   Hello World   "

# strip() - Removes whitespace from both ends
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")  # 'Hello World'

# lstrip() - Removes whitespace from left
print(f"lstrip(): '{text.lstrip()}'")  # 'Hello World   '

# rstrip() - Removes whitespace from right
print(f"rstrip(): '{text.rstrip()}'")  # '   Hello World'

# Removing specific characters
text2 = "***Hello***"
print(f"strip('*'): '{text2.strip('*')}'")  # 'Hello'

print()


# ============================================================================
# SEARCH AND CHECK METHODS
# ============================================================================

print("=" * 70)
print("SEARCH AND CHECK METHODS")
print("=" * 70)

text = "Hello World Python Programming"

# count() - Counts occurrences of substring
print(f"count('o'): {text.count('o')}")  # 4

# find() - Returns first index of substring (-1 if not found)
print(f"find('World'): {text.find('World')}")  # 6
print(f"find('Java'): {text.find('Java')}")  # -1

# rfind() - Returns last index of substring
print(f"rfind('o'): {text.rfind('o')}")  # 27

# index() - Like find() but raises error if not found
print(f"index('Python'): {text.index('Python')}")  # 12

# rindex() - Returns last index (raises error if not found)
print(f"rindex('o'): {text.rindex('o')}")  # 27

# startswith() - Checks if string starts with substring
print(f"startswith('Hello'): {text.startswith('Hello')}")  # True

# endswith() - Checks if string ends with substring
print(f"endswith('Programming'): {text.endswith('Programming')}")  # True

print()


# ============================================================================
# SPLITTING AND JOINING METHODS
# ============================================================================

print("=" * 70)
print("SPLITTING AND JOINING METHODS")
print("=" * 70)

# split() - Splits string into list
text = "Python,Java,C++,JavaScript"
print(f"split(','): {text.split(',')}")

# rsplit() - Splits from right
text = "one-two-three-four"
print(f"rsplit('-', 2): {text.rsplit('-', 2)}")  # ['one-two', 'three', 'four']

# splitlines() - Splits at line breaks
multiline = "Line 1\nLine 2\nLine 3"
print(f"splitlines(): {multiline.splitlines()}")

# partition() - Splits into 3 parts: before, separator, after
text = "Hello-World-Python"
print(f"partition('-'): {text.partition('-')}")  # ('Hello', '-', 'World-Python')

# rpartition() - Partitions from right
print(f"rpartition('-'): {text.rpartition('-')}")  # ('Hello-World', '-', 'Python')

# join() - Joins list elements into string
words = ["Python", "is", "awesome"]
print(f"' '.join(words): {' '.join(words)}")  # Python is awesome

print()


# ============================================================================
# REPLACEMENT METHODS
# ============================================================================

print("=" * 70)
print("REPLACEMENT METHODS")
print("=" * 70)

text = "I like apples, apples are tasty"

# replace() - Replaces substring
print(f"replace('apples', 'oranges'): {text.replace('apples', 'oranges')}")

# replace with count limit
print(f"replace('apples', 'oranges', 1): {text.replace('apples', 'oranges', 1)}")

# expandtabs() - Sets tab size
text_with_tabs = "Name:\tAge:\tCity"
print(f"expandtabs(4): {text_with_tabs.expandtabs(4)}")
print(f"expandtabs(16): {text_with_tabs.expandtabs(16)}")

print()


# ============================================================================
# VALIDATION METHODS (is* methods)
# ============================================================================

print("=" * 70)
print("VALIDATION METHODS")
print("=" * 70)

# isalnum() - Checks if alphanumeric (letters and numbers only)
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # True
print(f"'abc 123'.isalnum(): {'abc 123'.isalnum()}")  # False (has space)

# isalpha() - Checks if only letters
print(f"'Python'.isalpha(): {'Python'.isalpha()}")  # True
print(f"'Python3'.isalpha(): {'Python3'.isalpha()}")  # False

# isascii() - Checks if all characters are ASCII
print(f"'Hello'.isascii(): {'Hello'.isascii()}")  # True
print(f"'Hello😀'.isascii(): {'Hello😀'.isascii()}")  # False

# isdecimal() - Checks if all characters are decimals
print(f"'123'.isdecimal(): {'123'.isdecimal()}")  # True
print(f"'12.3'.isdecimal(): {'12.3'.isdecimal()}")  # False

# isdigit() - Checks if all characters are digits
print(f"'123'.isdigit(): {'123'.isdigit()}")  # True
print(f"'①②③'.isdigit(): {'①②③'.isdigit()}")  # True (superscript digits)

# isnumeric() - Checks if all characters are numeric
print(f"'123'.isnumeric(): {'123'.isnumeric()}")  # True
print(f"'½'.isnumeric(): {'½'.isnumeric()}")  # True (fraction)

# isidentifier() - Checks if valid Python identifier
print(f"'my_var'.isidentifier(): {'my_var'.isidentifier()}")  # True
print(f"'2var'.isidentifier(): {'2var'.isidentifier()}")  # False

# islower() - Checks if all characters are lowercase
print(f"'python'.islower(): {'python'.islower()}")  # True
print(f"'Python'.islower(): {'Python'.islower()}")  # False

# isupper() - Checks if all characters are uppercase
print(f"'PYTHON'.isupper(): {'PYTHON'.isupper()}")  # True
print(f"'Python'.isupper(): {'Python'.isupper()}")  # False

# isspace() - Checks if all characters are whitespace
print(f"'   '.isspace(): {'   '.isspace()}")  # True
print(f"' a '.isspace(): {' a '.isspace()}")  # False

# istitle() - Checks if string is in title case
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")  # True
print(f"'Hello world'.istitle(): {'Hello world'.istitle()}")  # False

# isprintable() - Checks if all characters are printable
print(f"'Hello'.isprintable(): {'Hello'.isprintable()}")  # True
print(f"'Hello\\n'.isprintable(): {'Hello\n'.isprintable()}")  # False

print()


# ============================================================================
# FORMAT METHODS
# ============================================================================

print("=" * 70)
print("FORMAT METHODS")
print("=" * 70)

# format() - Formats string with values
name = "Asif"
age = 25
text = "My name is {} and I am {} years old"
print(f"format(): {text.format(name, age)}")

# format_map() - Formats using dictionary
data = {"name": "Asif", "age": 25}
text = "My name is {name} and I am {age} years old"
print(f"format_map(): {text.format_map(data)}")

print()


# ============================================================================
# ENCODING METHODS
# ============================================================================

print("=" * 70)
print("ENCODING METHODS")
print("=" * 70)

text = "Hello World"

# encode() - Encodes string to bytes
encoded = text.encode('utf-8')
print(f"encode('utf-8'): {encoded}")  # b'Hello World'

# Different encoding formats
print(f"encode('ascii'): {text.encode('ascii')}")

print()


# ============================================================================
# TRANSLATION METHODS
# ============================================================================

print("=" * 70)
print("TRANSLATION METHODS")
print("=" * 70)

# maketrans() and translate() - Character mapping
text = "Hello World"

# Create translation table
trans_table = str.maketrans("aeiou", "12345")
print(f"Original: {text}")
print(f"translate(): {text.translate(trans_table)}")  # H2ll4 W4rld

# Remove characters
trans_table2 = str.maketrans("", "", "aeiou")
print(f"Remove vowels: {text.translate(trans_table2)}")  # Hll Wrld

print()


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("=" * 70)
print("PRACTICAL EXAMPLES")
print("=" * 70)

# Example 1: Email validation
email = "user@example.com"
if "@" in email and "." in email and email.count("@") == 1:
    print(f"✓ '{email}' appears to be valid")

# Example 2: Password strength check
password = "MyPass123"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
is_strong = has_upper and has_lower and has_digit and len(password) >= 8

print(f"\nPassword: {password}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has digit: {has_digit}")
print(f"Is strong: {is_strong}")

# Example 3: Clean and format user input
user_input = "  mUhAmMaD aSiF  "
cleaned = user_input.strip().title()
print(f"\nUser input: '{user_input}'")
print(f"Cleaned: '{cleaned}'")

# Example 4: Word count
sentence = "Python is a powerful programming language"
word_count = len(sentence.split())
print(f"\nSentence: {sentence}")
print(f"Word count: {word_count}")

# Example 5: Remove punctuation
import string
text_with_punct = "Hello, World! How are you?"
text_no_punct = text_with_punct.translate(str.maketrans("", "", string.punctuation))
print(f"\nWith punctuation: {text_with_punct}")
print(f"Without punctuation: {text_no_punct}")

print()


# ============================================================================
# STRING METHODS QUICK REFERENCE
# ============================================================================

print("=" * 70)
print("STRING METHODS QUICK REFERENCE")
print("=" * 70)
print(f"{'Method':<20} {'Category':<20} {'Returns'}")
print("-" * 70)
print(f"{'capitalize()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'casefold()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'lower()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'upper()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'title()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'swapcase()':<20} {'Case Conversion':<20} {'New string'}")
print(f"{'center()':<20} {'Alignment':<20} {'New string'}")
print(f"{'ljust()':<20} {'Alignment':<20} {'New string'}")
print(f"{'rjust()':<20} {'Alignment':<20} {'New string'}")
print(f"{'zfill()':<20} {'Alignment':<20} {'New string'}")
print(f"{'strip()':<20} {'Trimming':<20} {'New string'}")
print(f"{'lstrip()':<20} {'Trimming':<20} {'New string'}")
print(f"{'rstrip()':<20} {'Trimming':<20} {'New string'}")
print(f"{'find()':<20} {'Search':<20} {'Integer (index)'}")
print(f"{'rfind()':<20} {'Search':<20} {'Integer (index)'}")
print(f"{'index()':<20} {'Search':<20} {'Integer (index)'}")
print(f"{'count()':<20} {'Search':<20} {'Integer'}")
print(f"{'startswith()':<20} {'Search':<20} {'Boolean'}")
print(f"{'endswith()':<20} {'Search':<20} {'Boolean'}")
print(f"{'split()':<20} {'Splitting':<20} {'List'}")
print(f"{'rsplit()':<20} {'Splitting':<20} {'List'}")
print(f"{'splitlines()':<20} {'Splitting':<20} {'List'}")
print(f"{'partition()':<20} {'Splitting':<20} {'Tuple'}")
print(f"{'join()':<20} {'Joining':<20} {'New string'}")
print(f"{'replace()':<20} {'Replacement':<20} {'New string'}")
print(f"{'isalnum()':<20} {'Validation':<20} {'Boolean'}")
print(f"{'isalpha()':<20} {'Validation':<20} {'Boolean'}")
print(f"{'isdigit()':<20} {'Validation':<20} {'Boolean'}")
print(f"{'islower()':<20} {'Validation':<20} {'Boolean'}")
print(f"{'isupper()':<20} {'Validation':<20} {'Boolean'}")
print(f"{'format()':<20} {'Formatting':<20} {'New string'}")
print(f"{'encode()':<20} {'Encoding':<20} {'Bytes'}")
print(f"{'translate()':<20} {'Translation':<20} {'New string'}")
print("=" * 70)

print("\nREMEMBER: All string methods return NEW values!")
print("They do NOT modify the original string (strings are immutable).")