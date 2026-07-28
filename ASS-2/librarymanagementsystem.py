class Library:
    def __init__(self):
        self.books = []

  
    def add(self, book):
        self.books.append(book)
        print(f"'{book}' added successfully.")


    def remove(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' removed successfully.")
        else:
            print("Book not found.")

    def search(self, book):
        if book in self.books:
            print(f"'{book}' is available in the library.")
        else:
            print(f"'{book}' is not available.")

    
    def display(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")



library = Library()


while True:
    
    print("1. Add New Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add(book)

    elif choice == "2":
        book = input("Enter book name to remove: ")
        library.remove(book)

    elif choice == "3":
        book = input("Enter book name to search: ")
        library.search(book)

    elif choice == "4":
        library.display()

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")