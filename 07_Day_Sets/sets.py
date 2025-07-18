# Creating a Set
my_set = {1, 2, 3, 4}
print("Initial Set:", my_set)

# Getting Set's Length
print("Length of Set:", len(my_set))

# Accessing Items in a Set (via loop, since sets are unordered)
print("Accessing items:")
for item in my_set:
    print(item)

# Checking an Item
print("Is 2 in the set?", 2 in my_set)
print("Is 5 in the set?", 5 in my_set)

# Adding Items to a Set
my_set.add(5)
print("After Adding 5:", my_set)

# Adding multiple items using update()
my_set.update([6, 7, 8])
print("After Adding 6, 7, 8:", my_set)

# Removing Items from a Set
my_set.remove(3)  # Raises error if not found
print("After Removing 3:", my_set)

# Discarding an item (no error if not found)
my_set.discard(10)
print("After Discarding 10 (no error):", my_set)

# Popping an item (removes random element)
popped_item = my_set.pop()
print("Popped Item:", popped_item)
print("After Pop:", my_set)

# Clearing Items in a Set
temp_set = {10, 20, 30}
temp_set.clear()
print("After Clearing:", temp_set)

# Deleting a Set
del temp_set
# print(temp_set)  # This would raise an error because the set is deleted

# Converting List to Set
my_list = [1, 2, 2, 3, 4, 4, 5]
converted_set = set(my_list)
print("Converted Set from List:", converted_set)

# Joining Sets (Union)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = set1.union(set2)
print("Union of set1 and set2:", joined_set)

# Finding Intersection Items
intersection = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection)

# Checking Subset and Superset
small_set = {1, 2}
big_set = {1, 2, 3, 4}
print("Is small_set subset of big_set?", small_set.issubset(big_set))
print("Is big_set superset of small_set?", big_set.issuperset(small_set))

# Checking the Difference Between Two Sets
difference = big_set.difference(small_set)
print("Difference (big_set - small_set):", difference)

# Finding Symmetric Difference Between Two Sets
sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)
