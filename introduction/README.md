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

## **Python Input and Output**

In Python, **input** and **output** are used to interact with the user.

* **Input** means taking data from the user
* **Output** means displaying data to the user

---

## **Python Output**

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

## **Python Input**

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

## **Taking Multiple Inputs**

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum =", x + y)
```

---

## **Input and Output in One Program**

```python
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print(f"Student Name: {name}")
print(f"Marks: {marks}")
```

---

## **Common Mistakes**

❌ Forgetting type conversion:

```python
x = input("Enter number: ")
y = input("Enter number: ")
print(x + y)   # Wrong: adds strings
```

✅ Correct way:

```python
x = int(input("Enter number: "))
y = int(input("Enter number: "))
print(x + y)
```

---

## **Summary**

| Function  | Purpose               |
| --------- | --------------------- |
| `input()` | Takes input from user |
| `print()` | Displays output       |
| `int()`   | Converts to integer   |
| `float()` | Converts to decimal   |

---

