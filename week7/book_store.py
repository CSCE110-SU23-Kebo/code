import book_library

import random

def print_books(bookstore):
    """
    Print two versions of the dictionaries containing book records
    """
    """
    Types of bookstore
    1 # bookstore = { ISBN1: ['spiderman 2023', 23], ISBN2: ['dragon ball super', 23],  ISBN1: ['miles morales', 6], ISBN2: ['deadpool', -1]}
    1 # bookstore = { ISBN1: ['spiderman 2023', 23, price], ISBN2: ['dragon ball super', 23, price],  ISBN1: ['miles morales', 6, price], ISBN2: ['deadpool', 8, price]}
    """

    for ISBN, record in bookstore.items():
        if len(bookstore[ISBN]) == 2:
            print(f"{'ISBN:':<6}{ISBN:<11}{'Title:':<7}{record[0]:<20}{'Collection:':<12}{record[1]:<4}")
        elif len(bookstore[ISBN]) == 3:
            print(f"{'ISBN:':<6}{ISBN:<11}{'Title:':<7}{record[0]:<20}{'Collection:':<12}{record[1]:<4}{'Price:':<7}{record[2]:<6}")


def set_prices(starting_price, ending_price, bookstore):
    """
    This function adds a price record to the dictionary of books
    """
    for ISBN, record in bookstore.items():
        price = round(random.uniform(starting_price, ending_price), 2)
        bookstore[ISBN].append(price)


def main():
    """
    This is the entry point of the bookstore program
    """
    bookstore = {} # dictionary
    while True:
        book_library.print_menu()
        option = int(input("Enter an option: "))
        if option ==1 :
            book_library.add_books(bookstore)
        elif option==2:
            print_books (bookstore)
        elif option == 8:
            starting_price = float (input("Starting price"))    
            ending_price = float (input("Ending price"))
            set_prices(starting_price, ending_price, bookstore)
        elif option == 6:
            print("End", end="")
            break

main()