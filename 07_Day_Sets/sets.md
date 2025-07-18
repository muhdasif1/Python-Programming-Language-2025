Great! Let's go step by step and explore **Python Sets** in depth.

---

## What is a Set?

A **set** in Python is a collection of **unordered, unindexed**, and **unique** elements.

* **Unordered**: Elements have no fixed position.
* **No duplicates**: Every element is unique.
* **Mutable**: You can add or remove elements.
* **Defined using `{}` or the `set()` constructor**.

---

## 1️ Creating a Set

### Syntax:

```python
my_set = {1, 2, 3}
```

### Using `set()` constructor:

```python
my_set = set([1, 2, 3])
```

**Important**:

* You can't create an empty set using `{}` — it creates an empty dictionary.

```python
empty_set = set()  # ✅ correct
empty_dict = {}    # ⚠️ this is a dict
```

---

## 2️ Getting Set's Length

Use `len()` to get the number of elements in the set:

```python
my_set = {10, 20, 30}
print(len(my_set))  # Output: 3
```

---

## 3️ Accessing Items in a Set

### Sets are unordered — no index access:

```python
my_set = {1, 2, 3}
# print(my_set[0])  ❌ Error: sets do not support indexing
```

### Access via loop:

```python
for item in my_set:
    print(item)
```

---

## 4️ Checking an Item

Use the `in` keyword:

```python
my_set = {1, 2, 3}
print(2 in my_set)   # True
print(5 in my_set)   # False
```

---

## 5️ Adding Items to a Set

### `add()` method:

```python
my_set = {1, 2}
my_set.add(3)
print(my_set)  # {1, 2, 3}
```

* If the item already exists, nothing happens.

```python
my_set.add(2)
print(my_set)  # Still {1, 2, 3}
```

---

## 6️ Removing Items from a Set

### `remove()` – removes item, raises error if not found:

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # {1, 3}
# my_set.remove(5)  ❌ KeyError
```

### `discard()` – removes item if exists, no error otherwise:

```python
my_set.discard(5)  # ✅ No error
```

---

## 7️ Clearing Items in a Set

### `clear()` – removes all elements:

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
```

---

## 8️ Deleting a Set

### `del` – deletes the entire set from memory:

```python
my_set = {1, 2, 3}
del my_set
# print(my_set)  ❌ NameError: my_set is not defined
```

---

## 9️ Converting List to Set

### Use `set()` to remove duplicates:

```python
my_list = [1, 2, 2, 3, 4]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4}
```

---

## 10 Joining Sets

### `union()` or `|` operator:

```python
a = {1, 2}
b = {2, 3, 4}

# Method 1
joined = a.union(b)  # {1, 2, 3, 4}

# Method 2
joined = a | b
```

---

## 11 Finding Intersection Items

### `intersection()` or `&` operator:

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Method 1
common = a.intersection(b)  # {2, 3}

# Method 2
common = a & b
```

---

## 12 Checking Subset and Superset

### `issubset()`:

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True
```

### `issuperset()`:

```python
print(b.issuperset(a))  # True
```

---

## 13 Checking the Difference Between Two Sets

### `difference()` or `-` operator:

```python
a = {1, 2, 3}
b = {2, 3, 4}

diff = a.difference(b)  # {1}
# or
diff = a - b
```

---

## 14 Finding Symmetric Difference Between Two Sets

### `symmetric_difference()` or `^` operator:

Returns items that are in **either set but not both**.

```python
a = {1, 2, 3}
b = {2, 3, 4}

sym_diff = a.symmetric_difference(b)  # {1, 4}
# or
sym_diff = a ^ b
```

---
