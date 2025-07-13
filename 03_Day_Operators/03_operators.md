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