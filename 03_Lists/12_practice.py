print("=" * 50)
print("Adding Elements to Python Lists")
print("=" * 50)

# Family Members
print("\n👨‍👩‍👧‍👦 Family Members:")
members = ["Asif", "Gul", "Ayesha", "Aatif", "Shayan"]
members.append("Koko")
print(members)

print("\nMy Family:")
print(f"First bro: {members[0]}")
print(f"First sister: {members[1]}")
print(f"Second bro: {members[2]}")
print(f"Second sister: {members[3]}")
print(f"Third bro: {members[4]}")
print(f"Third brother: {members[5]}")
print(members[-1])

print("\n" + "=" * 50)
# Car Collection
print("\n🚗 Car Collection:")
car_list = ["BMW", "Audi", "Mercedes", "Ferrari", "Lamborghini", 
            "Honda", "Toyota", "Benz", "Porsche", "Ferrari"]
car_list.append("Benz S Class")
print(car_list)

print("\nMy Cars:")
print(f"First car: {car_list[0]}")
print(f"Second car: {car_list[1]}")
print(f"Third car: {car_list[2]}")
print(f"Fourth car: {car_list[3]}")
print(f"Fifth car: {car_list[4]}")
print(f"Sixth car: {car_list[5]}")
print(f"Seventh car: {car_list[6]}")
print(f"Eighth car: {car_list[7]}")
print(f"Ninth car: {car_list[8]}")
print(f"Tenth car: {car_list[9]}")

print("\n" + "=" * 50)


# insert() Method Example
print("\n🏠 Inserting Elements into a List:")
houses = ["House A", "House B", "House C", "House D"]
houses.insert(2, "House X")  # Insert "House X" at index 2
houses.insert(0, "House Y")  # Insert "House Y" at the beginning
print(houses)
print("\n" + "=" * 50)


# Remove() Method Example
print("\n🛠️ Removing Elements from a List:")
tools = ["Hammer", "Screwdriver", "Wrench", "Pliers", "Drill"]
tools.remove("Wrench")  # Remove "Wrench" from the list
print(tools)

people = ["Alice", "Bob", "Charlie", "David"]
del people[0]  # Remove "Charlie" from the list
print(people)
print("\n" + "=" * 50)


car_collection = ["Toyota", "Honda", "Ford", "BMW", "Audi"]
print(car_collection)
print("\n🚙 Car Collection Before Removal:")
car_collection.remove("Ford")  # Remove "Ford" from the list
del car_collection[1]  # Remove the second car (index 1)
print(car_collection)
print("\n" + "=" * 50)

