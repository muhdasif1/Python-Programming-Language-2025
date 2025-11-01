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

## 🧵 **STRING METHODS**

Strings are sequences of characters (text).
Example: `s = "Hello World"`

| Method               | Description                               | Example                                   |
| -------------------- | ----------------------------------------- | ----------------------------------------- |
| `s.upper()`          | Converts all letters to uppercase         | `"hello".upper()` → `"HELLO"`             |
| `s.lower()`          | Converts all letters to lowercase         | `"HELLO".lower()` → `"hello"`             |
| `s.title()`          | Capitalizes the first letter of each word | `"hello world".title()` → `"Hello World"` |
| `s.capitalize()`     | Capitalizes the first letter only         | `"hello".capitalize()` → `"Hello"`        |
| `s.strip()`          | Removes spaces from start and end         | `" hello ".strip()` → `"hello"`           |
| `s.replace(a, b)`    | Replaces `a` with `b`                     | `"hello".replace("l", "x")` → `"hexxo"`   |
| `s.split(delimiter)` | Splits string into list                   | `"a,b,c".split(",")` → `["a","b","c"]`    |
| `s.join(list)`       | Joins list into string                    | `",".join(["a","b"])` → `"a,b"`           |
| `s.find(sub)`        | Returns index of substring                | `"hello".find("e")` → `1`                 |
| `s.count(sub)`       | Counts occurrences                        | `"banana".count("a")` → `3`               |
| `s.isalpha()`        | True if all letters                       | `"abc".isalpha()` → `True`                |
| `s.isdigit()`        | True if all digits                        | `"123".isdigit()` → `True`                |
| `s.startswith(x)`    | Checks if starts with x                   | `"hello".startswith("he")` → `True`       |
| `s.endswith(x)`      | Checks if ends with x                     | `"hello".endswith("lo")` → `True`         |

---

## 🔢 **INTEGER (int) METHODS**

Integers are numbers without decimals.
Integers don’t have many “methods,” but you can use **built-in functions** on them:

| Function/Method | Description                   | Example                   |
| --------------- | ----------------------------- | ------------------------- |
| `abs(x)`        | Absolute value                | `abs(-5)` → `5`           |
| `pow(x, y)`     | Power of x^y                  | `pow(2, 3)` → `8`         |
| `divmod(a, b)`  | Returns (quotient, remainder) | `divmod(9, 2)` → `(4, 1)` |
| `int(x)`        | Converts to integer           | `int("12")` → `12`        |
| `bit_length()`  | Number of bits to represent   | `(10).bit_length()` → `4` |

---

## 🧮 **LIST METHODS**

Lists are mutable (changeable) sequences.
Example: `lst = [1, 2, 3]`

| Method             | Description                 | Example                       |
| ------------------ | --------------------------- | ----------------------------- |
| `append(x)`        | Adds an element at end      | `lst.append(4)` → `[1,2,3,4]` |
| `extend(iterable)` | Adds multiple elements      | `lst.extend([5,6])`           |
| `insert(i, x)`     | Adds at index i             | `lst.insert(1, 99)`           |
| `remove(x)`        | Removes first occurrence    | `lst.remove(2)`               |
| `pop(i)`           | Removes and returns element | `lst.pop(0)` → removes first  |
| `clear()`          | Empties list                | `lst.clear()`                 |
| `index(x)`         | Returns index of x          | `lst.index(3)`                |
| `count(x)`         | Counts x                    | `[1,1,2].count(1)` → `2`      |
| `sort()`           | Sorts list ascending        | `lst.sort()`                  |
| `reverse()`        | Reverses list               | `lst.reverse()`               |
| `copy()`           | Shallow copy                | `b = lst.copy()`              |

---

## 🔗 **TUPLE METHODS**

Tuples are like lists but **immutable** (cannot be changed).
Example: `t = (1, 2, 3)`

| Method     | Description        | Example                  |
| ---------- | ------------------ | ------------------------ |
| `count(x)` | Counts x in tuple  | `(1,1,2).count(1)` → `2` |
| `index(x)` | Returns index of x | `(1,2,3).index(2)` → `1` |

---

## 🧩 **SET METHODS**

Sets are unordered collections with no duplicates.
Example: `s = {1, 2, 3}`

| Method                    | Description                    | Example                         |
| ------------------------- | ------------------------------ | ------------------------------- |
| `add(x)`                  | Adds element                   | `s.add(4)`                      |
| `remove(x)`               | Removes x (error if not found) | `s.remove(2)`                   |
| `discard(x)`              | Removes x (no error)           | `s.discard(10)`                 |
| `pop()`                   | Removes random element         | `s.pop()`                       |
| `clear()`                 | Removes all                    | `s.clear()`                     |
| `union(t)`                | Combines sets                  | `s.union({4,5})`                |
| `intersection(t)`         | Common elements                | `s.intersection({2,3,4})`       |
| `difference(t)`           | Elements not in t              | `s.difference({2,4})`           |
| `symmetric_difference(t)` | Elements in one set only       | `s.symmetric_difference({2,4})` |
| `issubset(t)`             | True if subset                 | `{1,2}.issubset({1,2,3})`       |
| `issuperset(t)`           | True if superset               | `{1,2,3}.issuperset({1,2})`     |

---

## 🗂️ **DICTIONARY METHODS**

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
