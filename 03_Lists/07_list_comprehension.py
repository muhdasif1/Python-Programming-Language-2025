# Without list comprehension
items = ["apple", "banana", "cherry", "kiwi", "mango"]
new_items = []

for x in items:
    if "a" in x:
        new_items.append(x)

print(new_items)

# With list comprehension
items = ["apple", "banana", "cherry", "kiwi", "mango"]
new_items = [x for x in items if "a" in x]
print(new_items)

# Condition example (exclude "apple")
new_items = [x for x in items if x != "apple"]
print(new_items)

# Without condition
new_items = [x for x in items]
print(new_items)

# Using range() as iterable
numbers = [x for x in range(10)]
print(numbers)

# Using range() with condition
numbers = [x for x in range(10) if x < 5]
print(numbers)

# Expression example (uppercase values)
new_items = [x.upper() for x in items]
print(new_items)

# Set all values to 'hello'
new_items = ["hello" for x in items]
print(new_items)

# Conditional expression
new_items = [x if x != "banana" else "orange" for x in items]
print(new_items)
