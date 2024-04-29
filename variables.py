#variables in python

first_name = 'John'
last_name = 'Gaita'
country = 'Kenya'
city = 'Nairobi'
age = 25
is_married = False
skills = ['HTML','CSS','Python','javascript']
personal_info ={
     'firstname' : 'John',
     'lastname'  : 'Gaita',
     'country'   :'Kenya',
     'city'      : 'Nairobi'
}

#printing the values stored in the variables

print('First name:',first_name)
print('First name length:', len(first_name))
print('last name:', last_name)
print('last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Personal information:', personal_info)

#Declaring multiple variables in one inline

first_name , last_name, country, age , is_married = 'John', 'Gaita', 'kenya', 25 , False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)