print("\nComparison Operators:\n")

a: int = 10
b: int = 20

print(f"{a} > {b}  --> {a > b}")
print(f"{a} < {b}  --> {a < b}")
print(f"{a} == {b} --> {a == b}")
print(f"{a} != {b} --> {a != b}")
print(f"{a} >= {b} --> {a >= b}")
print(f"{a} <= {b} --> {a <= b}")
print("--------------------------------------------------")

print("********** Comparison Operators ************")
a : int = 10
b : int = 20
print("a is 10  ==  b is 20: ",a==b)
print("a is 10  !=  b is 20: ",a!=b)
print("a is 10  >   b is 20: ",a>b)           
print("a is 10  <   b is 20: ",a<b)
print("a is 10  >=  b is 20: ",a>=b)
print("a is 10  <=  b is 20: ",a<=b)
print("--------------------------------------------------")
print()

a : int = 15
b : int = 15
dict = {"a 15 is b 15": a == b,
        "a 15 is not b 15": a != b,
        "a 15 is greater than b 15": a > b,
        "a 15 is less than b 15": a < b,
        "a 15 is greater than or equal to b 15": a >= b,
        "a 15 is less than or equal to b 15": a <= b
        }
print(dict,type(dict))
print()
list_comparisons = [
    ("a 15 is b 15", a == b),
    ("a 15 is not b 15", a != b),
    ("a 15 is greater than b 15", a > b),           
    ("a 15 is less than b 15", a < b),
    ("a 15 is greater than or equal to b 15", a >= b),
    ("a 15 is less than or equal to b 15", a <= b)

]
print()
print(list_comparisons, type(list_comparisons))

touple_comparisons = (
    ("a 15 is b 15", a == b),
    ("a 15 is not b 15", a != b),
    ("a 15 is greater than b 15", a > b),           
    ("a 15 is less than b 15", a < b),      
    ("a 15 is greater than or equal to b 15", a >= b),
    ("a 15 is less than or equal to b 15", a <= b)
)
print(touple_comparisons, type(touple_comparisons))


print("********** Comparison Operators ************")
a : int = 10
b : int = 20
print("a == b : ",a==b)
print("a != b : ",a!=b)
print("a > b : ",a>b)           
print("a < b : ",a<b)
print("a >= b : ",a>=b)
print("a <= b : ",a<=b)
print("--------------------------------------------------")
print()

print("********** Comparison Operators ************")
name1 : str = "Muhammad Asif"
name2 : str = "Muhammad Asif"
print("name1 is name2 :", name1 == name2)
print("name1 is not name2 :", name1 != name2)

age : int = 25
age2 : int = 30
print("age 25 is age2 30 :",age > age2)
print("age 25 is not age2 30 :",age < age2)
print("age 25 is age2 30 :",age >= age2)
print("age 25 is not age2 30 :",age <= age2)
print("--------------------------------------------------")
print()