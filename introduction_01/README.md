# What is Python Programming
Python is a **high-level, interpreted programming language** that’s known for being **easy to learn and read**. It was created by **Guido van Rossum** and first released in **1991**.


**Key Features:**

* **Readable syntax:** Its code looks almost like English, making it great for beginners.
* **Interpreted:** You don’t need to compile it — Python runs your code line by line.
* **Cross-platform:** Works on Windows, macOS, Linux, and more.
* **Versatile:** Used in web development, data science, AI, machine learning, automation, and more.
* **Huge community:** Millions of users, tons of free libraries and frameworks (like Django, Flask, NumPy, TensorFlow, etc.).

# **Practical Applications of Python**
Python has numerous practical applications across various industries. Some of the top applications include:

1. Data Science and Analytics: data analysis, machine learning, and visualization
2. Agentic AI: building autonomous agents, chatbots, and virtual assistants
3. Machine Learning: developing predictive models and recommender systems
4. Natural Language Processing (NLP): text analysis, sentiment analysis, and language translation
5. Computer Vision: image recognition, object detection, and facial recognition
6. Robotics: building and controlling robots, drones, and autonomous vehicles
7. Web Development: building web applications and frameworks
8. Artificial Intelligence and Machine Learning: AI, ML, and deep learning
9. Automation and Scripting: automating tasks and workflows
10. Scientific Computing: scientific simulations and data analysis
11. Cybersecurity: security testing and penetration testing
12. Internet of Things (IoT): building IoT applications and devices
---
# How Python works

### 1. **You write the code**

You write Python code in a **text editor or IDE** (like VS Code, PyCharm, or IDLE).
Example:

```python
print("Hello, World!")
```

---

### 2. **The Python Interpreter reads it**

Python is an **interpreted language**, meaning it doesn’t need to be “compiled” first.
Instead, a special program called the **Python interpreter** reads and runs your code **line by line**.

---

### 3. **Converts code to machine language**

The interpreter converts your code into a form the computer understands — **bytecode**, and then into **machine code** (0s and 1s).
This is how your computer actually performs the tasks you write in Python.

---

### 4. **The program runs**

Once translated, Python tells your computer what to do — for example, display text, do math, or control a robot!

---

### Example

```python
x = 5
y = 3
print(x + y)
```

Python reads this code line by line
Adds 5 + 3
Prints **8**

---
# **comments** 
 are used to explain your code and make it easier to understand. They are ignored by the Python interpreter — meaning they don’t affect how the program runs.

There are **two main types of comments**:

---

### 1. **Single-line comment**

Use the `#` symbol before your comment.

```python
# This is a single-line comment
print("Hello, World!")  # You can also add a comment at the end of a line
```

---

### 2. **Multi-line comment**

Python doesn’t have a specific multi-line comment syntax, but you can use triple quotes `'''` or `"""` to write multi-line comments (commonly used for documentation).

```python
'''
This is a multi-line comment.
You can write multiple lines here.
'''
print("Python comments example")
```

OR

```python
"""
This is also a multi-line comment.
It works the same way.
"""
```

---
# **PYTHON DATA TYPE METHODS AND FUNCTIONS**
# Includes: STRING, INTEGER, LIST, TUPLE, SET, and DICTIONARY methods
---

## **STRING METHODS**

Strings are sequences of characters (text).
Example: `s = "Hello World"`
| Method                  | Description                                      | Example                                            |
| ----------------------- | ------------------------------------------------ | -------------------------------------------------- |
| capitalize()            | Capitalizes the first letter and lowers the rest | "hello world".capitalize() → "Hello world"         |
| casefold()              | Converts to lowercase (stronger than lower())    | "HELLO".casefold() → "hello"                       |
| center(width, fillchar) | Centers string using spaces or a fill character  | "hi".center(10, "-") → "----hi----"                |
| count(sub)              | Counts occurrences of a substring                | "banana".count("a") → 3                            |
| encode(encoding)        | Returns encoded version of string (bytes)        | "hello".encode() → b'hello'                        |
| endswith(suffix)        | Checks if string ends with suffix                | "test.py".endswith(".py") → True                   |
| expandtabs(tabsize)     | Replaces tabs \t with spaces                     | "hi\tthere".expandtabs(4) → "hi  there"            |
| find(sub)               | Finds index of first occurrence or -1            | "apple".find("p") → 1                              |
| format(*args, **kwargs) | Inserts values into {} placeholders              | "My name is {}".format("Asif") → "My name is Asif" |
| format_map(mapping)     | Formats using a dictionary                       | "{name}".format_map({"name": "Asif"}) → "Asif"     |
| index(sub)              | Like find() but raises error if not found        | "apple".index("p") → 1                             |
| isalnum()               | True if all characters are letters or numbers    | "abc123".isalnum() → True                          |
| isalpha()               | True if all characters are letters               | "abc".isalpha() → True                             |
| isascii()               | True if all characters are ASCII                 | "Hello!".isascii() → True                          |
| isdecimal()             | True if all are decimal characters               | "123".isdecimal() → True                           |
| isdigit()               | True if all are digits                           | "123".isdigit() → True                             |
| isidentifier()          | True if valid Python identifier                  | "name1".isidentifier() → True                      |
| islower()               | True if all letters are lowercase                | "hello".islower() → True                           |
| isnumeric()             | True if all characters are numeric               | "12345".isnumeric() → True                         |
| isprintable()           | True if all characters are printable             | "hi!".isprintable() → True                         |
| isspace()               | True if only whitespace                          | "   ".isspace() → True                             |
| istitle()               | True if each word starts uppercase               | "Hello World".istitle() → True                     |
| isupper()               | True if all letters are uppercase                | "HELLO".isupper() → True                           |
| join(iterable)          | Joins elements of a list with the string         | "-".join(["a", "b"]) → "a-b"                       |
| ljust(width, fillchar)  | Left-justifies string in given width             | "hi".ljust(5, "-") → "hi---"                       |
| lower()                 | Converts all to lowercase                        | "HELLO".lower() → "hello"                          |
| lstrip(chars)           | Removes spaces (or chars) from left              | "   hi".lstrip() → "hi"                            |
| maketrans(x, y, z)      | Creates translation table for translate()        | str.maketrans("a", "1")                            |
| partition(sep)          | Splits into (before, sep, after)                 | "name:Asif".partition(":") → ('name', ':', 'Asif') |
| removeprefix(prefix)    | Removes prefix if present                        | "unhappy".removeprefix("un") → "happy"             |
| removesuffix(suffix)    | Removes suffix if present                        | "testing".removesuffix("ing") → "test"             |
| replace(old, new)       | Replaces old substring with new                  | "hello".replace("l", "x") → "hexxo"                |
| rfind(sub)              | Finds last index of substring                    | "banana".rfind("a") → 5                            |
| rindex(sub)             | Like rfind() but raises error if not found       | "banana".rindex("a") → 5                           |
| rjust(width, fillchar)  | Right-justifies string                           | "hi".rjust(5, "-") → "---hi"                       |
| rpartition(sep)         | Like partition(), starts from right              | "a:b:c".rpartition(":") → ('a:b', ':', 'c')        |
| rsplit(sep, maxsplit)   | Splits from right side                           | "a,b,c".rsplit(",", 1) → ['a,b', 'c']              |
| rstrip(chars)           | Removes spaces (or chars) from right             | "hi   ".rstrip() → "hi"                            |
| split(sep, maxsplit)    | Splits into list                                 | "a b c".split() → ['a', 'b', 'c']                  |
| splitlines(keepends)    | Splits string by line breaks                     | "Hi\nBye".splitlines() → ['Hi', 'Bye']             |
| startswith(prefix)      | Checks if starts with prefix                     | "hello".startswith("he") → True                    |
| strip(chars)            | Removes spaces (or chars) both sides             | "  hello  ".strip() → "hello"                      |
| swapcase()              | Swaps uppercase ↔ lowercase                      | "HeLLo".swapcase() → "hEllO"                       |
| title()                 | Capitalizes first letter of each word            | "hello world".title() → "Hello World"              |
| translate(table)        | Replaces chars using translation table           | "abc".translate(str.maketrans("a", "1")) → "1bc"   |
| upper()                 | Converts all letters to uppercase                | "hello".upper() → "HELLO"                          |
| zfill(width)            | Pads number string with zeros                    | "42".zfill(5) → "00042"                            |

---

## **INTEGER (int) METHODS**
# Python `int` and `float` Methods & Attributes

| Method / Attribute       | Description                                         | Example                                               |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| as_integer_ratio()        | Returns a pair of integers (numerator, denominator) | (2.5).as_integer_ratio() → (5, 2)                     |
| bit_count()               | Returns number of 1 bits in binary representation   | (13).bit_count() → 3                                  |
| bit_length()              | Returns number of bits required to represent number | (13).bit_length() → 4                                 |
| conjugate()               | Returns the complex conjugate (for real numbers, itself) | (5).conjugate() → 5                              |
| denominator               | Denominator of a rational number                   | (3.5).as_integer_ratio()[1] → 2                       |
| from_bytes(bytes, byteorder) | Converts bytes to an integer                     | int.from_bytes(b'\x00\x10', 'big') → 16               |
| imag                      | Imaginary part of a number                         | (3+4j).imag → 4                                       |
| is_integer()              | True if float has no fractional part               | (5.0).is_integer() → True                             |
| numerator                 | Numerator of a rational number                     | (3.5).as_integer_ratio()[0] → 7                       |
| real                      | Real part of a number                              | (3+4j).real → 3                                       |
| to_bytes(length, byteorder) | Returns bytes representing integer                | (16).to_bytes(2, 'big') → b'\x00\x10'                 |


---

## **LIST METHODS**

| Method               | Description                                   | Example                                      |
| -------------------- | --------------------------------------------- | -------------------------------------------- |
| append(x)            | Adds an item to the end of the list           | fruits.append("orange") → ["apple", "banana", "orange"] |
| clear()              | Removes all items from the list               | fruits.clear() → []                          |
| copy()               | Returns a shallow copy of the list            | new_list = fruits.copy() → ["apple", "banana"] |
| count(x)             | Returns number of occurrences of x            | [1, 2, 2, 3].count(2) → 2                    |
| extend(iterable)     | Adds elements of another iterable (like list) | fruits.extend(["mango", "grape"]) → ["apple", "banana", "mango", "grape"] |
| index(x)             | Returns index of first occurrence of x        | ["a", "b", "c"].index("b") → 1               |
| insert(i, x)         | Inserts item x at position i                  | fruits.insert(1, "kiwi") → ["apple", "kiwi", "banana"] |
| pop(i)               | Removes and returns item at index i (last if not given) | fruits.pop() → removes last item |
| remove(x)            | Removes first occurrence of value x           | fruits.remove("banana") → ["apple", "cherry"] |
| reverse()            | Reverses the elements of the list in place    | fruits.reverse() → ["cherry", "banana", "apple"] |
| sort()               | Sorts the list in ascending order             | numbers.sort() → [1, 2, 3, 4]                |
| sort(reverse=True)   | Sorts the list in descending order            | numbers.sort(reverse=True) → [4, 3, 2, 1]    |


---

## **TUPLE METHODS**

Tuples are like lists but **immutable** (cannot be changed).
Example: `t = (1, 2, 3)`

| Method     | Description        | Example                  |
| ---------- | ------------------ | ------------------------ |
| `count(x)` | Counts x in tuple  | `(1,1,2).count(1)` → `2` |
| `index(x)` | Returns index of x | `(1,2,3).index(2)` → `1` |

---

## **SET METHODS**
| Method                         | Description                               | Example                                           |
| ------------------------------ | ----------------------------------------- | ------------------------------------------------- |
| add(x)                         | Adds element `x`                          | `{1,2}.add(3)` → `{1,2,3}`                        |
| clear()                        | Removes all elements                      | `{1,2}.clear()` → `set()`                         |
| copy()                         | Returns a shallow copy                    | `{1,2}.copy()` → `{1,2}`                          |
| difference(s)                  | Elements in one but not the other         | `{1,2,3}.difference({2,3})` → `{1}`               |
| difference_update(s)           | Removes common elements                   | `A.difference_update(B)`                          |
| discard(x)                     | Removes if present (no error)             | `{1,2,3}.discard(2)` → `{1,3}`                    |
| intersection(s)                | Common elements                           | `{1,2,3}.intersection({2,3,4})` → `{2,3}`         |
| intersection_update(s)         | Keeps only common                         | `A.intersection_update(B)`                        |
| isdisjoint(s)                  | True if no common elements                | `{1,2}.isdisjoint({3,4})` → `True`                |
| issubset(s)                    | True if all elements in `s`               | `{1,2}.issubset({1,2,3})` → `True`                |
| issuperset(s)                  | True if contains all of `s`               | `{1,2,3}.issuperset({2,3})` → `True`              |
| pop()                          | Removes and returns random element        | `{1,2,3}.pop()`                                   |
| remove(x)                      | Removes element (error if missing)        | `{1,2}.remove(2)` → `{1}`                         |
| symmetric_difference(s)        | Elements in one or the other but not both | `{1,2,3}.symmetric_difference({3,4})` → `{1,2,4}` |
| symmetric_difference_update(s) | Updates with symmetric diff               | `A.symmetric_difference_update(B)`                |
| union(s)                       | Combines all unique elements              | `{1,2}.union({2,3})` → `{1,2,3}`                  |
| update(s)                      | Adds elements from another set            | `A.update(B)`                                     |

---

## **DICTIONARY METHODS**

Dictionaries store **key-value pairs**.
Example: `d = {"a": 1, "b": 2}`

| Method             | Description                               | Example                |
| ------------------ | ----------------------------------------- | ---------------------- |
| `get(key)`         | Returns value or None                     | `d.get("a")` → `1`     |
| `keys()`           | Returns all keys                          | `d.keys()`             |
| `values()`         | Returns all values                        | `d.values()`           |
| `items()`          | Returns (key, value) pairs                | `d.items()`            |
| `update(dict2)`    | Adds or updates entries                   | `d.update({"c":3})`    |
| `pop(key)`         | Removes key and returns value             | `d.pop("a")`           |
| `popitem()`        | Removes last inserted pair                | `d.popitem()`          |
| `clear()`          | Removes all                               | `d.clear()`            |
| `copy()`           | Shallow copy                              | `new_d = d.copy()`     |
| `setdefault(k, v)` | Returns value if key exists; else adds it | `d.setdefault("x", 5)` |

---
