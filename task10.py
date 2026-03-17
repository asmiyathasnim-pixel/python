# Complete Student Report 
# Write a program that collects student details, marks, and subjects, finds the final result, and 
# prints a complete report.

students = []

std = int(input("Enter Number of Students : "))

for i in range(std):
    print(f"Enter details for student {i + 1}")
    student = {
        "Name" : input("Enter name : "),
        "Age" : int(input("Enter age : ")),
        "Place" : input("Enter Place : "),
    }

    print(f"Enter you Marks")
    marks = {
        "sub1" : int(input("English : ")),
        "sub2" : int(input("Maths : ")),
        "sub3" : int(input("Chemistry : ")),
        "sub4" : int(input("Physics : "))
    }
    total = sum(marks.values())
    print("Total Marks : ", total)


    student["Total"] = total
    students.append(student)
    

print("Students Report")
cost = 1
for student in students:
    print(f"Student {cost}")
    print(f"Name : {student['Name']}")
    print(f"Age : {student['Age']}")
    print(f"Place : {student['Place']}")
    print(f"Total Mark : {student['Total']}")
    cost += 1