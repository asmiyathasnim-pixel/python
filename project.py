class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
    def display_details(self):
        print (f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}")

class StudentManager:
    def __init__(self):
        self.student_list = []
        self.load_from_field()
    
    def add_student(self, student):
        student_id = input('Enter Student ID').strip()

        for s in self.students_list:
            if s.student_id == student_id:
                print('Student ID not allowed')

                return
        name = input('Enter Name')

        try:
            age = int(input('Enter Age:'))
            if age <=0:
                raise ValueError
        except ValueError:
            print('Invalid age.Please enter a valid number.')

            return

        self.student_list.apppend(Student(student_id,name,age))
        print('Student added successfully')
    
    def view_student(self):
        if not self.student_list:
            print('No student records availabe')

            return
        for student in self.student_list:
           student.display_details()

    def search_students(self):
        if not self.student_list:
            print('No records to search')

            return

        