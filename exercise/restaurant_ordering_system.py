# Restaurant Ordering System

menu = {
    "Burger": 500,
    "Pizza": 1200,
    "Fries": 300,
    "Drink": 150
}

print("=== Welcome to Restaurant ===")

customer_name = input("Enter your name: ")

print("\nMenu:")
for item, price in menu.items():
    print(f"{item} - Rs.{price}")

item_name = input("\nEnter item name: ")

if item_name in menu:
    quantity = int(input("Enter quantity: "))
    
    total_bill = menu[item_name] * quantity
    
    print("\n===== Order Summary =====")
    print("Customer:", customer_name)
    print("Item:", item_name)
    print("Quantity:", quantity)
    print("Total Bill: Rs.", total_bill)
else:
    print("Item not available!")