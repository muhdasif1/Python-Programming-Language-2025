### What is a Tuple?

A **tuple** is an **ordered**, **immutable** (unchangeable) **collection** of items. It can store **multiple values** in a **single variable**, like a list, but **you can't modify** it after creation.

```python
my_tuple = (1, 2, 3)
print(my_tuple)
```

---

### Creating a Tuple

You create a tuple using **parentheses `()`** or just commas:

```python
# With parentheses
t1 = (1, 2, 3)

# Without parentheses (not recommended)
t2 = 4, 5, 6

# Single item tuple (must include a comma)
t3 = (10,)  

print(t1, t2, t3)
```

---

### Tuple Length

Use `len()` to find how many items are in a tuple:

```python
my_tuple = ("apple", "banana", "cherry")
print(len(my_tuple))  # Output: 3
```

---

### Accessing Tuple Items

Use **indexing** (starting from 0):

```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple
```

---

### Slicing Tuples

Just like lists, you can use slicing:

```python
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)
```

---

### Changing Tuples to Lists

Since tuples are immutable, convert to a list to change values:

```python
t = (1, 2, 3)
lst = list(t)      # Convert to list
lst[1] = 200       # Change item
t = tuple(lst)     # Convert back to tuple
print(t)           # Output: (1, 200, 3)
```

---

### Checking an Item in a Tuple

Use `in` keyword:

```python
my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)  # Output: True
```

---

### Joining Tuples

Use the `+` operator to join tuples:

```python
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5)
```

---

### Deleting Tuples

You **can’t delete items** from a tuple, but you can delete the whole tuple:

```python
my_tuple = (1, 2, 3)
del my_tuple
# print(my_tuple)  # This will raise an error: NameError
```

---