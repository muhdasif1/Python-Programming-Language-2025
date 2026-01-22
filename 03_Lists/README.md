# Python List Operations

This project demonstrates various operations and methods that can be performed on Python lists. It includes examples for creating, accessing, modifying, looping, copying, joining, and sorting lists, as well as using list comprehensions and conditional expressions.

## Table of Contents

* [Introduction](#introduction)
* [Creating Lists](#creating-lists)
* [Accessing Items](#accessing-items)
* [Modifying Lists](#modifying-lists)
* [Adding Items](#adding-items)
* [Removing Items](#removing-items)
* [Looping Through Lists](#looping-through-lists)
* [List Comprehensions](#list-comprehensions)
* [Sorting Lists](#sorting-lists)
* [Copying Lists](#copying-lists)
* [Joining Lists](#joining-lists)
* [List Methods](#list-methods)

---

## Introduction

Lists in Python are ordered collections that can store multiple items, which may be of different data types. Lists are mutable, allowing you to modify, add, and remove items.

---

## Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
mixed_list = ["abc", 34, True, 40, "male"]
this_list3 = list(("apple", "banana", "cherry"))  # From a tuple
```

* Lists can contain duplicates.
* Lists can contain multiple data types.
* Lists can be created using square brackets `[]` or the `list()` constructor.

---

## Accessing Items

```python
items = ["pen", "pencil", "eraser"]

# By index
print(items[1])     # pencil
print(items[-1])    # eraser

# Using slicing
print(items[2:5])
print(items[:4])
print(items[2:])
print(items[-4:-1])
```

* Positive indexing starts from `0`.
* Negative indexing starts from `-1` (last item).
* Slicing allows accessing ranges of items.

---

## Modifying Lists

```python
items = ["pen", "pencil", "eraser"]
items[1] = "marker"  # Change a single item

items[1:3] = ["marker", "highlighter"]  # Change multiple items
items[1:2] = ["marker", "highlighter"]  # Replace one item with multiple items
```

---

## Adding Items

```python
thislist.append("orange")              # Add at the end
thislist.insert(1, "orange")           # Insert at specific index
thislist.extend(["mango", "pineapple"]) # Add multiple items
thislist.extend(("kiwi", "orange"))     # Extend with a tuple
```

---

## Removing Items

```python
fruits.remove("banana")  # Remove by value
fruits.pop(1)            # Remove by index
fruits.pop()             # Remove last item
del fruits[0]            # Delete by index
fruits.clear()           # Remove all items
```

---

## Looping Through Lists

```python
# Using for loop
for x in fruits:
    print(x)

# Using index
for i in range(len(fruits)):
    print(fruits[i])

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Using list comprehension
[print(x) for x in fruits]
```

---

## List Comprehensions

```python
# With condition
new_items = [x for x in items if "a" in x]

# Exclude a value
new_items = [x for x in items if x != "apple"]

# Range as iterable
numbers = [x for x in range(10)]

# Range with condition
numbers = [x for x in range(10) if x < 5]

# Expression example
new_items = [x.upper() for x in items]

# Conditional expression
new_items = [x if x != "banana" else "orange" for x in items]
```

---

## Sorting Lists

```python
items.sort()                 # Alphabetical or numerical
items.sort(reverse=True)     # Descending order
items.sort(key=str.lower)    # Case-insensitive
```

* Custom sort function example:

```python
def sort_by_distance(n):
    return abs(n - 50)

items.sort(key=sort_by_distance)
```

---

## Copying Lists

```python
fruits_copy = fruits.copy()
fruits_copy = list(fruits)
fruits_copy = fruits[:]
```

---

## Joining Lists

```python
combined_list = letters + numbers        # Using +
letters.extend(numbers)                  # Using extend()
for x in numbers:                        # Using append() in a loop
    letters.append(x)
```

---

## List Methods

| Method      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `append()`  | Adds an item to the end of the list                          |
| `clear()`   | Removes all items from the list                              |
| `copy()`    | Returns a copy of the list                                   |
| `count()`   | Returns the number of times a value occurs                   |
| `extend()`  | Adds all items from another iterable                         |
| `index()`   | Returns the index of the first occurrence                    |
| `insert()`  | Inserts an item at a specified index                         |
| `pop()`     | Removes an item at a specified index (last if not specified) |
| `remove()`  | Removes the first occurrence of a value                      |
| `reverse()` | Reverses the list order                                      |
| `sort()`    | Sorts the list (alphabetically or numerically)               |

---
