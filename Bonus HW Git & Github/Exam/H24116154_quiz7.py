def display_menu() :
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit\n")

# To get the valid input from user
def user_choice() :
    while True:
        choice = input("Enter your choice (1-6): ")
        print()
        if choice.isdigit() and (1 <= int(choice) <= 6):
            return int(choice)
        else:
            print("Please enter a valid integer (1-6)!")

def add_book(dictionary) :
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
    while True:
        book = input("Enter the title, genre, and price of the book (separated by |): ")
        print()

        # Ensure the user input the valid format of book
        if book.count("|") == 2:
            title, genre, price = book.split("|")   # [title,genre,price]

            if len(genre) == 1 and genre.isupper():

                try:
                    price = float(price)
                    dictionary[title] = {"genre": genre, "price": price}  # {title1:{genre:genre1,price:price1},title2:{genre:genre2,price:price2}...}
                    print(f"Added {title} to the library.\n")
                    break
                except ValueError:
                    print("Please enter a valid number for the price!")

            else:
                print("Please enter \'an\' uppercase letter for the genre!")
        else:
            print("Please enter the valid format! (title|genre|price)")

    # print all books
    for title, info in sorted(dictionary.items()):
            print("%s (%s, $%.2f)"%(title,info["genre"],info["price"]))

def remove_book(dictionary) :
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    title = input("Enter the title of the book to remove: ")
    print()
    if title in dictionary:
        del dictionary[title]
        print("Removed %s from the library.\n"%title)
    else:
        print("Error: %s not found in the library.\n"%title)
    print()


def get_book_info(dictionary) :
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    title = input("Enter the title of the book: ")
    print()
    if title in dictionary:
        book = dictionary[title]
        print(f"Title: {title}\nGenre: {book['genre']}\nPrice: ${book['price']:.2f}\n")
    else:
        print(f"Error: {title} not found in the library.\n")
    print()

def list_all_books(dictionary) :
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """

    if dictionary:
        for title, info in sorted(dictionary.items()):
            print(f"{title} ({info['genre']}, ${info['price']:.2f})")
    else:
        print("No books in the library.")
    print()

def list_books_by_genre(dictionary) :
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    genre = input("Enter the genre to search for: ")
    print()
    
    books_in_genre = {title: info for title, info in dictionary.items() if info["genre"] == genre}
    if books_in_genre:
        for title, info in sorted(books_in_genre.items()):
            print(f"{title} ({info['genre']}, ${info['price']:.2f})")
    else:
        print(f"No books found in the {genre} genre.\n")

if __name__ == "__main__" :
    
    library = {} # initialization

    while True:
        print("="*40)
        display_menu()
        choice = user_choice()
        
        if choice == 6:
            print("Goodbye!")
            break
        
        elif choice == 1:
            add_book(library)
        elif choice == 2:
            remove_book(library)
        elif choice == 3:
            get_book_info(library)
        elif choice == 4:
            list_all_books(library)
        elif choice == 5:
            list_books_by_genre(library)

        print("="*40)
