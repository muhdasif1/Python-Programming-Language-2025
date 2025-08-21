first_name : str = "Muhammad"
last_name : str = "Asif"
full_name = first_name + " " + last_name
print(f"Mr. {full_name}")
print(f"""Hello {full_name} How are you""")
print()

print(first_name.upper())
print(first_name.lower())
print(first_name.title())

print(last_name.upper())
print(last_name.lower())
print(last_name.title())

print(f"name in uppercase: {full_name.upper()}")
print(f"name in lowercase: {full_name.lower()}")
print(f"name in titlecase: {full_name.title()}")

dir(str)