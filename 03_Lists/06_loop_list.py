# Loop through a list using for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the index numbers
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

# Loop using while loop
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Loop using list comprehension
fruits = ["apple", "banana", "cherry"]
[print(x) for x in fruits]
