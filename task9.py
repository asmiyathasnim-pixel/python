# Multiple Students 
# Write a program that stores details of more than one student and prints each student’s 
# information clearly.

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"Enter details for Student {i + 1}")
    student = {
        "ID": input("Student ID: "),
        "Name": input("Name: "),
        "Age": int(input("Age: "))
    }
    students.append(student)

print(" Student Information ")
cost = 1
for student in students:
    print(f"Student {cost}")
    print(f"ID   : {student['ID']}")
    print(f"Name : {student['Name']}")
    print(f"Age  : {student['Age']}")
    cost += 1

    