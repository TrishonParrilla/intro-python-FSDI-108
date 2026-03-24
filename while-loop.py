"""
A while loop repeats a block of code as long as a condition is TRUE.
Be careful - if the condition never becomes FALSE you'll get an infinite loop

While condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("count is: ", count)
    count += 1  #assignment operator adds 1 and loop stops at =5

    #using break to stop the loop

number = 0

while True: #infinite loop
    print(number)
    number += 1
    if number == 3:
        break #stop the loop when it reaches 3

#using CONTINUE to skip an iteration
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue #skip
    print(count)

print("---------------------------------------------------------")
# else with while loop
#the else block runs when the loop condition becomes False (Not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop is finished")

print("----------------------------------")

userLoggedIn = False
user_pass = False

while user_pass != "secret123":
    userLoggedIn = False
    user_pass = ((input("Enter Password:")))
    if user_pass != "secret123":
        print("wrong! Try again")
else:
    print("Access Granted")
    