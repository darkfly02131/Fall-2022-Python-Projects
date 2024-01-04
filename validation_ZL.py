#!/usr/bin/env python3
    
#function gets the float number from the user.
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low  and number < high:
            return number
        else:
            print('Entry must be greater than 0')
        
    
            
        

#function gets the int from the user   
def get_int(prompt):
    while True:
        number = int(input(prompt))
        if number > 0:
            return number
        else:
            print('Entry must be greater than 0')
    
    

def main():
    #While loop to see if the user wants to continue.
    choice = "y"
    while choice.lower() == "y":
        number = get_float('Enter a number: ', 0 ,10 )
        print(number, '\n')
        number = get_int('Enter a different number: ')
        print(number, '\n')
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
