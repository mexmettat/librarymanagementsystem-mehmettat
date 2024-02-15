class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ").strip()
        while not title:
            print("Title cannot be empty. Please enter a valid title.")
            title = input("Enter the book title: ").strip()

        author = input("Enter the book author: ").strip()
        while not author:
            print("Author cannot be empty. Please enter a valid author.")
            author = input("Enter the book author: ").strip()

        release_year = input("Enter the release year (numeric): ")
        while not release_year.isdigit():
            print("Invalid input. Please enter a numeric value for the release year.")
            release_year = input("Enter the release year (numeric): ")

        pages = input("Enter the number of pages (numeric): ")
        while not pages.isdigit():
            print("Invalid input. Please enter a numeric value for the number of pages.")
            pages = input("Enter the number of pages (numeric): ")

        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ").strip()
        while not title_to_remove:
            print("Title cannot be empty. Please enter a valid title.")
            title_to_remove = input("Enter the title of the book to remove: ").strip()

        self.file.seek(0)
        lines = self.file.read().splitlines()
        updated_books = [line for line in lines if title_to_remove not in line]

        if len(updated_books) == len(lines):
            print(f"Book with the title '{title_to_remove}' not found. Deletion process not performed.")
        else:
            self.file.seek(0)
            self.file.truncate()
            self.file.write('\n'.join(updated_books))
            print(f"Book '{title_to_remove}' removed successfully!")

    def search_books(self):
        search_term = input("Enter search term (title, author, or year): ").strip().lower()
        while not search_term:
            print("Search term cannot be empty. Please enter a valid search term.")
            search_term = input("Enter search term (title, author, or year): ").strip().lower()

        self.file.seek(0)
        lines = self.file.read().splitlines()
        found_books = []

        for line in lines:
            book_info = line.split(',')
            if search_term in [book_info[0].lower(), book_info[1].lower(), book_info[2].lower()]:
                found_books.append(line)

        if found_books:
            print("\nFound Books:")
            for book in found_books:
                print(book)
        else:
            print("\nNo books found.")

# Create an object named "lib" with "Library" class
lib = Library()

# Create a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search Books")
    print("5) Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.search_books()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

