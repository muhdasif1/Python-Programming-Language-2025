### ✅ What Are Operators in Python?

**Operators** in Python are **symbols or special characters** used to perform **operations** on variables and values. For example, `+` is an operator used to add two values.

---

## Categories of Operators in Python

Python provides several types of operators:

| Operator Type        | Description                         |
| -------------------- | ----------------------------------- |
| Arithmetic Operators | Perform mathematical operations     |
| Assignment Operators | Assign values to variables          |
| Comparison Operators | Compare two values                  |
| Logical Operators    | Combine conditional statements      |
| Identity Operators   | Compare memory locations            |
| Membership Operators | Test for membership in a sequence   |
| Bitwise Operators    | Perform operations on binary values |

---

## 1. Arithmetic Operators

| Operator | Name           | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `3 + 2`   | `5`    |
| `-`      | Subtraction    | `5 - 3`   | `2`    |
| `*`      | Multiplication | `4 * 2`   | `8`    |
| `/`      | Division       | `10 / 2`  | `5.0`  |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

---

## 2. Assignment Operators

| Operator | Meaning                 | Example   | Equivalent to |
| -------- | ----------------------- | --------- | ------------- |
| `=`      | Assign value            | `x = 5`   | —             |
| `+=`     | Add and assign          | `x += 3`  | `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 2`  | `x = x - 2`   |
| `*=`     | Multiply and assign     | `x *= 4`  | `x = x * 4`   |
| `/=`     | Divide and assign       | `x /= 2`  | `x = x / 2`   |
| `//=`    | Floor divide and assign | `x //= 2` | `x = x // 2`  |
| `%=`     | Modulus and assign      | `x %= 2`  | `x = x % 2`   |
| `**=`    | Exponent and assign     | `x **= 2` | `x = x ** 2`  |

---

## 3. Comparison Operators

Used to compare values. Always return `True` or `False`.

| Operator | Description              | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | `True` |
| `!=`     | Not equal to             | `5 != 3` | `True` |
| `>`      | Greater than             | `5 > 2`  | `True` |
| `<`      | Less than                | `2 < 5`  | `True` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True` |
| `<=`     | Less than or equal to    | `4 <= 6` | `True` |

---

## 4. Logical Operators

Used to combine multiple conditions.

| Operator | Description                  | Example         | Result  |
| -------- | ---------------------------- | --------------- | ------- |
| `and`    | True if both are true        | `True and True` | `True`  |
| `or`     | True if at least one is true | `True or False` | `True`  |
| `not`    | Reverses the result          | `not True`      | `False` |

---

## 5. Identity Operators

Used to compare memory locations.

| Operator | Description                       | Example      | Result       |
| -------- | --------------------------------- | ------------ | ------------ |
| `is`     | True if both refer to same object | `x is y`     | `True/False` |
| `is not` | True if not same object           | `x is not y` | `True/False` |

```python
x = [1, 2]
y = x
z = [1, 2]
print(x is y)      # True
print(x is z)      # False (different objects even with same data)
```

---

## 6. Membership Operators

Test whether a value is in a sequence.

| Operator | Description                      | Example            | Result |
| -------- | -------------------------------- | ------------------ | ------ |
| `in`     | True if value exists in sequence | `2 in [1,2,3]`     | `True` |
| `not in` | True if value not in sequence    | `5 not in [1,2,3]` | `True` |

---

## 7. Bitwise Operators (Advanced)

Work on bits (binary).

| Operator | Name        | Example  | Binary Result          |     |          |            |
| -------- | ----------- | -------- | ---------------------- | --- | -------- | ---------- |
| `&`      | AND         | `5 & 3`  | `1` (101 & 011 = 001)  |     |          |            |
| \`       | \`          | OR       | \`5                    | 3\` | `7` (101 | 011 = 111) |
| `^`      | XOR         | `5 ^ 3`  | `6` (101 ^ 011 = 110)  |     |          |            |
| `~`      | NOT         | `~5`     | `-6` (invert all bits) |     |          |            |
| `<<`     | Left Shift  | `5 << 1` | `10` (shift left by 1) |     |          |            |
| `>>`     | Right Shift | `5 >> 1` | `2` (shift right by 1) |     |          |            |

---

## Summary Table

| Type       | Examples                            |                           |
| ---------- | ----------------------------------- | ------------------------- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |                           |
| Assignment | `=`, `+=`, `-=`, `*=`, etc.         |                           |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=`    |                           |
| Logical    | `and`, `or`, `not`                  |                           |
| Identity   | `is`, `is not`                      |                           |
| Membership | `in`, `not in`                      |                           |
| Bitwise    | `&`, \`                             | `, `^`, `\~`, `<<`, `>>\` |

---



### Full Python Code: All Operators in One Place

```python

print(" 1. Arithmetic Operators")
a = 10
b = 3
print("a + b =", a + b)       # Addition
print("a - b =", a - b)       # Subtraction
print("a * b =", a * b)       # Multiplication
print("a / b =", a / b)       # Division
print("a // b =", a // b)     # Floor Division
print("a % b =", a % b)       # Modulus
print("a ** b =", a ** b)     # Exponentiation

print("\n 2. Assignment Operators")
x = 5
print("x =", x)
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 4
print("x *= 4:", x)
x /= 3
print("x /= 3:", x)
x %= 2
print("x %= 2:", x)
x = 4
x **= 2
print("x **= 2:", x)
x //= 2
print("x //= 2:", x)

print("\n 3. Comparison Operators")
a = 7
b = 5
print("a == b:", a == b)     # Equal to
print("a != b:", a != b)     # Not equal to
print("a > b:", a > b)       # Greater than
print("a < b:", a < b)       # Less than
print("a >= b:", a >= b)     # Greater or equal
print("a <= b:", a <= b)     # Less or equal

print("\n 4. Logical Operators")
x = True
y = False
print("x and y:", x and y)   # AND
print("x or y:", x or y)     # OR
print("not x:", not x)       # NOT

print("\n 5. Identity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2:", list1 is list2)       # True
print("list1 is list3:", list1 is list3)       # False
print("list1 is not list3:", list1 is not list3)

print("\n 6. Membership Operators")
fruits = ['apple', 'banana', 'cherry']
print("'banana' in fruits:", 'banana' in fruits)
print("'mango' not in fruits:", 'mango' not in fruits)

print("\n 7. Bitwise Operators")
a = 5  # binary: 0101
b = 3  # binary: 0011
print("a & b =", a & b)      # AND: 0101 & 0011 = 0001 (1)
print("a | b =", a | b)      # OR: 0101 | 0011 = 0111 (7)
print("a ^ b =", a ^ b)      # XOR: 0101 ^ 0011 = 0110 (6)
print("~a =", ~a)            # NOT: ~0101 = -(0101 + 1) = -6
print("a << 1 =", a << 1)    # Left shift: 1010 (10)
print("a >> 1 =", a >> 1)    # Right shift: 0010 (2)
```

---
