#!/usr/bin/env python3
#Zachary Lord

# display a welcome message
print("Welcome to the Future Value Calculator")
print()
choice = 'y'
while choice.lower() == 'y':
    
    monthly_investment = float(input("Enter monthly investment:\t"))
    while monthly_investment <=0:
        print('Entry must be greater than 0. Please try again.')
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <= 0:
            print()
        else:
            montly_investment= monthly_investment

    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))

# convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

# calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

# display the result
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

# see if the user wants to continue
        choice = input("Continue (y/n)? ")
        if choice == 'n':
            break

        print()
        print("Bye!")
