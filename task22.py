# 2⃣ Employee Salary System 
# Base class Employee → calculate_salary() 
# Subclasses: 
# ● FullTimeEmployee 
# ● Freelancer 
# ● Intern 
# Each calculates salary differently. 
# Methods / Concepts to Use: 
# ● Inheritance 
# ● Method overriding 
# ● Polymorphism 
# ● Constructor in subclasses 

class Employee:
    def __init__(self,name):
        self.name = name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
    
class Freelancer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
employees = [
    FullTimeEmployee("Varun", 60000),
    Freelancer("Meena", 500, 50),
    Intern("Vishnu", 150000)
]

for i in employees:
    print(f"{i.name}'s Salary : {i.calculate_salary()}")

    