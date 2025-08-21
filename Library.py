import json
import os

BOOKS_FILE = 'books.json'

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r') as f:
                self.books = json.load(f)
        else:
            self.books = []

    def save_books(self):
        with open(BOOKS_FILE, 'w') as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author):
        book = {
            'title': title,
            'author': author,
            'available': True
        }
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def remove_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"Book '{title}' removed.")
                return
        print("Book not found.")

    def borrow_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                if book['available']:
                    book['available'] = False
                    self.save_books()
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently borrowed.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                if not book['available']:
                    book['available'] = True
                    self.save_books()
                    print(f"You have returned '{title}'.")
                else:
                    print(f"'{title}' was not borrowed.")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
            return
        for idx, book in enumerate(self.books, 1):
            status = "Available" if book['available'] else "Borrowed"
            print(f"{idx}. {book['title']} by {book['author']} - {status}")

def menu():
    library = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter title to remove: ")
            library.remove_book(title)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            title = input("Enter title to borrow: ")
            library.borrow_book(title)
        elif choice == '5':
            title = input("Enter title to return: ")
            library.return_book(title)
        elif choice == '6':
            print("Exiting Library System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
