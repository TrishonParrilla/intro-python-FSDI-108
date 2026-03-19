# if -> checks a condition
# elif- (else if) checks another condition if the first is False
# else -> runs of all other conditions are false

x = 10

if x > 5: 
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#shorthand IF statements

if x > 5: print("x is greater than 5")

#short hand if .else

print("even") if x % 2 == 0 else print("odd")

# nested IF statements
if x > 0:
    if x < 20:
        print("x is a positive number that is less than 20")


#combining conditions
age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")


print("=============================================")
jacket = False
print("Enter Today's Temperature")
today_temp = int(input())

if today_temp >= 86:
    print("It's hot outside!")
elif today_temp >= 68 and today_temp < 86:
    print("The weather is nice")
elif today_temp >= 50 and today_temp < 68:
    print("its a bit chilly")
else: 
    print("It's cold")
    
if today_temp < 59:
    jacket = True
if jacket == True:
    print("Better wear a jacket")
else: 
    print("No jacket needed.")