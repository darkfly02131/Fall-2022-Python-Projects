#!/usr/bin/env python3
#Zachary Lord

#function shows the books in the book catalog
def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print("Title:""    " + title)
        print("Author:   " + book["author"])
        print("Pub year: " + book["pubyear"])
    else:
        print("Sorry, " + title + " doesn't exist in the catalog.")
#Function lists the books that're in the list
def list_book(book_catalog):
    movie1= list(book_catalog.keys())
    for movie1 in book_catalog:
        book = book_catalog[movie1]
        print("Title:   " + movie1)
        print("Author:  " + book["author"])
        print("Pub year :" + book["pubyear"])
        print()
        
#Function adds a new book to the list
def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "add" and title in book_catalog:
        print(title + " already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(title + " doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    author = input("Author name: ")
    pubyear = input("Publication year: ")
    
    # Create a dictionary for the book data
    book = {"author": author,
            "pubyear": pubyear}

    # Add the book data to the catalog using title as key
    book_catalog[title] = book
#Function deletes the books
def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " removed from catalog.")
    else:
        print(title + " doesn't exist in the catalog.")
#Function to display the menu of the list
def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("list - List book")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    display_menu()
    #establish Book catalog list
    book_catalog = {
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien", 
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    while True:
        print()
        command = input("Command: ").lower()
        if command == 'list':
            list_book(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
