# Change a specific item using its index
items = ["pen", "pencil", "eraser"]
items[1] = "marker"
print(items)
# Output: ['pen', 'marker', 'eraser']


# Change a range of item values
items = ["pen", "pencil", "eraser", "notebook", "sharpener", "ruler"]
items[1:3] = ["marker", "highlighter"]
print(items)
# Output: ['pen', 'marker', 'highlighter', 'notebook', 'sharpener', 'ruler']


# Replace one item with multiple new items
items = ["pen", "pencil", "eraser"]
items[1:2] = ["marker", "highlighter"]
print(items)
# Output: ['pen', 'marker', 'highlighter', 'eraser']