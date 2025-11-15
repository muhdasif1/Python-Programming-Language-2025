
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

print("********** Logical Operators in Conditional Statements ************")
age : int = 25
has_id : bool = True
if age >= 18 and has_id:    
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")      
print("--------------------------------------------------")
print()

print("********** Logical Operators with Membership ************")
fruits : list = ["apple", "banana", "cherry"]
is_apple_present : bool = "apple" in fruits and len(fruits) > 2
is_grape_absent : bool = "grape" not in fruits or len(fruits) < 2
print("Is apple present and more than 2 fruits?:", is_apple_present)
print("Is grape absent or less than 2 fruits?:", is_grape_absent)
print("--------------------------------------------------")
print()

print("********** Logical Operators with Identity ************")
list1 : list = [1, 2, 3]
list2 : list = list1
list3 : list = [1, 2, 3]
is_list1_list2_same : bool = list1 is list2 and len(list1) == len(list2)
is_list1_list3_different : bool = list1 is not list3 or len(list1) != len(list3)
print("Is list1 and list2 the same object and same length?:", is_list1_list2_same)
print("Is list1 and list3 different objects or different lengths?:", is_list1_list3_different)
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
  