# Sort list alphabetically
items = ["orange", "mango", "kiwi", "pineapple", "banana"]
items.sort()
print(items)

# Sort list numerically
items = [100, 50, 65, 82, 23]
items.sort()
print(items)

# Sort list descending (strings)
items = ["orange", "mango", "kiwi", "pineapple", "banana"]
items.sort(reverse=True)
print(items)

# Sort list descending (numbers)
items = [100, 50, 65, 82, 23]
items.sort(reverse=True)
print(items)

# Custom sort function
def sort_by_distance(n):
    return abs(n - 50)

items = [100, 50, 65, 82, 23]
items.sort(key=sort_by_distance)
print(items)

# Case-sensitive sort
items = ["banana", "Orange", "Kiwi", "cherry"]
items.sort()
print(items)

# Case-insensitive sort
items = ["banana", "Orange", "Kiwi", "cherry"]
items.sort(key=str.lower)
print(items)
