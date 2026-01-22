# Join two lists using + operator
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

combined_list = letters + numbers
print(combined_list)

# Join lists using append() in a loop
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

for x in numbers:
    letters.append(x)

print(letters)

# Join lists using extend() method
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

letters.extend(numbers)
print(letters)
