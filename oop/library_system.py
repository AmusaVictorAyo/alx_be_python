class Book:
    # Base class representing a generic book
    def __init__(self, title, author):
        # Initialize common book attributes
        self.title = title
        self.author = author


class EBook(Book):
    # Derived class representing a digital book
    def __init__(self, title, author, file_size):
        # Initialize shared attributes from Book
        super().__init__(title, author)
        # Initialize ebook-specific attribute
        self.file_size = file_size


class PrintBook(Book):
    # Derived class representing a physical book
    def __init__(self, title, author, page_count):
        # Initialize shared attributes from Book
        super().__init__(title, author)
        # Initialize print-specific attribute
        self.page_count = page_count


class Library:
    # Library class demonstrating composition
    def __init__(self):
        # Store all book instances here
        self.books = []

    def add_book(self, book):
        # Add a book object to the library collection
        self.books.append(book)

    def list_books(self):
        # Print details depending on the book type
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, "
                    f"File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, "
                    f"Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")