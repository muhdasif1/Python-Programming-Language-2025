# ============================================================
# STRING METHODS
# ============================================================

text = "hello world"
num_text = "12345"
mixed_text = "Hello123"
space_text = "   "
tab_text = "hi\tthere"
list_text = ["a", "b", "c"]

print("1. capitalize():", text.capitalize())
print("2. casefold():", "HELLO".casefold())
print("3. center():", "hi".center(10, "-"))
print("4. count():", "banana".count("a"))
print("5. encode():", "hello".encode())
print("6. endswith():", "test.py".endswith(".py"))
print("7. expandtabs():", tab_text.expandtabs(4))
print("8. find():", "apple".find("p"))
print("9. format():", "My name is {}".format("Asif"))
print("10. format_map():", "{name}".format_map({"name": "Asif"}))
print("11. index():", "apple".index("p"))
print("12. isalnum():", mixed_text.isalnum())
print("13. isalpha():", "abc".isalpha())
print("14. isascii():", "Hello!".isascii())
print("15. isdecimal():", num_text.isdecimal())
print("16. isdigit():", num_text.isdigit())
print("17. isidentifier():", "name1".isidentifier())
print("18. islower():", text.islower())
print("19. isnumeric():", num_text.isnumeric())
print("20. isprintable():", "hi!".isprintable())
print("21. isspace():", space_text.isspace())
print("22. istitle():", "Hello World".istitle())
print("23. isupper():", "HELLO".isupper())
print("24. join():", "-".join(list_text))
print("25. ljust():", "hi".ljust(5, "-"))
print("26. lower():", "HELLO".lower())
print("27. lstrip():", "   hi".lstrip())
table = str.maketrans("a", "1")
print("28. maketrans():", table)
print("29. partition():", "name:Asif".partition(":"))
print("30. removeprefix():", "unhappy".removeprefix("un"))
print("31. removesuffix():", "testing".removesuffix("ing"))
print("32. replace():", "hello".replace("l", "x"))
print("33. rfind():", "banana".rfind("a"))
print("34. rindex():", "banana".rindex("a"))
print("35. rjust():", "hi".rjust(5, "-"))
print("36. rpartition():", "a:b:c".rpartition(":"))
print("37. rsplit():", "a,b,c".rsplit(",", 1))
print("38. rstrip():", "hi   ".rstrip())
print("39. split():", "a b c".split())
print("40. splitlines():", "Hi\nBye".splitlines())
print("41. startswith():", "hello".startswith("he"))
print("42. strip():", "  hello  ".strip())
print("43. swapcase():", "HeLLo".swapcase())
print("44. title():", "hello world".title())
print("45. translate():", "abc".translate(str.maketrans("a", "1")))
print("46. upper():", "hello".upper())
print("47. zfill():", "42".zfill(5))


# ============================================================
# INTEGER METHODS / FUNCTIONS
# ============================================================
# 🔢 Python Numeric Methods and Attributes Demonstration
# Works for both int and float types

# Integer examples
num_int = 13
print("Integer:", num_int)
print("bit_count():", num_int.bit_count())
print("bit_length():", num_int.bit_length())
print("conjugate():", num_int.conjugate())
print("to_bytes(2, 'big'):", num_int.to_bytes(2, 'big'))
print()

# Convert bytes back to int
b = b'\x00\x10'
print("from_bytes(b'\\x00\\x10', 'big'):", int.from_bytes(b, 'big'))
print()

# Float examples
num_float = 2.5
print("Float:", num_float)
print("as_integer_ratio():", num_float.as_integer_ratio())
print("is_integer():", num_float.is_integer())
print("numerator:", num_float.as_integer_ratio()[0])
print("denominator:", num_float.as_integer_ratio()[1])
print()

# Integer float check
whole_float = 5.0
print("Whole float:", whole_float)
print("is_integer():", whole_float.is_integer())
print()

# Complex number example
num_complex = 3 + 4j
print("Complex number:", num_complex)
print("real:", num_complex.real)
print("imag:", num_complex.imag)
print("conjugate():", num_complex.conjugate())
print()

# ============================================================
# LIST METHODS
# ============================================================

# Sample list
fruits = ["apple", "banana", "cherry"]
numbers = [3, 1, 4, 2]

print("Original lists:")
print("fruits =", fruits)
print("numbers =", numbers)
print("-" * 50)
fruits.append("orange")
print("1. append():", fruits)
temp = fruits.copy()
temp.clear()
print("2. clear():", temp)
new_list = fruits.copy()
print("3. copy():", new_list)
print("4. count():", fruits.count("banana"))
fruits.extend(["mango", "grape"])
print("5. extend():", fruits)
print("6. index():", fruits.index("banana"))
fruits.insert(1, "kiwi")
print("7. insert():", fruits)
removed_item = fruits.pop()
print("8. pop():", fruits, "→ removed:", removed_item)
fruits.remove("banana")
print("9. remove():", fruits)
fruits.reverse()
print("10. reverse():", fruits)
numbers.sort()
print("11. sort():", numbers)
numbers.sort(reverse=True)
print("   sort(reverse=True):", numbers)

# ============================================================
# TUPLE METHODS
# ============================================================
print("\n=== TUPLE METHODS ===")
t = (1, 2, 2, 3)
print(t.count(2))          # 2
print(t.index(3))          # 3

# ============================================================
# SET METHODS
# ============================================================
print("\n=== SET METHODS ===")
s = {1, 2, 3}
s.add(4)
print(s)                   # {1, 2, 3, 4}
s.discard(2)
print(s)                   # {1, 3, 4}
s2 = {3, 4, 5, 6}
print(s.union(s2))         # {1, 3, 4, 5, 6}
print(s.intersection(s2))  # {3, 4}
print(s.difference(s2))    # {1}
print(s.symmetric_difference(s2))  # {1, 5, 6}
print(s.issubset({1, 3, 4, 5}))    # True
print(s.issuperset({3}))           # True
s.clear()
print(s)                   # set()

# ============================================================
# DICTIONARY METHODS
# ============================================================
print("\n=== DICTIONARY METHODS ===")
d = {"a": 1, "b": 2, "c": 3}
print(d.get("a"))          # 1
print(d.keys())            # dict_keys(['a', 'b', 'c'])
print(d.values())          # dict_values([1, 2, 3])
print(d.items())           # dict_items([('a', 1), ('b', 2), ('c', 3)])
d.update({"d": 4})
print(d)                   # {'a':1, 'b':2, 'c':3, 'd':4}
print(d.pop("b"))          # removes and returns 2
print(d.popitem())         # removes last item
d.setdefault("x", 99)
print(d)                   # {'a': 1, 'c': 3, 'x': 99}
copy_dict = d.copy()
print(copy_dict)
d.clear()
print(d)                   # {}
