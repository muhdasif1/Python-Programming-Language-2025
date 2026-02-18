print("Accessing an item by index (positive indexing)")
items = ["pen", "pencil", "eraser"]
print(items[0])
print(items[1])   # Output: pencil
print(items[2])
print("*****************************************************")

print("Accessing an item using negative indexing")
items = ["pen", "pencil", "eraser"]
print(items[-1])  # Output: eraser
print(items[-2])
print(items[-3])
print("*****************************************************")

print("Accessing a range of items (index 2 to 4)")
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[2:5])  # Output: ['eraser', 'marker', 'sharpener']
print("*****************************************************")

print("Accessing items from the beginning to index 3")
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[:4])   # Output: ['pen', 'pencil', 'eraser', 'marker']
print("*****************************************************")

print("Accessing items from index 2 to the end")
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[2:])   # Output: ['eraser', 'marker', 'sharpener', 'ruler', 'notebook']
print("*****************************************************")

print("Accessing items using negative range indexing")
items = ["pen", "pencil", "eraser", "marker", "sharpener", "ruler", "notebook"]
print(items[-4:-1])  # Output: ['marker', 'sharpener', 'ruler']
print("*****************************************************")
