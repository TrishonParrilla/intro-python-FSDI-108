# Dictionaries store data in Key:value pairs
# written with curly brackets {}

student = {
    "name" : "Leo",
    "age" : 23,
    "major" : "Computer Science"
}

print(student)

# Accessing items
print(student["name"]) #access by key
print(student.get("major")) #another way to access

# Adding Items
student["graduation_year"] = 2025
print(student)

#changing values
student["age"] = 25
print(student)

#removing Items
student.pop("major")
print(student)

#check if a key exists
if "name" in student:
    print("key 'name' exists in dictionary")


#nested dictionary
studnets = {
    "students1" : {"name": "Leo", "age": 22},
    "students2" : {"name": "Alex", "age" :21}
}

print(studnets["students2"]["age"])

"""
Mini challenge - Student Report card
store and analyze a student's grades.

1. create a dictionary called "report_card" with keys:
    - "name"
    -"subject"
    -"grades"  (use a tuple with 3 numbers)
#ex: {"name":"Leo", .... "grades":(90,85,88)}
2. print the student's name and subject.
3. calculate the average of the 3 grades (hint use sum() and len())
4. add a new key called "average" with the calculated result.
5. If the average is 90 or above -> print "EXCELLENT"
    if between 70 and 89 print "Good job"
    otherwise - print "Needs improvement"
    remove the "subject" key and print the updated dictionary
"""

print("=================================================")

report_card = {
    "name":"parri",
    "subject":"computer engineering",
    "grades":(50,83,99)
}

print(f"{report_card["name"]}, {report_card["subject"]}")
average = sum(report_card["grades"]) / len(report_card["grades"])
report_card["average"] = average
if report_card["average"] >= 90: #could use (average) variable also
    print("Excellent")
elif report_card["average"] >= 70 and report_card["average"] <= 89: 
    print("Good job")
else:
    print("Needs improvement")
print(report_card["average"])