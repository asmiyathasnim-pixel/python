# Student Details Record 
# Write a program to store student details. 
# The program should allow changes to details, remove wrong data, and show the final 
# details. 

student = {
    "Name" : input('Enter your name: '),
    "Age" : int(input('Enter your age: ')),
    "Place" : input('Enter your place: '),
}

student.update({"Status" : 'Student'})
print(student)

student.update({"Place" :input('change your place: ')})
print(student)

del student["Place"]
print(student)

