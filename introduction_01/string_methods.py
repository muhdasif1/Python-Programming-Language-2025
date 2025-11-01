# -------------------------------
# STRING METHODS
# -------------------------------
print("STRING METHODS")
text = "  hello world  "
print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", text.strip())
print("replace():", text.replace("world", "Python"))
print("split():", text.split())
print("join():", "-".join(["Python", "is", "fun"]))
print("find():", text.find("world"))
print("count():", text.count("l"))
print("startswith():", text.startswith(" "))
print("endswith():", text.endswith(" "))
print()

# -------------------------------
# INTEGER METHODS (int)
# -------------------------------
print("INTEGER EXAMPLES")
num = 25
print("bit_length():", num.bit_length())  # Returns bits needed to represent number
print("to_bytes():", num.to_bytes(2, 'big'))  # Converts int to bytes
print("from_bytes():", int.from_bytes(b'\x00\x19', 'big'))  # Converts bytes to int
print()

# -------------------------------
# LIST METHODS
# -------------------------------
print("LIST METHODS")
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("append():", fruits)
fruits.insert(1, "grape")
print("insert():", fruits)
fruits.remove("banana")
print("remove():", fruits)
fruits.sort()
print("sort():", fruits)
fruits.reverse()
print("reverse():", fruits)
print("count():", fruits.count("apple"))
print("index():", fruits.index("apple"))
print()

# -------------------------------
# TUPLE METHODS
# -------------------------------
print("TUPLE METHODS")
numbers = (1, 2, 2, 3)
print("count():", numbers.count(2))
print("index():", numbers.index(3))
print()

# -------------------------------
# SET METHODS
# -------------------------------
print("SET METHODS")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("union():", s1.union(s2))
print("intersection():", s1.intersection(s2))
print("difference():", s1.difference(s2))
print("add():", s1 | {6})
print("discard():", s1 - {2})
print()

# -------------------------------
# DICTIONARY METHODS
# -------------------------------
print("DICTIONARY METHODS")
student = {"name": "Ali", "age": 15, "class": "10th"}
print("keys():", student.keys())
print("values():", student.values())
print("items():", student.items())
student.update({"age": 16})
print("update():", student)
student.pop("class")
print("pop():", student)
print("get():", student.get("name"))
print("clear():", student.clear(), student)
print()