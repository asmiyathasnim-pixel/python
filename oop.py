class Car:

    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

    def start(self):
        print(f'{self.name} engine has started ')

car1 = Car('BMW',240000,'white')
car2 = Car('Maruthi', 58000, 'blue')

print(car1.name, car1.price, car1.colour)
print(car2.name, car1.price, car1.colour)
car1.start()
car2.start()

