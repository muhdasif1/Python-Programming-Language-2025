# ============================================================
# STRING METHODS
# ============================================================
print("=== STRING METHODS ===")
s = " Hello World "
print(s.upper())           # HELLO WORLD
print(s.lower())           # hello world
print(s.title())           # Hello World
print(s.capitalize())      #  hello world
print(s.strip())           # Hello World
print(s.replace("World", "Python"))  #  Hello Python
print(s.split())           # ['Hello', 'World']
print("-".join(["a", "b", "c"]))     # a-b-c
print(s.find("World"))     # index of "World"
print(s.count("l"))        # number of 'l'
print("abc".isalpha())     # True
print("123".isdigit())     # True
print(s.startswith(" H"))  # True
print(s.endswith("d "))    # True

# ============================================================
# INTEGER METHODS / FUNCTIONS
# ============================================================
print("\n=== INTEGER METHODS ===")
x = -5
y = 10
print(abs(x))              # 5
print(pow(2, 3))           # 8
print(divmod(9, 2))        # (4, 1)
print(int("42"))           # 42
print((10).bit_length())   # 4

# ============================================================
# LIST METHODS
# ============================================================
print("\n=== LIST METHODS ===")
lst = [1, 2, 3]
lst.append(4)
print(lst)                 # [1, 2, 3, 4]
lst.extend([5, 6])
print(lst)                 # [1, 2, 3, 4, 5, 6]
lst.insert(1, 99)
print(lst)                 # [1, 99, 2, 3, 4, 5, 6]
lst.remove(99)
print(lst)                 # [1, 2, 3, 4, 5, 6]
print(lst.pop())           # removes and returns 6
print(lst.index(3))        # 2
print(lst.count(2))        # 1
lst.sort()
print(lst)                 # [1, 2, 3, 4, 5]
lst.reverse()
print(lst)                 # [5, 4, 3, 2, 1]
copy_list = lst.copy()
print(copy_list)
lst.clear()
print(lst)                 # []

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
