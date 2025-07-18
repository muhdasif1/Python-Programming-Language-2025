# Personal Information
first_name = 'Muhammad'
last_name = 'Asif'
country = 'Pakistan'
city = 'Peeshawar'
age = 19
is_married = False
skills = ['Python','c++' , 'Agents','openai-sdk','langGraph']

# Dictionary to hold more info
person_info = {
    'firstname': first_name,
    'lastname': last_name,
    'country': country,
    'city': city,
    'age': age,
    'is_married': is_married,
    'skills': skills
}

# Print Information
print('--- Personal Details ---')
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)

#  Declaring Multiple Variables in One Line
first_name, last_name, country, age, is_married = 'Muhammad', 'Asif', 'Pakistan', 19, False

# Re-print after re-declaration
print('\n--- Re-declared Info ---')
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
