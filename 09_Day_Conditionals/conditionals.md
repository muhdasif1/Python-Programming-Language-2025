## What Are Conditionals?

**Conditionals** are used to **make decisions** in Python.
They allow the program to **execute certain code blocks only if a condition is true**.

---

## Python Conditional Statements:

1. `if`
2. `if...else`
3. `if...elif...else`
4. Nested `if`
5. Conditional Expressions (`?:` alternative using ternary)

---

## 1. `if` Statement

Used to run code **only when the condition is true**.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

**Output:**
`You are an adult`

---

## 2. `if...else` Statement

Runs one block **if true**, another **if false**.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Output:**
`Minor`

---

## 3. `if...elif...else` Statement

Used for **multiple conditions**.

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Fail")
```

**Output:**
`Grade: C`

---

## 4. Nested `if` Statements

`if` inside another `if`.

```python
number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not positive")
```

**Output:**
`Positive odd number`

---

## 5. Ternary Operator (Short If-Else)

One-line conditional expression.

```python
age = 22
status = "Adult" if age >= 18 else "Minor"
print("You are:", status)
```

**Output:**
`You are: Adult`

---

## Conditional Operators

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

---

## Practice Example: Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Summary:

* Use `if` for one condition
* Use `if...else` when you have two options
* Use `if...elif...else` for more choices
* Use nested `if` for conditions inside other conditions
* Use ternary for compact one-line checks

---