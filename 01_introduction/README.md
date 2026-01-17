# **What is Python?**

Python is a high-level, popular programming language known for its simplicity and readability. It was created by **Guido van Rossum** and first released in **1991**. Python is widely used across many fields due to its versatility and ease of use.

---

# **Uses of Python**

Python is used in many areas of software development, including:

* **Web development** (server-side applications)
* **Software development**
* **Mathematics and scientific computing**
* **System scripting and automation**
* **Data analysis and big data processing**
* **Artificial Intelligence and Machine Learning**

---

# **What Can Python Do?**

Python provides powerful capabilities, such as:

* Creating **web applications** on servers
* Automating tasks and building **software workflows**
* Connecting to and working with **database systems**
* Reading, writing, and modifying **files**
* Handling **big data** and performing **complex mathematical operations**
* Supporting **rapid prototyping** as well as **production-ready software development**

---

# **Why Choose Python?**

Python is one of the most preferred programming languages because:

* It works on multiple platforms such as **Windows, macOS, Linux, and Raspberry Pi**
* It has a **simple syntax** that closely resembles the English language
* Developers can write programs using **fewer lines of code** compared to many other languages
* It uses an **interpreter system**, allowing code to run immediately after it is written
* It supports multiple programming paradigms:

  * Procedural programming
  * Object-Oriented programming
  * Functional programming

---

# **Python Input and Output**

In Python, **input** and **output** are used to interact with the user.

* **Input** means taking data from the user
* **Output** means displaying data to the user

---

# **Python Output**

Python uses the **`print()`** function to display output on the screen.

### **Example 1: Simple Output**

```python
print("Hello, Python!")
```

**Output:**

```
Hello, Python!
```

---

### **Example 2: Printing Variables**

```python
name = "Asif"
age = 20
print(name)
print(age)
```

---

### **Example 3: Multiple Values in `print()`**

```python
name = "Asif"
age = 20
print("Name:", name, "Age:", age)
```

---

### **Example 4: Using f-strings (Recommended)**

```python
name = "Asif"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

---

# **Python Input**

Python uses the **`input()`** function to take input from the user.

⚠️ **Important:**
The `input()` function always returns data as a **string**.

---

### **Example 1: Simple Input**

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

### **Example 2: Input with Numbers**

Since input is a string, we must convert it to a number.

```python
age = int(input("Enter your age: "))
print("You are", age, "years old")
```

---

### **Example 3: Float Input**

```python
price = float(input("Enter product price: "))
print("Price is:", price)
```

---

# **Taking Multiple Inputs**

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum =", x + y)
```

---

# **Input and Output in One Program**

```python
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print(f"Student Name: {name}")
print(f"Marks: {marks}")
```

---

# **Common Mistakes**

Forgetting type conversion:

```python
x = input("Enter number: ")
y = input("Enter number: ")
print(x + y)   # Wrong: adds strings
```

 Correct way:

```python
x = int(input("Enter number: "))
y = int(input("Enter number: "))
print(x + y)
```

---

# **Summary**

| Function  | Purpose               |
| --------- | --------------------- |
| `input()` | Takes input from user |
| `print()` | Displays output       |
| `int()`   | Converts to integer   |
| `float()` | Converts to decimal   |

---

# **Python Comments**

**Comments** in Python are used to explain code.
They help programmers understand what the code does and make programs easier to read and maintain.

👉 Comments are **ignored by Python** and do not affect program execution.

---

## Why Use Comments?

* To explain **logic and purpose** of code
* To make code **readable**
* To help **others (and yourself)** understand the code later
* To temporarily **disable code** during testing

---

## Types of Comments in Python

Python mainly supports **two types of comments**:

---

## 1. Single-Line Comments

Single-line comments start with the **`#`** symbol.

### Example:

```python
# This is a single-line comment
print("Hello Python")  # This comment explains the line
```

---

## 2. Multi-Line Comments

Python does not have a special syntax for multi-line comments.
However, they are commonly written using:

### Method 1: Multiple `#`

```python
# This is a multi-line comment
# It is written using
# multiple hash symbols
```

### Method 2: Triple Quotes (Docstrings)

Triple quotes are often used for **documentation**.

```python
"""
This is a multi-line comment.
It is mostly used to explain
functions, classes, or modules.
"""
print("Python Comments")
```

⚠️ Note: Triple-quoted strings are technically **docstrings**, not comments, but they are often used like comments.

---

## Comments in Functions

```python
def add(a, b):
    # This function adds two numbers
    return a + b
```

---

## Commenting Out Code (Debugging)

```python
print("This line runs")
# print("This line is disabled")
```

---

## Good Commenting Practices

✅ Write **clear and meaningful** comments
✅ Explain **why**, not just **what**
❌ Avoid obvious comments

### Bad Example:

```python
x = 5  # Assign 5 to x
```

### Good Example:

```python
x = 5  # Number of students in class
```

---

## Summary

| Type        | Syntax           | Use                |
| ----------- | ---------------- | ------------------ |
| Single-line | `#`              | Short explanations |
| Multi-line  | `#` or `""" """` | Documentation      |
| Inline      | After code       | Quick notes        |

---

# **Python Variables**

A **variable** in Python is used to **store data** in memory.
You can think of a variable as a **container** that holds a value which can be used and changed later in a program.

---

# **Creating Variables**

In Python, you **do not need to declare a variable type**.
A variable is created when you assign a value to it.

```python
name = "Asif"
age = 20
marks = 85.5
```

---

# **Rules for Naming Variables**

* Must start with a **letter (a–z, A–Z)** or **underscore (_)**
* Cannot start with a number
* Can contain letters, numbers, and underscores
* Variable names are **case-sensitive**

✅ Valid:

```python
student_name
_age
totalMarks
```

❌ Invalid:

```python
1name
total-marks
class
```

---

# **Types of Variables (Based on Values)**

```python
name = "Ali"        # String
age = 18            # Integer
height = 5.7        # Float
is_student = True   # Boolean
```

---

# **Changing Variable Values**

The value of a variable can be changed anytime.

```python
age = 18
age = 19
print(age)
```

---

# **Multiple Variable Assignment**

```python
x, y, z = 10, 20, 30
```

Assigning the same value to multiple variables:

```python
a = b = c = 100
```

---

# **Using Variables in Output**

```python
name = "Asif"
marks = 90
print("Name:", name)
print("Marks:", marks)
```

Using f-strings:

```python
print(f"Name: {name}, Marks: {marks}")
```

---

# **Why Variables Are Important**

* Store user input
* Perform calculations
* Reuse data
* Make programs flexible and dynamic

---

## **Summary**

* Variables store data
* No data type declaration needed
* Values can be changed
* Python decides the data type automatically

---

# **Python Data Types**

In programming, a **data type** defines the kind of value a variable can store.
Different data types allow different operations to be performed on the data.

Python has many **built-in data types**, and you do **not need to declare them explicitly**.
Python automatically assigns the data type based on the value.

---

# **Built-in Data Types in Python**

Python provides the following built-in data types, grouped into categories:

---

## 1. Text Type

### `str` (String)

Used to store text data.

```python
name = "Python"
```

---

## 2. Numeric Types

### `int` (Integer)

Whole numbers without decimals.

```python
x = 10
```

### `float` (Floating-point)

Numbers with decimals.

```python
y = 3.14
```

### `complex`

Numbers with a real and imaginary part.

```python
z = 2 + 3j
```

---

## 3. Sequence Types

### `list`

Ordered, changeable collection.

```python
fruits = ["apple", "banana", "mango"]
```

### `tuple`

Ordered, unchangeable collection.

```python
colors = ("red", "green", "blue")
```

### `range`

Sequence of numbers.

```python
numbers = range(1, 5)
```

---

## 4. Mapping Type

### `dict` (Dictionary)

Stores data in key-value pairs.

```python
student = {"name": "Asif", "age": 20}
```

---

## 5. Set Types

### `set`

Unordered collection with no duplicates.

```python
unique_numbers = {1, 2, 3}
```

### `frozenset`

Unchangeable set.

```python
fs = frozenset([1, 2, 3])
```

---

## 6. Boolean Type

### `bool`

Represents `True` or `False`.

```python
is_active = True
```

---

## 7. Binary Types

### `bytes`

Immutable sequence of bytes.

```python
b = bytes(5)
```

### `bytearray`

Mutable sequence of bytes.

```python
ba = bytearray(5)
```

### `memoryview`

Access memory of binary objects.

```python
mv = memoryview(bytes(5))
```

---

## 8. None Type

### `NoneType`

Represents absence of a value.

```python
x = None
```

---

# **Checking Data Type**

You can check the data type using the `type()` function:

```python
x = 10
print(type(x))
```

---

# **Summary Table**

| Category | Data Types                         |
| -------- | ---------------------------------- |
| Text     | `str`                              |
| Numeric  | `int`, `float`, `complex`          |
| Sequence | `list`, `tuple`, `range`           |
| Mapping  | `dict`                             |
| Set      | `set`, `frozenset`                 |
| Boolean  | `bool`                             |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| None     | `NoneType`                         |

---