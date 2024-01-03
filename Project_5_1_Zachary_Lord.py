#!/usr/bin/env python3
#Zachary Lord
#Setting the task variable
TAX = 0.06
#Sales tax calculation
def sales_tax(total):
    sales_tax = total * TAX
    return sales_tax

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_aftertax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_aftertax)
    
if __name__ == "__main__":
    main()
