# Input values
total_students: int = 100
faculty_members: int = 12
total_staff: int = 4
total_absent: int = 15
milk_per_person: int = 250

# Calculate total members present
calculation = total_students + faculty_members + total_staff - total_absent
print(f"Total Members: {calculation}")

# Calculate total milk required
total_milk = calculation * milk_per_person
print(f"Total Milk: {total_milk}g")
