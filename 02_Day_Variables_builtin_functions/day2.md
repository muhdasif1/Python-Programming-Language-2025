### Built in functions in python?
Python provides many **built-in functions** that you can use without importing any library. These functions are always available and help with common programming tasks.

---

###  **Most Common Built-in Functions in Python**

| Function       | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| `print()`      | Displays output to the console                              |
| `input()`      | Takes input from the user                                   |
| `len()`        | Returns the length of a sequence (like string, list, tuple) |
| `type()`       | Returns the type of an object                               |
| `int()`        | Converts a value to an integer                              |
| `float()`      | Converts a value to a float                                 |
| `str()`        | Converts a value to a string                                |
| `list()`       | Converts a value to a list                                  |
| `dict()`       | Creates a dictionary                                        |
| `range()`      | Returns a sequence of numbers                               |
| `sum()`        | Returns the sum of items in an iterable                     |
| `max()`        | Returns the maximum value                                   |
| `min()`        | Returns the minimum value                                   |
| `abs()`        | Returns absolute (positive) value                           |
| `round()`      | Rounds a number to the nearest integer                      |
| `sorted()`     | Returns a sorted list from the given iterable               |
| `help()`       | Opens the help system                                       |
| `id()`         | Returns the unique ID of an object                          |
| `isinstance()` | Checks if an object is an instance of a class               |
| `zip()`        | Combines multiple iterables element-wise                    |

---
### What is a **Variable** in Python?

A **variable** is like a **container** in memory that stores data (like numbers, text, lists, etc.) so you can use it later in your program.

---

###  **How to create a variable in Python**

```python
x = 5             # x is a variable storing an integer
name = "Muhammad Asif"      # name is a variable storing a string
pi = 3.14         # pi stores a float (decimal)
is_valid = True   # stores a boolean value (True/False)
```

---

### **Variable Rules in Python**

1. Must **start with a letter** (a–z, A–Z) or underscore `_`
2. Cannot start with a number
3. Can only contain **letters, numbers, and underscores**
4. **Case-sensitive** (`Name` ≠ `name`)

✅ Valid:

```python
user_name = "Muhammad Asif"
_age = 20
score2 = 100
```

❌ Invalid:

```python
2score = 100      # starts with a number
user-name = "Muhammad Asif" # hyphens are not allowed
```

---

###  **Types of Variables (by value)**

| Variable            | Value          | Type    |
| ------------------- | -------------- | ------- |
| `x = 10`            | Integer        | `int`   |
| `name = "Asif"`      | Text           | `str`   |
| `pi = 3.14`         | Decimal number | `float` |
| `flag = True`       | Boolean        | `bool`  |
| `marks = [1, 2, 3]` | List           | `list`  |

---

### Check Variable Type

```python
x = 5
print(type(x))   # <class 'int'>
```

---

### Memory Concept

When you write:

```python
x = 10
```

Python stores the value `10` in memory and gives it the label `x`. Later, you can use `x` to refer to that value.

---
