class Book:
    # Base class representing a generic book
    def __init__(self, title, author):
        # Common attributes for all books
        self.title = title
        self.author = author

    def __str__(self):
        # Human-readable representation for printing
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    # Derived class representing a digital book
    def __init__(self, title, author, file_size):
        # Initialize shared attributes from Book
        super().__init__(title, author)
        # EBook-specific attribute
        self.file_size = file_size

    def __str__(self):
        # Include file size in printed output
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    # Derived class representing a physical printed book
    def __init__(self, title, author, page_count):
        # Initialize shared attributes from Book
        super().__init__(title, author)
        # PrintBook-specific attribute
        self.page_count = page_count

    def __str__(self):
        # Include page count in printed output
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    # Library demonstrates composition by managing book objects
    def __init__(self):
        # Collection of Book / EBook / PrintBook instances
        self.books = []

    def add_book(self, book):
        # Add a book instance to the library
        self.books.append(book)

    def list_books(self):
        # Print each book using its own __str__ (polymorphism)
        for book in self.books:
            print(str(book))