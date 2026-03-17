# 5⃣ Library Book Issuer 
# Create Library class: 
# ● Store books 
# ● Issue one by one using iterator 
# Methods / Concepts to Use: 
# ● __iter__() 
# ● __next__() 
# ● Custom iterator 
# ● StopIteration 

class Library:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.books = file.read().splitlines()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return f"Issued Book: {book}"
        else:
            raise StopIteration


library = Library("books.txt")

for book in library:
    print(book)

    