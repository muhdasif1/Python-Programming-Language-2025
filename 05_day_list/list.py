# What is a List
my_list = [1, 2, 3, "apple", True]
print("Original List:", my_list)

# How to Create a List
fruits = ["apple", "banana", "cherry"]
print("\nCreated List:", fruits)

# Accessing List Items Using Positive Indexing
print("\nPositive Indexing:")
print(fruits[0])  # apple
print(fruits[1])  # banana

# Accessing List Items Using Negative Indexing
print("\nNegative Indexing:")
print(fruits[-1])  # cherry
print(fruits[-2])  # banana

# Unpacking List Items
print("\nUnpacking List:")
a, b, c = fruits
print(a, b, c)

# Slicing Items from a List
print("\nSlicing:")
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']

# Modifying Lists
print("\nModifying:")
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Checking Items in a List
print("\nChecking Item:")
if "apple" in fruits:
    print("Yes, 'apple' is in the list.")

# Adding Items to a List
print("\nAppending:")
fruits.append("orange")
print(fruits)

# Inserting Items into a List
print("\nInserting:")
fruits.insert(1, "kiwi")
print(fruits)

# Removing Items from a List
print("\nRemoving by value:")
fruits.remove("kiwi")
print(fruits)

# Removing Items Using Pop
print("\nPop:")
fruits.pop()       # removes last item
fruits.pop(0)      # removes item at index 0
print(fruits)

# Removing Items Using Del
print("\nUsing del:")
del fruits[0]
print(fruits)

# Clearing List Items
print("\nClearing:")
fruits.clear()
print(fruits)

# Copying a List
print("\nCopying:")
fruits = ["apple", "banana", "cherry"]
copy_list = fruits.copy()
print(copy_list)

# Joining Lists
print("\nJoining:")
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(combined)

# Counting Items in a List
print("\nCounting:")
numbers = [1, 2, 2, 3, 2]
print("Count of 2:", numbers.count(2))

# Finding Index of an Item
print("\nIndex:")
print("Index of banana:", fruits.index("banana"))

# Reversing a List
print("\nReversing:")
fruits.reverse()
print(fruits)

# Sorting List Items
print("\nSorting:")
nums = [4, 1, 3, 2]
nums.sort()
print("Ascending:", nums)
nums.sort(reverse=True)
print("Descending:", nums)
