# A – Accessing Values
person = {"name": "Ali", "age": 25}
print("A:", person["name"])

# B – Built-in Methods
print("B:", dir(person))

# C – Copy a Dictionary
copy_dict = person.copy()
print("C:", copy_dict)

# D – Delete Item
del person["age"]
print("D:", person)

# E – Empty Dictionary
empty = {}
print("E:", empty)

# F – Fromkeys Method
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print("F:", d)

# G – Get Method
print("G:", person.get("name"))
print("G (missing):", person.get("city", "N/A"))

# H – Has Key (using 'in')
print("H:", "name" in person)

# I – Items Method
for k, v in person.items():
    print("I:", k, v)

# J – Join Values (example concept)
data = {"a": "1", "b": "2"}
joined = "-".join(data.values())
print("J:", joined)

# K – Keys Method
print("K:", person.keys())

# L – Length of Dictionary
print("L:", len(person))

# M – Modify Value
person["name"] = "Ahmed"
print("M:", person)

# N – Nested Dictionary
students = {
    "s1": {"name": "Ali", "marks": 90},
    "s2": {"name": "Sara", "marks": 95}
}
print("N:", students["s1"]["marks"])

# O – Ordered Insertion (shown in loop)
ordered = {"a": 1, "b": 2, "c": 3}
for k in ordered:
    print("O:", k, ordered[k])

# P – Pop Method
val = person.pop("name")
print("P:", val)
print("P (after pop):", person)

# Q – Quick Dictionary Creation
quick = dict(x=1, y=2)
print("Q:", quick)

# R – Remove Last Item
sample = {"a": 1, "b": 2}
sample.popitem()
print("R:", sample)

# S – Setdefault Method
person.setdefault("country", "Pakistan")
print("S:", person)

# T – Traverse Dictionary
for key in person:
    print("T:", key, "=>", person[key])

# U – Update Dictionary
person.update({"age": 30, "city": "Lahore"})
print("U:", person)

# V – Values Method
print("V:", person.values())

# W – Word Frequency Counter
text = "hello world"
freq = {}
for char in text:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
print("W:", freq)

# X – XML-like Key Mapping
xml_map = {"<tag>": "data", "</tag>": "end"}
print("X:", xml_map["<tag>"])

# Y – YAML-like Structure
config = {
    "version": 1.0,
    "settings": {
        "debug": True,
        "log": "info"
    }
}
print("Y:", config["settings"]["log"])

# Z – Zip to Create Dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped = dict(zip(keys, values))
print("Z:", zipped)
