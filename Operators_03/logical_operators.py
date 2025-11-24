print("********** Logical Operators ************")
x : int = 10
y : int = 20
z : int = 30
print("x < y and y < z :", x < y and y < z)
print("x < y or y > z :", x < y or y > z)
print("not(x < y) :", not(x < y))
print("--------------------------------------------------")
print()

print("********** Logical Operators ************")
p : bool = True
q : bool = False
print("p and q :", p and q)        # Logical AND
print("p or q  :", p or q)         # Logical OR
print("not p   :", not p)          # Logical NOT
print("not q   :", not q)          # Logical NOT
print("--------------------------------------------------")
print()

print("********** Logical Operators with Comparisons ************")
a : int = 10
b : int = 20
c : int = 15
print("a < b and b > c :", a < b and b > c)
print("a < b or b < c  :", a < b or b < c)
print("not(a < c)      :", not(a < c))
print("not(b > a)      :", not(b > a))
print("--------------------------------------------------")
print()

print("********** Combined Logical Operations ************")
x : int = 5
y : int = 10
z : int = 15
print("(x < y) and (y < z) :", (x < y) and (y < z))
print("(x > y) or (y < z)  :", (x > y) or (y < z))
print("not(x == 5)         :", not(x == 5))
print("not(y > 15)         :", not(y > 15))
print("--------------------------------------------------")
print()

print("********** Logical Operators with Mixed Types ************")
num : int = 10
text : str = "10"
is_num_equal_text : bool = (str(num) == text) and (num > 5)
is_num_not_equal_text : bool = (str(num) != text) or (num < 5)
print("Is num equal to text and greater than 5?:", is_num_equal_text)
print("Is num not equal to text or less than 5?:", is_num_not_equal_text)
print("--------------------------------------------------")
print()

print("********** End of Logical Operators Demonstration ************")      
  