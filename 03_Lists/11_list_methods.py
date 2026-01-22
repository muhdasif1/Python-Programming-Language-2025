# append()
items = ["apple", "banana"]
items.append("cherry")
print(items)

# clear()
items = ["apple", "banana", "cherry"]
items.clear()
print(items)

# copy()
items = ["apple", "banana", "cherry"]
items_copy = items.copy()
print(items_copy)

# count()
items = ["apple", "banana", "apple", "cherry"]
print(items.count("apple"))

# extend()
items = ["apple", "banana"]
more_items = ["cherry", "mango"]
items.extend(more_items)
print(items)

# index()
items = ["apple", "banana", "cherry"]
print(items.index("banana"))

# insert()
items = ["apple", "banana", "cherry"]
items.insert(1, "orange")
print(items)

# pop()
items = ["apple", "banana", "cherry"]
items.pop(1)
print(items)

# remove()
items = ["apple", "banana", "cherry"]
items.remove("banana")
print(items)

# reverse()
items = ["apple", "banana", "cherry"]
items.reverse()
print(items)

# sort()
items = ["orange", "apple", "banana", "cherry"]
items.sort()
print(items)
