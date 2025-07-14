# -------------------------------
# 1. Creating a String
# -------------------------------
s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multiline string'''
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# -------------------------------
# 2. String Concatenation
# -------------------------------
greeting = s1 + " " + s2
print("\nConcatenated String:", greeting)

# -------------------------------
# 3. Escape Sequences in Strings
# -------------------------------
escaped = "He said, \"Python is great!\"\nNew Line\tTabbed"
print("\nEscape Sequences:")
print(escaped)

# -------------------------------
# 4. String Formatting
# -------------------------------

# Old Style Formatting
name = "Asif"
age = 22
print("\nOld Style Formatting:")
print("My name is %s and I am %d years old." % (name, age))

# New Style Formatting
print("\nNew Style Formatting:")
print("My name is {} and I am {} years old.".format(name, age))

# f-Strings (Python 3.6+)
print("\nf-String Formatting:")
print(f"My name is {name} and I am {age} years old.")

# -------------------------------
# 5. Strings as Sequences of Characters
# -------------------------------
text = "Python"
print("\nCharacters in String:")
for char in text:
    print(char)

# -------------------------------
# 6. Unpacking Characters
# -------------------------------
a, b, c, d, e, f = text
print("\nUnpacked Characters:", a, b, c, d, e, f)

# -------------------------------
# 7. Accessing Characters by Index
# -------------------------------
print("\nAccess by Index:")
print("First character:", text[0])
print("Last character:", text[-1])

# -------------------------------
# 8. Slicing Python Strings
# -------------------------------
print("\nSlicing:")
print(text[0:2])  # Py
print(text[2:])   # thon
print(text[:4])   # Pyth
print(text[::2])  # Pto

# -------------------------------
# 9. Reversing a String
# -------------------------------
print("\nReversed String:")
print(text[::-1])  # nohtyP

# -------------------------------
# 10. Skipping Characters While Slicing
# -------------------------------
print("\nSkipping Characters:")
print(text[::2])  # Pto
print(text[1::2]) # yhn

# -------------------------------
# 11. String Methods
# -------------------------------
sample = "  hello world  "
print("\nString Methods:")
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Title Case:", sample.title())
print("Stripped:", sample.strip())
print("Replaced:", sample.replace("world", "Python"))
print("Split:", sample.split())
print("Find 'world':", sample.find("world"))
print("Count 'l':", sample.count("l"))
print("Starts with '  he':", sample.startswith("  he"))
print("Ends with 'ld  ':", sample.endswith("ld  "))
print("Is digit:", "123".isdigit())
print("Is alpha:", "abc".isalpha())
print("Join:", "-".join(['a', 'b', 'c']))
