 #!/usr/bin/env python3
#Zachary Lord
from Movie import Movie

#Lists the movies from the list
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            print(str(i)+ '. '+ row.getStr())
            i += 1
        print()
        
#Adds the movies into the list
def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = Movie(name, year )
    movie_list.append(movie)
    print(movie.name + " was added.\n")   
#Deletes a movie from the list
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie.getStr() + " was deleted.\n")
#Function for the display menu
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    movie_list = [Movie("Monty Python and the Holy Grail", 1975), Movie("On the Waterfront", 1954), Movie("Cat on a Hot Tin Roof", 1958)]
    display_menu()

    #While True loop for the functionality of the display menu
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
