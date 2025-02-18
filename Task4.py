class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book Info: '{self.title}' by {self.author}, published in {self.year_published}")

# Create three book objects
book1 = Book("Solo Leveling", "Chugong", 2024)
book2 = Book("One Piece", "Eiichiro Oda", 1997)
book3 = Book("Harry Potter", "J.K. Rowling", 1997)

# Display their details
book1.describe()
book2.describe()
book3.describe()