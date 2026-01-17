# Accessing an item by index (positive indexing)
this_list = ["apple", "banana", "cherry"]
print(this_list[1])   # Output: banana

# Accessing an item using negative indexing
this_list = ["apple", "banana", "cherry"]
print(this_list[-1])  # Output: cherry

# Accessing a range of items (index 2 to 4)
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])  # Output: ['cherry', 'orange', 'kiwi']

# Accessing items from the beginning to index 3
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])   # Output: ['apple', 'banana', 'cherry', 'orange']

# Accessing items from index 2 to the end
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])   # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Accessing items using negative range indexing
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])  # Output: ['orange', 'kiwi', 'melon']
