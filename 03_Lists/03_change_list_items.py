# --------------------------------------- #
# Example 1: Change a specific item value
# --------------------------------------- #

# Create a list of stationery items
items = ["pen", "pencil", "eraser"]

# Print the original list
print("Original list:")
print(items)

# Change the second item (index 1)
items[1] = "marker"

# Print the updated list
print("List after changing the second item:")
print(items)

# --------------------------------------- #
# Example 2: Change a range of item values
# --------------------------------------- #

# Create a new list of stationery items
items = ["pen", "pencil", "eraser", "notebook", "sharpener", "ruler"]

# Print the original list
print("\nOriginal list:")
print(items)

# Change multiple items using slicing (index 1 to 2)
items[1:3] = ["marker", "highlighter"]

# Print the updated list
print("List after changing a range of items:")
print(items)

# --------------------------------------------------- #
# Example 3: Replace one item with multiple new items
# --------------------------------------------------- #

# Create another list of stationery items
items = ["pen", "pencil", "eraser"]

# Print the original list
print("\nOriginal list:")
print(items)

# Replace the second item with two new values
items[1:2] = ["marker", "highlighter"]

# Print the updated list
print("List after replacing one item with multiple items:")
print(items)
