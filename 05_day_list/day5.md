## What is a List?

A **list** is a built-in Python data structure that can store **multiple items** in a **single variable**. Lists are **ordered**, **changeable**, and allow **duplicate values**.

```python
my_list = [1, 2, 3, "apple", True]
print(my_list)
```

---

## How to Create a List

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

---

## Accessing List Items Using Positive Indexing

Index starts from **0**.

```python
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
```

---

## Accessing List Items Using Negative Indexing

Index starts from **-1** (last item).

```python
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
```

---

## Unpacking List Items

You can unpack list elements into variables.

```python
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a, b, c)  # Output: apple banana cherry
```

---

## Slicing Items from a List

```python
print(fruits[0:2])   # Output: ['apple', 'banana']
print(fruits[1:])    # Output: ['banana', 'cherry']
```

---

## Modifying Lists

```python
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

---

## Checking Items in a List

```python
if "apple" in fruits:
    print("Yes, apple is in the list")
```

---

## Adding Items to a List

### Append (adds to the end)

```python
fruits.append("orange")
print(fruits)
```

---

## Inserting Items into a List

```python
fruits.insert(1, "kiwi")
print(fruits)  # Inserts kiwi at index 1
```

---

## Removing Items from a List

### Remove by value

```python
fruits.remove("banana")
print(fruits)
```

---

## Removing Items Using `pop()`

### Removes item by index (default is last item)

```python
fruits.pop()
print(fruits)

fruits.pop(0)  # Remove first item
print(fruits)
```

---

## Removing Items Using `del`

```python
del fruits[0]  # Delete item at index 0
print(fruits)
```

---

## Clearing List Items

```python
fruits.clear()
print(fruits)  # Output: []
```

---

## Copying a List

```python
new_fruits = fruits.copy()
print(new_fruits)
```

---

## Joining Lists

```python
list1 = [1, 2]
list2 = [3, 4]
joined = list1 + list2
print(joined)
```

---

## Counting Items in a List

```python
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # Output: 3
```

---

## Finding Index of an Item

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1
```

---

## Reversing a List

```python
fruits.reverse()
print(fruits)
```

---

## Sorting List Items

```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
```

To sort in descending order:

```python
numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]
```

---

