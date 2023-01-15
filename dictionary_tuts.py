'''Dictionary class in Python'''

person = {
    "first_name": "Peter",
    "last_name": "Nwachukwu",
    "age": 30,
    "salary": 35000,
    "married": True
}
print(person)

# Looping all keys and values in Dictionary

# for key in person:
#     print(key)

# for key in person.keys():
#     print(key)

# for values in person.values():
#     print(values)

# for key,values in person.items():
#     print('key:',str(key),'values:',str(values))


# for key in person.keys():
    # print(key)
    # print(person)

#  Using Dictionary constructor

person2 = dict(first_name = "Bola", last_name = "Yemi")
print(person2)


people = dict(name= 'Williams', age= 33, sex= 'Male')
print(people,type(people))
print(type(people))



#   Get values in Dict

print(person["first_name"])

print(person.get("last_name"))

#   Adding

person["phone"]="09156222746"
print(person)

#  Get Dict Keys

print(person.keys())

#   Get items in Dict

print(person.items())

# Remove item

person.pop("phone")

print(person)


name = {
    'name': 'peter',
    'sex': 'male',
    'age': 21
}
print(name)


#  Looping in a DIctionary

#  for a in name:
#      print(a)

#  for a in range(0,len(a)):
#      print(a)

#  To get keys in Dictionary
print(name.get('age'))
print(name.keys())

#   To get items in Dictionary
print(name.items())

#   To add to a Dictionary
name['number']='+1 (915)-(622)-2746'
print(name)

print(name.items())




#  List of Dictionary

people = [
    {"name": "Peter", "age": 32},
    {"name": "John", "age": 23},
    {"name": "Daniel", "age":15},
]
print(people)

#  To get Dictionary key

print(people[1]["name"])



profile = [
    {'name': 'Johnson', 'age': 32},
    {'name': 'Samuel', 'age': 23},
]
print(profile)
print(type(profile))



people = [
    {'name': "Peter", 'age': 22, 'sex': "Male"},
    {'name': "Samuel", 'age': 23, 'sex': "Male"}
]
print(people)

# Looping all keys and values in Dictionary

for key in people:
    print(key)
