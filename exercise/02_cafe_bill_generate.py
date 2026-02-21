""" 
☕ Use Case 2: Café Bill Generator
🎯 Goal Create a simple Python program that calculates and displays a customer’s café bill.

🧠 Instructions
> Create variables for:
- coffee_price (float)
- sandwich_price (float)
- cake_price (float)
- customer_name (string)

> Calculate the total bill using addition.
> Print the output in this format: Café Bill
- Customer Name: Ayesha Coffee: $2.5 Sandwich: $4.0 Cake: $3.0
- Total Bill: $9.5

💡 Bonus Challenge (Optional)
Add a line that thanks the customer:
print("Thank you for visiting our café,", customer_name + "!")
Expected Output: Thank you for visiting our café, Muhammad Asif!
"""

coffee_price: float = 19.20
sandwich_price: float = 23.4
cake_price: float = 25.5
customer_name: str = "Muhammad Asif"

total_bill = coffee_price + sandwich_price + cake_price

print("Café Bill")
print("Customer Name:", customer_name)
print("Coffee: $", coffee_price)
print("Sandwich: $", sandwich_price)
print("Cake: $", cake_price)
print("Total Bill: $", total_bill)
print("Thank you for visiting our café,", customer_name + "!")