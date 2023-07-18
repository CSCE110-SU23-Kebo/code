from math import *

def main():
    """
    Driver function
    """
    library = {} # This is library of books
    while True:
        print_menu()
        option = input("Choose a menu option: ")
        if option == "1":
            add_books(library)
        elif option == "2":
            print_books(library)
        elif option == "3":
            create_collections(library)
        elif option == "4":
            sort_collections(library)
        elif option == "5":
            delete_collection(library)
        elif option == "6":
            print("End", end="")
            break
        else:
            print("\nInvalid entry!")

def print_menu():
    """
    Prints the menu of options to the librarian
    """
    print(f"{'*'*6}Main menu{'*'*6}")
    print("1. Adds a book to the library")
    print("2. Print the books in the library")
    print("3. Create collections")
    print("6. Quit")
    print(f"{'*'*12}")


def add_books(library):
    """
    Adds a book to the library
    """
    entries = int(input("How many books would you like to enter? "))
    for book in range(1, entries+1):
        entry = input(f"Enter book {book}: ")
        ISBN = entry.split()[-1]
        title = entry[:-11].strip()
        print(f"Is the ISBN valid? {ISBN_is_valid(ISBN)}")
        print(f"Is ISBN in the library? {ISBN_in_library (library, ISBN)}")
        library[ISBN] = [title, -1] # Initialization of a book
    print(library)


def ISBN_is_valid(ISBN):
    """
    Checks if an ISBN is Valid:
    ~ The ISBN must be unique, ten digits, and should contain numbers only.
    """
    pass

def ISBN_in_library (library, ISBN):
    """
    Checks if an ISBN is in the library
    """
    pass

def print_books(library):
    """
    Print the books in the library
    """
    pass

def create_collections(library):
    """
    Creates a collection in the library
    """
    # library = { ISBN1: ['spiderman 2023', 23], ISBN2: ['dragon ball super', 23],  ISBN1: ['miles morales', 6], ISBN2: ['deadpool', 8]}
    

    print(f"The keys (ISBN) in the library are: {library.keys()}")
    print(f"The values ([title, collection]) in the library are: {library.values()} ")

    library_size = len(library)
    available_books = [library[ISBN][1] for ISBN in library.keys() if library[ISBN][1] == -1]
    print(f"List of available textbooks: {available_books}")
    number_of_available_books = len(available_books)
    print(f"The number of books in the library is: {library_size}")
    print(f"The number of books in the library is: {number_of_available_books}")

    collection_size = int(input("What is the size the collection?"))
    number_of_collections = ceil(number_of_available_books / collection_size)
    print(f"The number of collections is: {number_of_collections}")

    # Create a loop that repeats number_of_collections times and set the collection values to a collection number



def sort_collections(library):
    """
    Sorts the collections in the library
    """
    pass

def delete_collection(library):
    """
    Deletes a collection from the library
    """
    pass


if __name__ == "__main__":
    main() # Called only if the collections is running as standalone


