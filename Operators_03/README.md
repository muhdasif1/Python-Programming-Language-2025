Operators in Python are **special symbols** (like `+`, `-`, `==`, `and`, etc.) that tell Python to perform a specific action, such as **addition, comparison, checking conditions**, and much more.

Think of operators as **tools** that help you do calculations, comparisons, and operations on data.

---

# **Types of Operators in Python**

Python operators are mainly divided into **7 categories**:

1. **Arithmetic Operators**
2. **Comparison (Relational) Operators**
3. **Logical Operators**
4. **Assignment Operators**
5. **Identity Operators**
6. **Membership Operators**
7. **Bitwise Operators**

---

# 1. **Arithmetic Operators**

Used for mathematical calculations.

| Operator | Meaning             | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3` → 8   |
| `-`      | Subtraction         | `5 - 3` → 2   |
| `*`      | Multiplication      | `5 * 3` → 15  |
| `/`      | Division            | `6 / 3` → 2.0 |
| `//`     | Floor Division      | `7 // 3` → 2  |
| `%`      | Modulus (Remainder) | `7 % 3` → 1   |
| `**`     | Exponent (Power)    | `2 ** 3` → 8  |

**Example Code**

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 2. **Comparison Operators**

Used to compare values (returns **True** or **False**).

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal to         |
| `!=`     | Not equal to     |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

**Example**

```python
a = 10
b = 5

print(a == b)
print(a > b)
print(a < b)
```

---

# 3. **Logical Operators**

| Operator | Meaning                      | Example            |
| -------- | ---------------------------- | ------------------ |
| `and`    | True if both conditions True | `a > 5 and b < 10` |
| `or`     | True if at least one True    | `a > 5 or b > 10`  |
| `not`    | Reverse the result           | `not(a > 5)`       |

**Example**

```python
x = True
y = False

print(x and y)
print(x or y)
print(not x)
```

---

# 4. **Assignment Operators**

| Operator | Meaning                 | Example   |
| -------- | ----------------------- | --------- |
| `=`      | Assign                  | `a = 5`   |
| `+=`     | Add and assign          | `a += 2`  |
| `-=`     | Subtract and assign     | `a -= 2`  |
| `*=`     | Multiply and assign     | `a *= 2`  |
| `/=`     | Divide and assign       | `a /= 2`  |
| `%=`     | Modulus and assign      | `a %= 3`  |
| `//=`    | Floor divide and assign | `a //= 3` |
| `**=`    | Exponent and assign     | `a **= 2` |

---

# 5. **Identity Operators**

Used to check **memory location**.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `is`     | Check if same object     |
| `is not` | Check if not same object |

**Example**

```python
a = [1, 2]
b = a

print(a is b)       # True
print(a is not b)   # False
```

---

# 6. **Membership Operators**

Used to check if an element is in a sequence.

| Operator | Meaning                     |
| -------- | --------------------------- |
| `in`     | True if element present     |
| `not in` | True if element not present |

**Example**

```python
a = [1, 2, 3]

print(2 in a)
print(5 not in a)
```

---

# 7. **Bitwise Operators**

Work with binary numbers.

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

**Example**

```python
a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(a << 1)  # 10
print(a >> 1)  # 2
```

---