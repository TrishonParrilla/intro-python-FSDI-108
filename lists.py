# Lists are used to store multiple items in a single variable.
# A container that can hold many items
# Lists are written with square brackets [ ]

my_list = [10, 20, 30, 40, 50]
print(my_list)

# List can contain different data types

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) #first item (apple)
print(fruits[2]) #returns (Cherry)

# You can also use a Negative index to count from the end of the list
print(fruits[-1])

fruits[1] = "mango" #change banana -> mango
print(fruits)

#Adding Items 
fruits.append("orange") #adds/appends an item to the end of the list
print(fruits)

fruits.insert(1, "kiwi") #adds itself to a specific index
print(fruits)

#removing items
fruits.remove("apple") #removes last item
print(fruits)

fruits.pop() #removes last index when empty
print(fruits)

"""fruits.pop(0) #can specifiy where
print(fruits)"""

#looping through list
for fruit in fruits:
    print(fruit)

#check if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

#print list length
print(len(fruits)) #number of items in list