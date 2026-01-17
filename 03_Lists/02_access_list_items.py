# Accessing an item by index (positive indexing)
items = ["pen", "pencil", "eraser"]
print(items[1])   # Output: pencil

# Accessing an item using negative indexing
items = ["pen", "pencil", "eraser"]
print(items[-1])  # Output: eraser

# Accessing a range of items (index 2 to 4)
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[2:5])  # Output: ['eraser', 'marker', 'sharpener']

# Accessing items from the beginning to index 3
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[:4])   # Output: ['pen', 'pencil', 'eraser', 'marker']

# Accessing items from index 2 to the end
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[2:])   # Output: ['eraser', 'marker', 'sharpener', 'ruler', 'notebook']

# Accessing items using negative range indexing
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[-4:-1])  # Output: ['marker', 'sharpener', 'ruler']
