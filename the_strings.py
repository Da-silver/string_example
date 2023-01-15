'''Strings in python'''

course = "Python Course For Beginners "
name = "Johnson Bernard"
school = "Barachel Group Of School"
age = 26

print(course)
print(name)
print(school)
print(age)


# String concatenation

print("Hello,my name is " + name)
print("I am " + str(age))



# Dot notation

print("welcome to coding class".upper())
print(course.upper())
print(school.upper())

name= "emma"
print(name.capitalize())



# String formatting, F-String Format

print(f"Hello,my name is {name} and i am {age}")

# Len short form for Length

print(len(course))
print(len(name))




# Methods With Strings

# make all lower

course = "PYTHON FOR BEGINNERS"
print(course.lower())

# Replace
course = "                      python for beginners"
print(course.replace("beginners","intermidiate"))
print(course.strip())
print(course)





name = "Bernard"
age = 32
print(f"My name is {name} and i am {age} years")


name = "John Tete"
print(name.strip())
print(name)
print(name.find("h"))
print(name.isalpha())
print(name.isalnum())


course = "computer science"
course2 = "computer_science"
print(course.split())
print(course2.split("_"))
print(course.replace("computer","Environmental"))
print(course.replace("computer","Political"))

name = "Johnson Drey"
print(name.startswith("J"))
print(name.startswith("w"))
print(name.endswith("y"))
print(name.endswith("Y"))
print(len(name))



name = "    Nwachukwu Peter Yahsom"
print(name)

print(name.strip())

print(name.split())

print(name.index("N"))

print(name.replace("Nwachukwu","Daniel"))
print(name)

print(name.count("e"))

print(name.count("a"))


name = "Harold Berk"
age = 56

print(name)

print("my name is " + name)

print(f"my name is {name} and i am {age} years old")



s = "hey what\'s up"
print(s)

print("c:useradminjava")
