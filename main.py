"""Library Mangement System"""


class Book:
    """Book class that have...."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Year: {self.year}")


class TextBook(Book):
    """TextBok....."""

    def __init__(self, title, author, year, subject):
        self.title = title
        self.author = author
        self.year = year
        self.subject = subject

    def display_info(self):
        print("Library_Name:", library_name)
        print(
            f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Subject: {self.subject}"
        )


library_name = "City Library"

b1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
b1.display_info()
b2 = Book("History of Rome", "Smith", 1998)
b2.display_info()
t1 = TextBook("Python Basics", "John Doe", 2020, "Programming")
t1.display_info()

print("\nIterating through books:")
for x in [b1, b2, t1]:
    print(x.title)
