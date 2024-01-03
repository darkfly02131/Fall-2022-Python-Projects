#!/usr/bin/env python3
#Zachary Lord

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_gallon= float(input('Enter the cost per gallon:\t'))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used,1)
total_cost= gallons_used * cost_gallon
round(total_cost, 1)
cost_per= cost_gallon / 10
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print('Total Gas Cost:\t\t\t' + str(total_cost))
print('Cost per Mile:\t\t\t' + str(cost_per))
print()
print("Bye")


