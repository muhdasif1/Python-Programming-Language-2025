## Operator
In programming (and in Python specifically), an **operator** is a special symbol or keyword that tells the interpreter to perform a specific computation or manipulation on one or more values (called **operands**). You can think of operators as the verbs of your code—they take inputs, do something with them, and produce an output.

Here’s the core idea:

* **Operands** are the data you work with (literals like `5`, variables like `x`, expressions like `a + b`).
* **Operators** act on those operands to produce a result.

---
Here’s a truly exhaustive overview of every operator available in Python, grouped by category and ordered by precedence (highest to lowest). Use this as your go‑to reference!

---

## Operator Precedence (Highest → Lowest)

| Precedence Level | Operators                                                                     | Description                                        |                      |
| ---------------- | ----------------------------------------------------------------------------- | -------------------------------------------------- | -------------------- |
| 1                | `()`                                                                          | Parentheses (grouping)                             |                      |
| 2                | `x[index]`  `x[index:index]`  `x(...)`  `x.attribute`                         | Subscription, slicing, call, attribute reference   |                      |
| 3                | `**`                                                                          | Exponentiation                                     |                      |
| 4                | `+x`  `-x`  `~x`                                                              | Unary plus, unary minus, bitwise NOT               |                      |
| 5                | `*`  `/`  `//`  `%`                                                           | Multiplication, true division, floor division, mod |                      |
| 6                | `+`  `-`                                                                      | Addition, subtraction                              |                      |
| 7                | `<<`  `>>`                                                                    | Bitwise shifts                                     |                      |
| 8                | `&`                                                                           | Bitwise AND                                        |                      |
| 9                | `^`                                                                           | Bitwise XOR                                        |                      |
| 10               | \|                                                                            | Bitwise OR                                         |                      |
| 11               | `in`  `not in`                                                                | Membership tests                                   |                      |
| 12               | `is`  `is not`                                                                | Identity tests                                     |                      |
| 13               | `<`  `<=`  `>`  `>=`  `!=`  `==`                                              | Comparisons                                        |                      |
| 14               | `not`                                                                         | Boolean NOT                                        |                      |
| 15               | `and`                                                                         | Boolean AND                                        |                      |
| 16               | `or`                                                                          | Boolean OR                                         |                      |
| 17               | `if–else` (ternary)                                                           | Conditional expression                             |                      |
| 18               | `:=`                                                                          | Assignment expression (Python 3.8+)                |                      |
| 19               | `=`  `+=`  `-=`  `*=`  `/=`  `//=`  `%=`  `**=`  `<<=`  `>>=`  `&=`  `^=`  \` | =\`                                                | Assignment operators |
| 20               | `,`                                                                           | Comma (tuple packing/unpacking)                    |                      |
| 21               | `lambda`                                                                      | Lambda expression                                  |                      |

---

## 1. Arithmetic Operators

| Operator | Description                  | Example        |
| -------- | ---------------------------- | -------------- |
| `+`      | Addition                     | `2 + 3  → 5`   |
| `-`      | Subtraction                  | `5 - 2  → 3`   |
| `*`      | Multiplication               | `4 * 3  → 12`  |
| `/`      | True division (float result) | `7 / 2  → 3.5` |
| `//`     | Floor division               | `7 // 2 → 3`   |
| `%`      | Modulus (remainder)          | `7 % 3  → 1`   |
| `**`     | Exponentiation               | `2 ** 3 → 8`   |
| `+x`     | Unary plus                   | `+5    → 5`    |
| `-x`     | Unary minus                  | `-5    → -5`   |

---

## 2. Comparison (Relational) Operators

| Operator | Description              | Example           |
| -------- | ------------------------ | ----------------- |
| `==`     | Equal to                 | `5 == 5   → True` |
| `!=`     | Not equal to             | `5 != 3   → True` |
| `<`      | Less than                | `3 < 5    → True` |
| `<=`     | Less than or equal to    | `3 <= 3   → True` |
| `>`      | Greater than             | `5 > 3    → True` |
| `>=`     | Greater than or equal to | `5 >= 5   → True` |

---

## 3. Assignment Operators

| Operator | Equivalent to | Example   |               |
| -------- | ------------- | --------- | ------------- |
| `=`      | —             | `x = 10`  |               |
| `+=`     | `x = x + y`   | `x += 5`  |               |
| `-=`     | `x = x - y`   | `x -= 2`  |               |
| `*=`     | `x = x * y`   | `x *= 3`  |               |
| `/=`     | `x = x / y`   | `x /= 4`  |               |
| `//=`    | `x = x // y`  | `x //= 2` |               |
| `%=`     | `x = x % y`   | `x %= 3`  |               |
| `**=`    | `x = x ** y`  | `x **= 2` |               |
| `<<=`    | `x = x << y`  | `x <<= 1` |               |
| `>>=`    | `x = x >> y`  | `x >>= 1` |               |
| `&=`     | `x = x & y`   | `x &= y`  |               |
| `^=`     | `x = x ^ y`   | `x ^= y`  |               |
| \|=\`    | \`x = x       | y\`       | `x &#124;= y` |

---

## 4. Boolean (Logical) Operators

| Operator | Description | Example                   |
| -------- | ----------- | ------------------------- |
| `and`    | Logical AND | `True and False  → False` |
| `or`     | Logical OR  | `True or False   → True`  |
| `not`    | Logical NOT | `not True       → False`  |

---

## 5. Bitwise Operators

Operate on the binary representation of integers:

| Operator | Description | Example                         |
| -------- | ----------- | ------------------------------- |
| `&`      | Bitwise AND | `0b1010 & 0b1100 → 0b1000`      |
| \|       | Bitwise OR  | `0b1010 &#124; 0b1100 → 0b1110` |
| `^`      | Bitwise XOR | `0b1010 ^ 0b1100 → 0b0110`      |
| `~`      | Bitwise NOT | `~0b1010 → -0b1011`             |
| `<<`     | Left shift  | `0b0011 << 2 → 0b1100`          |
| `>>`     | Right shift | `0b1100 >> 2 → 0b0011`          |

---

## 6. Membership Operators

Test sequence membership:

| Operator | Description                                      | Example                 |
| -------- | ------------------------------------------------ | ----------------------- |
| `in`     | True if left operand is in right operand         | `'a' in 'cat' → True`   |
| `not in` | True if left operand is **not** in right operand | `3 not in [1,2] → True` |

---

## 7. Identity Operators

Compare object identities:

| Operator | Description                                 | Example      |
| -------- | ------------------------------------------- | ------------ |
| `is`     | True if both refer to the **same** object   | `a is b`     |
| `is not` | True if both refer to **different** objects | `a is not b` |

---

## 8. Conditional Expression (Ternary)

```python
x = 10
result = "even" if x % 2 == 0 else "odd"
# → "even"
```

---

## 9. Walrus Operator (Assignment Expression) – Python 3.8+

Assign and return in one expression:

```python
if (n := len(my_list)) > 5:
    print(f"Too many elements: {n}")
```

---

## 10. Lambda Operator

An anonymous function:

```python
square = lambda x: x*x
print(square(5))  # → 25
```

---

## 11. Comma (`,`) and Colon (`:`)

* **Comma** is used for tuple packing/unpacking, function arguments:

  ```python
  t = 1, 2, 3        # tuple packing
  a, b, c = t        # unpacking
  ```
* **Colon** appears in slices, dicts, and block headers:

  ```python
  lst[1:4]          # slicing
  d = {'a': 1}      # dict literal
  if x > 0: print(x)
  ```

---

### Putting It All Together

```python
# Precedence demo:
result = (5 + 3) * 2 ** 2 // 3 % 4   # eval order: (), **, *, //, %, +
print(result)  # → 2

# Mixed operators:
a = [1, 2, 3]
b = a                                  # identity
print(a is b)                         # True

x = 0b1010
y = 0b1100
print(x & y, x | y, x ^ y)            # bitwise ops

print("p" in "python")                # membership

# Ternary + walrus
print("Long" if (n := len(a)) > 5 else "Short", n)
```

---

❓ **Need examples of operator precedence in complex expressions?**
❓ **Want to see how custom classes implement rich comparison or in‑place operators?**
Let me know!
