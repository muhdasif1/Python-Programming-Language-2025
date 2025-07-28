## What is a Dictionary in Python?

A **dictionary** in Python is an **unordered, mutable collection** of **key-value pairs**.

### Key Points:

* Keys must be **unique** and **immutable** (e.g., strings, numbers, tuples).
* Values can be **any type** (strings, lists, other dictionaries, etc.).
* Denoted by `{}` curly braces.

```python
# Example dictionary
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}
print(person)
```

---

## Dictionary Creation Methods

### 1. Using `{}`

```python
d = {"a": 1, "b": 2}
```

### 2. Using `dict()`

```python
d = dict(a=1, b=2)
```

### 3. From list of tuples

```python
d = dict([("a", 1), ("b", 2)])
```

---

## Common Dictionary Operations

### Access value by key

```python
print(person["name"])  # Ali
```

### Add or update

```python
person["email"] = "ali@example.com"
```

### Delete a key

```python
del person["age"]
```

### Check if key exists

```python
if "city" in person:
    print("City exists")
```

---

## Dictionary Iteration

```python
for key in person:
    print(key, "=>", person[key])

# OR
for key, value in person.items():
    print(key, ":", value)
```

---

## Dictionary Methods Explained

| Method         | Description                             | Example                          |
| -------------- | --------------------------------------- | -------------------------------- |
| `clear()`      | Removes all items                       | `d.clear()`                      |
| `copy()`       | Returns a shallow copy                  | `d2 = d.copy()`                  |
| `fromkeys()`   | Creates a new dict from keys            | `dict.fromkeys(["a", "b"], 0)`   |
| `get()`        | Returns value for key (or default)      | `d.get("x", "Not found")`        |
| `items()`      | Returns key-value pairs                 | `for k, v in d.items()`          |
| `keys()`       | Returns all keys                        | `list(d.keys())`                 |
| `values()`     | Returns all values                      | `list(d.values())`               |
| `pop()`        | Removes item by key                     | `d.pop("name")`                  |
| `popitem()`    | Removes last inserted item              | `d.popitem()`                    |
| `setdefault()` | Like get, but sets value if key missing | `d.setdefault("gender", "male")` |
| `update()`     | Updates dictionary with another dict    | `d.update({"age": 30})`          |

---

## Dictionary Comprehension

Like list comprehension, but for dictionaries:

```python
# Squares of numbers 1-5
squares = {x: x*x for x in range(1, 6)}
print(squares)
```

---

## 🔄 Nesting Dictionaries

```python
students = {
    "101": {"name": "Ali", "marks": 90},
    "102": {"name": "Sara", "marks": 95}
}
print(students["101"]["marks"])
```

---

## 🔍 Dictionary vs List

| Feature   | Dictionary                    | List         |
| --------- | ----------------------------- | ------------ |
| Access by | Key                           | Index        |
| Order     | Insertion order (Python 3.7+) | Ordered      |
| Use Case  | Fast lookup by key            | Ordered data |

---

## Practice: Sample Program

```python
# Count frequency of characters
text = "banana"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)  # {'b': 1, 'a': 3, 'n': 2}
```

---

## Summary

* Dictionaries store key-value pairs.
* Keys are unique and immutable.
* Support fast access, insertion, and deletion.
* Useful for lookups, mappings, JSON-like data.

---

