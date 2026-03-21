# sets are used to store multiple items in a single variable.
# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES

#sets are written with curly brackets { }

fruits = {"apple", "banana", "cherry"
}

print(fruits)

#no duplicates allowed
fruits = {"apple", "banana", "apple"}
print(fruits)

#check if an item exists
print("banana" in fruits)

#adding items
fruits.add("orange")
print(fruits)

#adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

#removing items
fruits.remove("banana")
print(fruits)

#removes an item even if knowing if it is a member of the set or not [will not throw error]
fruits.discard("kiwi")
print(fruits)

#set operations (like math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) #combining 2 sets(Duplicates will be removed :D)
print(set1.intersection(set2)) #returns common elements(showing duplicates in the sets)
print(set1.difference(set2)) #whats only in set1 and prints nothing else in set 2

invited_friends = {"Alex","Sam","Leo","Nina"} #my two sets
rsvped = {"Nina", "Sam", "Jordan"}

print(invited_friends.union(rsvped)) #a union of everyone invited printed
print(rsvped) #print of those who are coming
print(invited_friends.difference(rsvped)) #print who hasnt replied yet 
invited_friends.update(["Jason", "Derrick"]) #added 2 names to invited friends
print(invited_friends) 
rsvped.remove("Jordan") #removing someone
print(rsvped)

print(len(rsvped)) #the total of those who are still coming

if print("Leo" in rsvped) == True: #checking if leo shows
    print("Leo is still coming")
else:
    print("Leo aint showing :(")