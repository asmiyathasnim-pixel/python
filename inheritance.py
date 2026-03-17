class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def address (self):
        print(self.name,self.contact)


class Doctor(Person):
    pass
class patient(Person):
    pass

doc1 = Doctor('John',9009900909)
pat1 = patient('Riya',7887788778)

doc1.address()
pat1.address()

