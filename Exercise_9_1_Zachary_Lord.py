#!/usr/bin/env python3
#Zachary Lord
import locale as lc
lc.setlocale(lc.LC_ALL, "us")
#function purpose: Display welcome message
def display_welcome():
    print("The Quarterly Sales program")
    print()
#Function purp: get the quarterly sales from the user
def get_quarterly_sales():
    sales_list = []
    for i in range(4):
        sales = float(input("Enter sales for Q" + str(i+1) + ": "))
        sales_list.append(sales)
    return sales_list
#function purp: calculate the sales
def process_sales(sales_list):
    # calculate total
    total = 0
    for sales in sales_list:
         total += sales
    total = round(total, 2)

    # get count
    count = len(sales_list)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # get min and max
    lowest_quarter = min(sales_list)    
    highest_quarter = max(sales_list)
                
    # format and display the result
    print()
    print("{:20} {:>10}".format("Total:", lc.currency(total, grouping=True)))
    print("{:20} {:>10}".format("Average Quarter:",lc.currency(average, grouping=True)))
    print("{:20} {:>10}".format("Lowest Quarter:", lc.currency(lowest_quarter, grouping=True)))
    print("{:20} {:>10}".format("Highest Quarter:", lc.currency(highest_quarter, grouping=True)))

def main():
    display_welcome()
    sales_list = get_quarterly_sales()
    process_sales(sales_list)

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
