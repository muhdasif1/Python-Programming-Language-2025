car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2025
}
x = car["model"]
print(x)
print("**************************")

car1 = {
  "brand": "Range Rover",
  "model": "Sports",
  "year": 2024
}
x = car1.get("model")
print(x)
print("**************************")

car2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car2.keys()
print(x)
print("**************************")

car3 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car3.keys()
print(x) #before the change
car3["color"] = "white"
print(x) #after the change
print("**************************")