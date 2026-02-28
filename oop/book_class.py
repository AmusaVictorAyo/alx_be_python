class Book:
    """Represents a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """
        Initialize a Book instance with basic metadata.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Human-readable string representation.
        Used when print(book) is called.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation that can recreate the object.
        Useful for debugging and logging.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor called when object is deleted.
        """
        print(f"Deleting {self.title}")