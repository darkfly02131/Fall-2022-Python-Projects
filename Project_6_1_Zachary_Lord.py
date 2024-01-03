#Zachary Lord

#Welcome message initialization
def display_menu():
    print('Tip Calculator ')
    print()

#Gets the decimal value of the cost of the item.
def cost_of():
    while True:
        try:
            cost= float(input('Cost Amount:'))
            if cost <=0:
                print(' Number must be greater than 0.')
            else:
                return cost
        except:
            print('Must be a valid decimal. Please try again.')
    
    

#Gets the tip percentage from the usr
def percent():
    while True:
        try:
            percent= int(input('Tip Percent: '))
            if percent <= 0:
                print('Must be a valid integer. Please try again.')
            else:
                return percent
        except:
            print('Must be a valid integer. Please try again.')
        
#Calculates all of the required things.
def main():
    display_menu()
    costOf= cost_of()
    tipPercent= percent()
    tip_amount= round(costOf * (tipPercent / 100),2)
    total= costOf + tip_amount

    #Displays the results
    print('\nOUTPUT')
    print ('Cost of Meal:\t ',str(costOf))
    print('Tip percent:\t ',str(tipPercent) + '%')
    print('Tip Amount:\t ',str(tip_amount))
    print('Total Amount:\t ',str(total))

if __name__ == '__main__':
    main()

