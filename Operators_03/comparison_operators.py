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
