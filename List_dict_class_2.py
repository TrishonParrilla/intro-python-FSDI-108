print("===========================") #just added lines for clarity
print("List Assignment")
print("===========================")

list_values = [5, 10, 15, 20, 25, "Parri"] #step 1

print(list_values) 

print("=====================") 

print(list_values[0]) #step 2 also accessing by iterating(kinda the same as printing the entire list i guess? idk)

print("====================")

for list_item in list_values: #this is apart of step 2 with the iterating part
    print(list_item)

print("====================") 

list_values[0] = 1 #step 3 replacing the 0th index in the list
print(list_values)

print("=====================")

list_values.pop(0) #step 4 removing something by index
print(list_values)

print("=====================")

print(list_values) #step 5 list value and length
print(len(list_values))

print("========================")
print("Dictionary Assignment")
print("========================")

team_info = {
    "team":"trailblaizer", #step 1 creating a dictionary with 3 key value pairs
    "size": 15,
    "record":(15,5) 
}

print(team_info["team"]) #step 2 access value using key

print("=========================")

team_info["mascot"] = "bird" #step 3 adding a new key
print(team_info["mascot"])
print(team_info)

print("=========================")

team_info["size"] = 10  #step 4 replacing value in dict
print(team_info["size"])
print(team_info)

print("==========================")

team_info.pop("mascot") #step 5 removing a key from dict
print(team_info)

print("===========================")