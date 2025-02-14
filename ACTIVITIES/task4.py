class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 20)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book2 = Book("The Hunger Games", "Suzanne Collins", 2008)
book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)

book1.describe()
book2.describe()
book3.describe()