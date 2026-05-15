class Book:
    def __init__(self, isbn, title, author, pages, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.borrowed = False

    def do_borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title} borrowed"
        else:
            return f"{self.title} already borrowed"

    def do_return(self):
        if not self.borrowed:
            self.borrowed = False
            return f"{self.title} returned"
        else:
            return f"{self.title} already returned"

    def book_info(self):
        status = "Borrowed" if self.borrowed else "Not Borrowed"
        return f"ISBN: {self.isbn} \nTitle: {self.title} \nAuthor: {self.author} \nPages: {self.pages} \nYear: {self.year} \nStatus: {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} has been added to the library"

    def search_book(self, key_word):
        find_books = []
        for book in self.books:
            if (
                key_word.lower() in book.title.lower()
                or key_word.lower() in book.author.lower()
            ):
                find_books.append(book)
        return find_books

    def available_books(self):
        return [book for book in self.books if not book.do_borrow]

    def borrowed_books(self):
        return [book for book in self.books if book.do_borrow]

    def library_info(self):
        total = len(self.books)
        borrowed = len(self.borrowed_books())
        available = len(self.available_books())

        report = f"=== {self.name} ===\n"
        report += f"Total Books: {total}\n"
        report += f"Available Books: {available}\n"
        report += f"Borrowed Books: {borrowed}\n"
        return report


# Usage
library = Library("Main Library")

# Adding books
book1 = Book("123456", "Python Programming", "John Wick", 350, 2023)

book2 = Book("987654", "Data Science", "John Doe", 230, 2022)

# Adding books
library.add_book(book1)
library.add_book(book2)
print(book1.book_info())

print(library.library_info())

# Borrow a book
print(book1.do_borrow())
print(library.library_info())
print(book2.book_info())
