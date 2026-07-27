class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_checked_out = True
                break

book_1 = Book("The C++ Programming Language", "Bjarne Stroustrup")
book_2 = Book("Automate the Boring Stuff with Python", "Al Sweigart")
book_3 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")

library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.checkout_book("The Hitchhiker's Guide to the Galaxy")

print(book_3.is_checked_out)