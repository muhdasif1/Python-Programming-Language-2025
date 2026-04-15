# Append item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend list with another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

name1: list = ["Muhammad asif", "moeez khan", "Nouroz"]
name2: list = ["Usman", "Ahmad", "Raza", "Shery"]
name1.extend(name2)
print(name1)