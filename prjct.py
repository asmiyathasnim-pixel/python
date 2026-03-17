class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == True:
            raise Exception("Book is already borrowed.")
        else:
            self.is_borrowed = True

    def return_book(self):
        if self.is_borrowed == False:
            raise Exception("Book was not borrowed.")
        else:
            self.is_borrowed = False

    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"
        return self.title + " by " + self.author + " - " + status

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def view_books(self):
        if len(self.books) == 0:
            print("No books in library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                book.borrow()
                print("Book borrowed successfully.")
                self.save_books()
                found = True
                break
        if found == False:
            raise Exception("Book not found.")

    def return_book(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                book.return_book()
                print("Book returned successfully.")
                self.save_books()
                found = True
                break
        if found == False:
            raise Exception("Book not found.")

    def load_books(self):
        try:
            file = open("library_data.txt", "r")
            for line in file:
                data = line.strip().split(",")
                title = data[0]
                author = data[1]
                status = data[2]
                book = Book(title, author)
                if status == "True":
                    book.is_borrowed = True

                self.books.append(book)

            file.close()
        except:
            file = open("library_data.txt", "w")
            file.close()

    def save_books(self):
        file = open("library_data.txt", "w")
        for book in self.books:
            file.write(book.title + "," + book.author + "," + str(book.is_borrowed) + "\n")
        file.close()

library = Library()

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added.")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("Enter title to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter title to return: ")
            library.return_book(title)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")

    except Exception as e:
        print("Error:", e)