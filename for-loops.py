"""
A for loop in python is a control structure that elts you repeat a block of code for each
item in a sequence (such as a lit, string, tuple, range of numbers ect..)


for variable in sequence:
    # Code block runs for each item in the sequence
"""

#basic example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for letter in "Leopoldo":
    print(letter)

print("_________________________________________")

#range() generates a sequence of numbers
for x in range(5): #indexes by 0
    print(x)

print("_________________________________________")
#Start end range
for x in range(2, 6):
    print(x)

print("_________________________________________")

#step
for x in range(0, 10, 2):
    print(x)

print("_________________________________________")

print("pick a number: ")
num = int(input())
print("-----")
for i in range(1,11):
    num_prod = num * i
    print(num_prod)
