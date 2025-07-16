# ✅ Creating Tuples
tuple1 = (10, 20, 30)
tuple2 = "apple", "banana", "cherry"     # No parentheses
tuple3 = (42,)                           # Single-item tuple (must use comma)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

# ✅ Tuple Length
print("Length of Tuple 2:", len(tuple2))

# ✅ Accessing Tuple Items
print("First item in Tuple 1:", tuple1[0])
print("Last item in Tuple 2:", tuple2[-1])

# ✅ Slicing Tuples
print("Slice from Tuple 2 (1:3):", tuple2[1:3])

# ✅ Changing Tuples to Lists (to modify values)
temp_list = list(tuple1)
temp_list[1] = 99
tuple1 = tuple(temp_list)
print("Modified Tuple 1:", tuple1)

# ✅ Checking an Item in a Tuple
print("Is 'banana' in Tuple 2?", 'banana' in tuple2)
print("Is 100 in Tuple 1?", 100 in tuple1)

# ✅ Joining Tuples
joined_tuple = tuple1 + tuple2
print("Joined Tuple:", joined_tuple)

# ✅ Deleting a Tuple
del tuple3
# print(tuple3)  # Uncommenting this will raise an error: NameError
