class Book:
    def __init__(self, title, author, publisher, ISBN, price, quantity):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ISBN = ISBN
        self.price = price
        self.quantity = quantity


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_book(self, ISBN, field, new_value):
        for book in self.books:
            if book.ISBN == ISBN:
                setattr(book, field, new_value)
                break
                # to exit the loop

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                break

    def search_book(self, keyword, search_by):
        found_items = []
        for book in self.books:
            if search_by == "title" and keyword.lower() == book.title.lower():
                found_items.append(book)
            elif search_by == "author" and keyword.lower() == book.author.lower():
                found_items.append(book)
            elif search_by == "ISBN" and keyword == book.ISBN:
                found_items.append(book)
            else:
                print("Not Found.")
        return found_items

bookstore = Bookstore()

book1 = Book("mathematics3", "Silverman", "Daneshgahi", "0316769177", "50", 150)
book2 = Book('To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott & Co.', '0446310786', 8.99, 5)
book3 = Book('1984', 'George Orwell', 'Secker & Warburg', '0452284236', 9.99, 3)

bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

search_results = bookstore.search_book('mathematics3', 'title')
for book in search_results:
    print(f'Title: {book.title}')
    print(f'Author: {book.author}')
    print(f'Price: ${book.price}')
    print('-' * 50)