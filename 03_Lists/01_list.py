# Creating and printing a list
name: list[str] = ["Muhammad", "Asif", "Nouroz", "Moeez"]
print(name)

# Another list example
this_list : list[str] = ["Apple", "Banana", "Cherry","Orange", "Mango"]
print(this_list)

# List with duplicate values
fruits_with_duplicates : list[str] = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits_with_duplicates)

# Finding the length of a list
this_list2 :list[str] = ["apple", "banana", "cherry"]
print(len(this_list2))

# Lists with different data types
string_list: list[str] = ["apple", "banana", "cherry"]
print(string_list)
number_list: list[int] = [1, 5, 7, 9, 3]
print(number_list)
boolean_list : list[bool] = [True, False, False]
print(boolean_list)

# Mixed data type list
mixed_list = ["abc", 34, True, 40, "male"]
print(mixed_list)

# Checking the type of a list
my_list = ["apple", "banana", "cherry"]
print(type(my_list))

# Creating a list using the list() constructor
this_list3 = list(("apple", "banana", "cherry"))  # tuple converted to list
print(this_list3)
