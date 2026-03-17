print("Hello World from Python") #No semicolons needed
print(2)
print(5 + 3)
print(True)

#shortcuts 
#saves a file - ctrl + s
#Run last command in Terminal - (up arrow)
"""
This is a comment
    This too
And this
"""

#variables and concatenation
name = "Leo"
age = 23
print(age) #prints the variable value

#concatenation (joining strings)
#fix it- cast age to string using str()
print("My name is " + name + " and I am " + str(age) + " years old.") 

name = "Parri"
age = 25
middle_name = "Antonio"
last_name = "Parrilla"
found = "false"

print(name)
print("My name is " + (name) + " and I am " + str(age) + " years old.")
print("Did he show up to class? " + str(found)) 

name = "parri"
place = "walmart"
price = 15
payment = "debit"

print(name + "went to " + place + "to get groceries and paid " + "$" + str(price) + " using " + payment)

# F-strings (formatted strings)
# Cleaner way to format strings

work = "sdgku"
job = "professor"
# start with f"", and variables in {}
print(f"I work at {work} and my job is {job}!")

#multi-line f-string
print(f"""
my name is {name} {middle_name} {last_name}
I like python!
    Type    indentations
""")


# type function

print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(found))  #<class 'str'>

#casting (changing data types)
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)


#User input
# input() lets the user type values

user_name = input("Enter Your name: ")
print(f"Hello, {user_name}")

#input always returns a string
print(input("Enter your age: "))

# Example: Converting input to int

new_age = int(input("Enter your age: "))
print(age + new_age)

pizza_slices = int(input("How many slices of pizza would you like?: "))
people = int(input("And how many people will be eating?: "))
people_per_slice = pizza_slices / people
print(f"There are {people_per_slice} slices of pizza for {people} people")

 