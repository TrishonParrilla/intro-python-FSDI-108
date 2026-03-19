#1. arithmatic operators

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x / y
print(res)

res = x * y
print(res)

#2. assingment operators - used to assign values to variables
# = means "put the value inside the variable"

x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)

# 3. Comparison Operator
# used to compare two values
# same as if else

# == (equal to), != (not equal), <= >= (less/greater than)

#4. logical operator - used to combined conditional statements
#used with booleans True/False

#and -> Both must be true
x = 3
y = 10
z = 10

print(x == y and y == z) #false because both conditions must be true
print(x == y or y == z) #False, because at least one must be true
print(not x == y) # not -> flips True to False


#identiy operators - used to compare objects, not if theyre equal
#but if theyre the exact same object

#is -> checks if two things are the exact same
#is not -> checks if they are not the same
x = 3
y = 4
print(x is y)
print( x is not y)

#6. Membership operator -used to test if a sequence is presented in an object
# in -> checks if something exists in a sequence (list)
# not in -> checks if something does not exist inside 

x = [1, 2, 3, 4, 5] #this is a list

print(4 in x)
print(9 not in x)