#tuples are just like lists- they can store multiple items.
#but they are immutable (cannot be changed after creation)

my_tuple = ("apple","banana","cherry")
print(my_tuple)

#accessing items in tuple

print(my_tuple[0])
print(my_tuple[2])

#check if an item exists
if "apple" in my_tuple:
    print("Yes, apple is in the tuple")

#length of a tuple
print(len(my_tuple))

#single item tuple
#you must add a comma at the end or python won't recognize it as a tuple

single = ("grape")
print(type(single)) #this is a str
tuple = ("water",)
print(type(tuple)) #this is a tuple

# Nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

travel_bag = ("passport","shoes", "powerbank", "wallet","airtag")
print(travel_bag[1], travel_bag[3])

if "shoes" in travel_bag:
    print("You're ready to walk")
else:
    print("You forgot your shoes")

essentials = ("deoderant", "toothpaste", "toiletpaper")

final_bag = essentials + travel_bag 
#final_bag = (travel_bag, essentials) ##if i added them like this it'd be 2 seperate tuples in one?
print(len(final_bag)) #??? only 2 items because its 2 tuples together so technically 2 items
#print(len(travel_bag + essentials)) #this for both?
print(final_bag[-1])


