#Zachary Lord

def display_menu():
    print('The Wizard Inventory program\n')
    print('COMMAND MENU')
    print('show - Show all items')
    print('grab- Grab an item')
    print('edit- Edit an item')
    print('drop - Drop an Item')
    print('exit - Exit an item')
    print()

def show_item(inventory):
    i= 1
    for item in inventory:
        print(str(i) +'.' + item)
        i+=1
    print()

def grab_item(inventory):
    item= input('Name:')
    inventory.append(item)
    write_inventory(inventory)
    print(item + ' was added.')
        

def edit_item(inventory):
    num = int(input('Number: '))
    name = input('Name: ')
    inventory[num-1]= name
    write_inventory(inventory)
    print(inventory[num-1],'was updated.')

def drop_item(inventory):
    num= int(input('Number: '))
    inv = inventory.pop(num-1)
    write_inventory(inventory)
    print(inv +'  was deleted.\n')

def read_inventory():
    inventory = []
    with open('wizard_all_items.txt') as file:
        for line in file:
            line = line.replace("\n", "")
            inventory.append(line)
    return inventory
def write_inventory(inventory):
    with open('wizard_all_items.txt', "w") as file:
        for inv in inventory:
            file.write(inv + '\n')

def main():
    inventory = read_inventory() 
    display_menu()


    while True:
        command= input('Command: ')
        if command  == 'show':
            show_item(inventory)
        elif command == 'grab':
            grab_item(inventory)
        elif command == 'edit':
            edit_item(inventory)
        elif command == 'drop':
            drop_item(inventory)
        else:
            command  == 'exit'
            break
            



if __name__ == "__main__":
    main()

    
        
