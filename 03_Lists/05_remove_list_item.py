print("Remove specified item")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
print("*****************************************************")

print("Remove first occurrence of a value")
fruits = ["apple", "banana", "cherry", "banana", "kiwi"]
fruits.remove("banana")
print(fruits)
print("*****************************************************")

print("Remove item by index using pop()")
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
print("*****************************************************")

print("Remove last item using pop()")
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)
print("*****************************************************")

print("Remove item by index using del")
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)
print("*****************************************************")

print("Clear the list")
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
print("*****************************************************")
