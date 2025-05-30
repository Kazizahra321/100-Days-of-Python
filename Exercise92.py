# Exercise 92: Library management system in python

class Library:
    def __init__(self):
        self.no_of_books= 0
        self.books= []
    def add_books(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
         
    def show_books(self):
        print(f"No of Books are: {self.no_of_books} and books are: {self.books}")


    
l1 =Library()
l1.add_books("Harry Potter")
l1.add_books("Percy Jackson")
l1.add_books("Alice in Wonderland")
l1.show_books()


