# Append item
print("Append item")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print()

# Insert item
print("Insert Item")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

car : list = ["Toyota", "RangeRover", "Hundai", "Honda", "Mercedes"]
car.insert(1,"BMW")
print(car) 
print()

# Extend list with another list
print("Extend  List")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print()

name1: list = ["Muhammad asif", "moeez khan", "Nouroz"]
name2: list = ["Usman", "Ahmad", "Raza", "Shery"]
name1.extend(name2)
print(name1)
print()