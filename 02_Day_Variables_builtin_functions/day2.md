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

Here is a **step-by-step explanation** of each of these **built-in Python functions**, along with **simple example code** so you can learn them clearly:

---

### 1. `print()`

**Use:** Displays output on the console.

```python
print("Hello, Muhammad Asif!")  # Output: Hello, Muhammad Asif!
```

---

### 2. `input()`

**Use:** Takes input from the user as a string.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

### 3. `len()`

**Use:** Returns the length (number of items) of a sequence (like string, list).

```python
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4
```

---

### 4. `type()`

**Use:** Shows the data type of a value.

```python
age = 25
print(type(age))  # Output: <class 'int'>
```

---

### 5. `int()`

**Use:** Converts a value to an integer.

```python
num = int("10")
print(num + 5)  # Output: 15
```

---

### 6. `float()`

**Use:** Converts a value to a float.

```python
num = float("3.14")
print(num + 1.0)  # Output: 4.14
```

---

### 7. `str()`

**Use:** Converts a value to a string.

```python
age = 22
text = str(age)
print("My age is " + text)  # Output: My age is 22
```

---

### 8. `list()`

**Use:** Converts a sequence (string, tuple, etc.) into a list.

```python
name = "Asif"
print(list(name))  # Output: ['A', 's', 'i', 'f']
```

---

### 9. `dict()`

**Use:** Creates a dictionary.

```python
person = dict(name="Asif", age=20)
print(person)  # Output: {'name': 'Asif', 'age': 20}
```

---

### 10. `range()`

**Use:** Generates a sequence of numbers.

```python
for i in range(3):
    print(i)  # Output: 0 1 2
```

---

### 11. `sum()`

**Use:** Adds all items in an iterable.

```python
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6
```

---

### 12. `max()`

**Use:** Returns the highest value.

```python
marks = [45, 78, 89, 34]
print(max(marks))  # Output: 89
```

---

### 13. `min()`

**Use:** Returns the smallest value.

```python
marks = [45, 78, 89, 34]
print(min(marks))  # Output: 34
```

---

### 14. `abs()`

**Use:** Returns the absolute value (no negative sign).

```python
num = -10
print(abs(num))  # Output: 10
```

---

### 15. `round()`

**Use:** Rounds a float to the nearest integer.

```python
pi = 3.14159
print(round(pi))  # Output: 3
```

---

### 16. `sorted()`

**Use:** Returns a new sorted list.

```python
data = [3, 1, 4, 2]
print(sorted(data))  # Output: [1, 2, 3, 4]
```

---

### 17. `help()`

**Use:** Opens help documentation for functions and modules.

```python
help(len)  # Shows the help for len function
```

---

### 18. `id()`

**Use:** Returns the unique ID of an object in memory.

```python
a = 5
print(id(a))  # Output: Unique memory ID (will vary)
```

---

### 19. `isinstance()`

**Use:** Checks if a value is a specific type.

```python
num = 10
print(isinstance(num, int))  # Output: True
```

---

### 20. `zip()`

**Use:** Combines elements from multiple iterables.

```python
names = ['Asif', 'Ali']
scores = [90, 85]
result = list(zip(names, scores))
print(result)  # Output: [('Asif', 90), ('Ali', 85)]
```

---
### What is a **Variable** in Python?

A **variable** is like a **container** in memory that stores data (like numbers, text, lists, etc.) so you can use it later in your program.



###  **How to create a variable in Python**

```python
x = 5             # x is a variable storing an integer
name = "Muhammad Asif"      # name is a variable storing a string
pi = 3.14         # pi stores a float (decimal)
is_valid = True   # stores a boolean value (True/False)
```



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



###  **Types of Variables (by value)**

| Variable            | Value          | Type    |
| ------------------- | -------------- | ------- |
| `x = 10`            | Integer        | `int`   |
| `name = "Asif"`      | Text           | `str`   |
| `pi = 3.14`         | Decimal number | `float` |
| `flag = True`       | Boolean        | `bool`  |
| `marks = [1, 2, 3]` | List           | `list`  |



### Check Variable Type

```python
x = 5
print(type(x))   # <class 'int'>
```



### Memory Concept

When you write:

```python
x = 10
```

Python stores the value `10` in memory and gives it the label `x`. Later, you can use `x` to refer to that value.



### Declaring Multiple Variables in One Line — Python

Yes! In Python, you can declare **multiple variables in a single line**. There are two main ways to do this:



### 1. **Assigning Different Values to Different Variables**

```python
x, y, z = 10, 20, 30
print(x)  # 10
print(y)  # 20
print(z)  # 30
```

 *Each variable gets its own value in order.*



### 2. **Assigning the Same Value to Multiple Variables**

```python
a = b = c = 100
print(a)  # 100
print(b)  # 100
print(c)  # 100
```

*All three variables point to the same value `100`.*



### 3. **Unpacking a List or Tuple into Variables**

```python
data = [1, 2, 3]
x, y, z = data
print(x, y, z)  # 1 2 3
```

> Useful when you have a sequence and want to extract values into separate variables.



### Must Match the Number of Values and Variables

```python
x, y = 5, 10, 15  # Error: too many values
```

```python
x, y, z = 5, 10   # Error: not enough values
```

---

### What Are **Data Types** in Python?

**Data types** define the **type of data** a variable holds — like a number, text, list, etc. Python automatically detects the data type when you assign a value.



### **Built-in Data Types in Python**

Let’s break them down with simple examples:

| Category  | Data Type    | Example                      |
| --------- | ------------ | ---------------------------- |
| Text      | `str`        | `"Hello"`                    |
| Numeric   | `int`        | `5`                          |
|           | `float`      | `3.14`                       |
|           | `complex`    | `2 + 3j`                     |
| Sequence  | `list`       | `[1, 2, 3]`                  |
|           | `tuple`      | `(1, 2, 3)`                  |
|           | `range`      | `range(5)`                   |
| Mapping   | `dict`       | `{"name": "Ali", "age": 20}` |
| Set       | `set`        | `{1, 2, 3}`                  |
|           | `frozenset`  | `frozenset({1, 2, 3})`       |
| Boolean   | `bool`       | `True`, `False`              |
| Binary    | `bytes`      | `b"abc"`                     |
|           | `bytearray`  | `bytearray(5)`               |
|           | `memoryview` | `memoryview(bytes(5))`       |
| None Type | `NoneType`   | `None`                       |



### **Examples**

```python
# Text
name = "Asif"           # str

# Numbers
age = 21                # int
pi = 3.14               # float
z = 3 + 4j              # complex

# Sequence
fruits = ["apple", "banana"]  # list
points = (1, 2, 3)             # tuple
count = range(5)              # range

# Mapping
student = {"name": "Ali", "age": 18}  # dict

# Set
colors = {"red", "blue"}      # set

# Boolean
is_valid = True               # bool

# None
x = None                      # NoneType
```



### Check the Type of a Variable

```python
x = 10
print(type(x))   # Output: <class 'int'>
```



### Python is **Dynamically Typed**

You don’t need to declare a type — Python figures it out:

```python
x = 5        # x is int
x = "Hello"  # now x is str
```

---

### **Numbers in Python**

In Python, **Numbers** are a basic data type used to store numeric values. There are 3 main types of numbers:



### **1. Integer (`int`)**

* Whole numbers (positive or negative)
* No decimal point

```python
x = 10
y = -5
print(type(x))  # <class 'int'>
```



### **2. Float (`float`)**

* Numbers **with decimal points**
* Used for **real numbers**

```python
pi = 3.14
temp = -27.5
print(type(pi))  # <class 'float'>
```



### **3. Complex (`complex`)**

* Used in **advanced math**
* Has a real and imaginary part
* Written as: `real + imagj`

```python
z = 2 + 3j
print(type(z))  # <class 'complex'>
```



### **Basic Math Operations**

```python
a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus (remainder) → 1
print(a ** b)  # Exponent (power) → 1000
```



### **Type Conversion**

Convert between number types:

```python
x = 10        # int
y = float(x)  # float
z = int(3.9)  # int (truncates to 3)

print(y)  # 10.0
print(z)  # 3
```



### Extra: `isinstance()` to Check Type

```python
print(isinstance(10, int))      # True
print(isinstance(3.14, float))  # True
```



### Summary

| Type      | Description              | Example        |
| --------- | ------------------------ | -------------- |
| `int`     | Whole numbers            | `5`, `-10`     |
| `float`   | Decimal numbers          | `3.14`, `-9.8` |
| `complex` | Real + Imaginary numbers | `2 + 3j`       |

---

