"""
A function is a block of code that only runs when it is called
We can pass data to functions(parameters), and they can return data.

def function_name(parameters):
    #code block (indented)
    #perform actions using the parameters
    #return the value #optional
     
"""

# simple function without parameters

def my_function():
    print("this is my function") #this runs when the function is called

my_function()

def other_function():
    print("This is another function")


other_function()
my_function()

#function with parameters

def print_full_name(first_name, last_name, middle_name):
    print(f"the name is {first_name}, {last_name}, {middle_name}")

print_full_name("Leo", "Flores", "J")


def get_full_name(fname, lname):
    return f"{fname} {lname}" #sends back full name as text



#stores the returned value in a variable
full_name = get_full_name("Leo", "Flores")
print(full_name)


#functions with default perameters
#if no argument is provided when calling the function it will use that value


def greet(name="student"):
    print(f"hello, {name}! Welcome to class")

#calling with no arguments -> using default perameters
greet()

greet("Leo")

