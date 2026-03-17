# Overview:
# ● Introduction to Object-Oriented Programming (OOP)
# ● Classes and Objects
# ● Defining class attributes and methods
# 📖 Learning Resources:
# ● Python OOP (W3Schools)
# 📌 Tasks:
# ✅ Create a class Car with attributes brand, model, and year
# ✅ Create an object of Car and print its details


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_details()

