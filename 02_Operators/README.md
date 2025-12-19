# **1. Arithmetic Operators**

Used for basic math operations.

| Operator | Meaning             | Example  | Output |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | 8      |
| `-`      | Subtraction         | `5 - 3`  | 2      |
| `*`      | Multiplication      | `5 * 3`  | 15     |
| `/`      | Division            | `5 / 2`  | 2.5    |
| `//`     | Floor division      | `5 // 2` | 2      |
| `%`      | Modulus (remainder) | `5 % 2`  | 1      |
| `**`     | Exponent            | `5 ** 2` | 25     |

**Example Code:**

```python
a = 5
b = 2

print(a + b)  # 7
print(a - b)  # 3
print(a * b)  # 10
print(a / b)  # 2.5
print(a // b) # 2
print(a % b)  # 1
print(a ** b) # 25
```

---

# **2. Assignment Operators**

Used to assign values to variables, sometimes combined with arithmetic.

| Operator | Example   | Meaning                  |      |       |                |
| -------- | --------- | ------------------------ | ---- | ----- | -------------- |
| `=`      | `a = 5`   | Assign 5 to a            |      |       |                |
| `+=`     | `a += 3`  | a = a + 3                |      |       |                |
| `-=`     | `a -= 3`  | a = a - 3                |      |       |                |
| `*=`     | `a *= 3`  | a = a * 3                |      |       |                |
| `/=`     | `a /= 3`  | a = a / 3                |      |       |                |
| `//=`    | `a //= 3` | a = a // 3               |      |       |                |
| `%=`     | `a %= 3`  | a = a % 3                |      |       |                |
| `**=`    | `a **= 3` | a = a ** 3               |      |       |                |
| `&=`     | `a &= 3`  | a = a & 3 (bitwise AND)  |      |       |                |
| `        | =`        | `a                       | = 3` | a = a | 3 (bitwise OR) |
| `^=`     | `a ^= 3`  | a = a ^ 3 (bitwise XOR)  |      |       |                |
| `<<=`    | `a <<= 3` | a = a << 3 (left shift)  |      |       |                |
| `>>=`    | `a >>= 3` | a = a >> 3 (right shift) |      |       |                |

---

# **3. Comparison Operators**

Used to compare two values. Returns **True** or **False**.

| Operator | Meaning          | Example          |
| -------- | ---------------- | ---------------- |
| `==`     | Equal            | `5 == 5` → True  |
| `!=`     | Not equal        | `5 != 3` → True  |
| `>`      | Greater than     | `5 > 3` → True   |
| `<`      | Less than        | `5 < 3` → False  |
| `>=`     | Greater or equal | `5 >= 5` → True  |
| `<=`     | Less or equal    | `5 <= 3` → False |

---

# **4. Logical Operators**

Used to combine **boolean** values (`True` or `False`).

| Operator | Meaning                 | Example                  |
| -------- | ----------------------- | ------------------------ |
| `and`    | True if **both** true   | `True and False` → False |
| `or`     | True if **any** is true | `True or False` → True   |
| `not`    | Reverses boolean        | `not True` → False       |

**Example:**

```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

# **5. Bitwise Operators**

Operate on **binary numbers** (bits).

| Operator | Meaning      | Example       |    |        |
| -------- | ------------ | ------------- | -- | ------ |
| `&`      | AND          | `5 & 3` → 1   |    |        |
| `        | `            | OR            | `5 | 3` → 7 |
| `^`      | XOR          | `5 ^ 3` → 6   |    |        |
| `~`      | NOT (invert) | `~5` → -6     |    |        |
| `<<`     | Left shift   | `5 << 1` → 10 |    |        |
| `>>`     | Right shift  | `5 >> 1` → 2  |    |        |

**Example:**

```python
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1  (0001)
print(a | b)  # 7  (0111)
print(a ^ b)  # 6  (0110)
print(~a)     # -6
print(a << 1) # 10
print(a >> 1) # 2
```

---

# **6. Identity Operators**

Check if two variables **refer to the same object** in memory.

| Operator | Meaning                 | Example      |
| -------- | ----------------------- | ------------ |
| `is`     | True if same object     | `x is y`     |
| `is not` | True if not same object | `x is not y` |

**Example:**

```python
x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)      # True
print(x is z)      # False
print(x is not z)  # True
```

---

# **7. Membership Operators**

Check if a **value is in a collection** (like list, string, tuple).

| Operator | Meaning                     | Example                     |
| -------- | --------------------------- | --------------------------- |
| `in`     | True if value exists        | `'a' in 'apple'` → True     |
| `not in` | True if value doesn't exist | `'b' not in 'apple'` → True |

**Example:**

```python
fruits = ['apple', 'banana']

print('apple' in fruits)     # True
print('cherry' not in fruits) # True
```

---

# **8. Python Operator Precedence**

Operators at the **top** have **higher precedence** (executed first), and operators at the **bottom** have **lower precedence** (executed later).

| Precedence | Operator Type                                  | Example           | Description                                           |    |            |
| ---------- | ---------------------------------------------- | ----------------- | ----------------------------------------------------- | -- | ---------- |
| 1          | `()`                                           | `(2 + 3) * 4`     | Parentheses — expressions inside `()` evaluated first |    |            |
| 2          | `**`                                           | `2 ** 3 ** 2`     | Exponentiation                                        |    |            |
| 3          | `+x, -x, ~x`                                   | `-5, +5, ~5`      | Unary plus, minus, bitwise NOT                        |    |            |
| 4          | `*, /, //, %`                                  | `5 * 2, 5 / 2`    | Multiplication, Division, Floor Division, Modulus     |    |            |
| 5          | `+, -`                                         | `5 + 2, 5 - 2`    | Addition, Subtraction                                 |    |            |
| 6          | `<<, >>`                                       | `2 << 1, 4 >> 1`  | Bitwise Shift Left, Shift Right                       |    |            |
| 7          | `&`                                            | `5 & 3`           | Bitwise AND                                           |    |            |
| 8          | `^`                                            | `5 ^ 3`           | Bitwise XOR                                           |    |            |
| 9          | `                                              | `                 | `5                                                    | 3` | Bitwise OR |
| 10         | `==, !=, >, >=, <, <=, is, is not, in, not in` | `5 == 3, x is y`  | Comparison, Identity, Membership                      |    |            |
| 11         | `not`                                          | `not True`        | Logical NOT                                           |    |            |
| 12         | `and`                                          | `True and False`  | Logical AND                                           |    |            |
| 13         | `or`                                           | `True or False`   | Logical OR                                            |    |            |
| 14         | `lambda`                                       | `lambda x: x + 1` | Lambda expression                                     |    |            |

---

## **Key Points to Remember**

1. **Parentheses `()` always override** precedence. Use them to make your code readable.
2. Exponentiation `**` is **right-associative**, so `2 ** 3 ** 2` equals `2 ** (3 ** 2)` = 512, **not** `(2 ** 3) ** 2`.
3. Multiplication/division (`* / // %`) is done **before** addition/subtraction (`+ -`).
4. Logical operators `not > and > or` are evaluated in that order.
5. Identity (`is`) and Membership (`in`) operators come **after bitwise** and **before logical NOT**.

---

## **Example**

```python
x = 2 + 3 * 4
y = (2 + 3) * 4
z = 2 ** 3 ** 2
a = True or False and False

print(x)  # 14  -> 3*4=12 then 2+12
print(y)  # 20  -> parentheses first: 2+3=5 then 5*4
print(z)  # 512 -> 3**2=9 then 2**9=512
print(a)  # True -> AND before OR: False and False=False, True or False=True
```

---

