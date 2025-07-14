## What are Strings?

In Python, a **string** is a **sequence of characters** enclosed in **single (`'`)**, **double (`"`)**, or **triple quotes (`'''` or `"""`)**.

```python
str1 = 'Hello'
str2 = "World"
str3 = '''This is
a multiline string'''
```

Strings are **immutable**, meaning they **cannot be changed** after creation.

---

## Creating a String

You can create strings using:

```python
a = 'Single quotes'
b = "Double quotes"
c = '''Triple
multi-line
string'''
```

---

## String Concatenation

Combine strings using the `+` operator.

```python
first = "Python"
second = "Rocks"
combined = first + " " + second
print(combined)  # Output: Python Rocks
```

---

## Escape Sequences in Strings

Escape sequences let you include **special characters** in strings.

| Escape Code | Meaning      |
| ----------- | ------------ |
| `\n`        | Newline      |
| `\t`        | Tab          |
| `\\`        | Backslash    |
| `\"`        | Double Quote |
| `\'`        | Single Quote |

```python
print("Line1\nLine2")
print("Column1\tColumn2")
print("He said, \"Hi!\"")
```

---

## String Formatting

Python supports multiple ways to insert values into strings.

---

### Old Style String Formatting (`%` Operator)

```python
name = "Asif"
age = 22
print("My name is %s and I am %d years old." % (name, age))
```

---

### New Style Formatting (`str.format()`)

```python
name = "Asif"
age = 22
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
```

---

### f-Strings (Python 3.6+)

Simplest and most readable.

```python
name = "Asif"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

---

## Python Strings as Sequences of Characters

A string is a **sequence**, meaning it can be **looped through** character by character.

```python
text = "Hello"
for char in text:
    print(char)
```

---

## Unpacking Characters

You can unpack characters into variables:

```python
word = "Hey"
a, b, c = word
print(a, b, c)  # H e y
```

---

## Accessing Characters by Index

Use square brackets `[]` to access characters.

```python
text = "Python"
print(text[0])   # P
print(text[-1])  # n (last character)
```

---

## Slicing Python Strings

Use `[start:end:step]` to get substrings.

```python
text = "Python"
print(text[0:2])   # Py
print(text[1:4])   # yth
print(text[:3])    # Pyt
print(text[3:])    # hon
```

---

## Reversing a String

Use slicing with a step of `-1`.

```python
text = "Python"
reversed_text = text[::-1]
print(reversed_text)  # nohtyP
```

---

## Skipping Characters While Slicing

Use the `step` in slicing.

```python
text = "HelloWorld"
print(text[::2])  # Hlool
print(text[1::2]) # elWrd
```

---

## String Methods

Here are some **common string methods**:

| Method             | Description                            |
| ------------------ | -------------------------------------- |
| `.lower()`         | Converts to lowercase                  |
| `.upper()`         | Converts to uppercase                  |
| `.title()`         | Capitalizes first letter of each word  |
| `.strip()`         | Removes whitespace                     |
| `.replace(a, b)`   | Replaces substring a with b            |
| `.find(sub)`       | Finds the first index of a substring   |
| `.split(sep)`      | Splits string into list by separator   |
| `.join(list)`      | Joins list into string                 |
| `.startswith(sub)` | Returns True if string starts with sub |
| `.endswith(sub)`   | Returns True if string ends with sub   |
| `.isdigit()`       | True if all chars are digits           |
| `.isalpha()`       | True if all chars are alphabets        |
| `.count(sub)`      | Counts occurrences of substring        |

### Example:

```python
text = "  Hello World  "
print(text.strip())          # "Hello World"
print(text.upper())          # "  HELLO WORLD  "
print(text.replace("World", "Python"))  # "  Hello Python  "
print(text.split())          # ['Hello', 'World']
```

---

## Summary

| Concept          | Example                                 |
| ---------------- | --------------------------------------- |
| String creation  | `'Hello'`, `"World"`, `'''Multiline'''` |
| Concatenation    | `"Hi" + " There"` → `"Hi There"`        |
| Escape Sequences | `"He said \"Hi\""`                      |
| Old Formatting   | `"Hello %s" % name`                     |
| `str.format()`   | `"Hello {}".format(name)`               |
| f-String         | `f"Hello {name}"`                       |
| Access by Index  | `s[0]`, `s[-1]`                         |
| Slicing          | `s[1:4]`, `s[::-1]`                     |
| String methods   | `.upper()`, `.split()`, `.replace()`    |

---
