# ========================================
# Python Identity Operators
# ========================================

# Create lists
list1 = [1, 2, 3]
list2 = list1  # list2 refers to the same object as list1
list3 = [1, 2, 3]  # list3 is a new object with the same values

# Identity Operator: is
print("list1 is list2:", list1 is list2)   # True, same object in memory
print("list1 is list3:", list1 is list3)   # False, different objects

# Identity Operator: is not
print("list1 is not list3:", list1 is not list3) # True, different objects

# Identity with numbers (immutable objects)
x = 10
y = 10
z = 20

print("x is y:", x is y)       # True, small integers are same object
print("x is z:", x is z)       # False, different objects
print("x is not z:", x is not z) # True
