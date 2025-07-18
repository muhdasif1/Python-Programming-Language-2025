## ✨ What is a Set?

A **set** in Python is a collection of **unordered, unindexed**, and **unique** elements.

* **Unordered**: Elements have no fixed position.
* **No duplicates**: Every element is unique.
* **Mutable**: You can add or remove elements.
* **Defined using `{}` or the `set()` constructor**.

---

## 1. Creating a Set

```python
my_set = {1, 2, 3}
```

### Using `set()` constructor:

```python
my_set = set([1, 2, 3])
```

### Creating an Empty Set:

```python
empty_set = set()  # ✔️ Correct
empty_dict = {}    # ❌ This is a dictionary
```

---

## 2. Getting Set's Length

```python
my_set = {10, 20, 30}
print(len(my_set))  # Output: 3
```

---

## 3. Accessing Items in a Set

```python
my_set = {1, 2, 3}
for item in my_set:
    print(item)
```

> Note: You can't access items by index.

---

## 4. Checking an Item

```python
my_set = {1, 2, 3}
print(2 in my_set)   # True
print(5 in my_set)   # False
```

---

## 5. Adding Items to a Set

```python
my_set = {1, 2}
my_set.add(3)
print(my_set)  # {1, 2, 3}
```

> Adding a duplicate will have no effect.

---

## 6. Removing Items from a Set

### Using `remove()`:

```python
my_set.remove(2)  # Removes 2
```

> Raises an error if the item doesn't exist.

### Using `discard()`:

```python
my_set.discard(5)  # Safe remove, no error
```

---

## 7. Clearing Items in a Set

```python
my_set.clear()
print(my_set)  # set()
```

---

## 8. Deleting a Set

```python
del my_set
# my_set no longer exists
```

---

## 9. Converting List to Set

```python
my_list = [1, 2, 2, 3, 4]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4}
```

---

## 10. Joining Sets

### Using `union()`:

```python
set1 = {1, 2}
set2 = {2, 3, 4}
joined = set1.union(set2)  # {1, 2, 3, 4}
```

### Using `|` operator:

```python
joined = set1 | set2
```

---

## 11. Finding Intersection Items

### Using `intersection()`:

```python
common = set1.intersection(set2)  # {2}
```

### Using `&` operator:

```python
common = set1 & set2
```

---

## 12. Checking Subset and Superset

```python
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))   # True
print(b.issuperset(a)) # True
```

---

## 13. Checking the Difference Between Two Sets

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

diff = set1.difference(set2)  # {1}
# or
print(set1 - set2)  # {1}
```

---

## 14. Finding Symmetric Difference Between Two Sets

```python
sym_diff = set1.symmetric_difference(set2)  # {1, 4}
# or
print(set1 ^ set2)  # {1, 4}
```

---

## 15. Joining Sets (Again)

Same as point 10: use `union()` or `|` to join sets.

---
