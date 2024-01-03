#Zachary Lord
#imports time related modules
from datetime import date, time, datetime, timedelta
#Display menu for the program
def display_menu():
    print('Arrival Time Calculator')
    print()

def main():
    #establishes time related variables
    date_of = input('Estimated date of departure (YYYY-MM-DD): ')
    time_of = input('Estimated time of departure (HH:MM AM/PM)' )
    miles =  int(input('Enter miles: '))
    mph = int(input('Enter miles per hour: '))
    #Formats the time related variables
    estimated_date = datetime.strptime(date_of,"%Y-%m-%d")
    date = estimated_date.strftime('%Y-%m-%d')
    estimated_time = datetime.strptime(time_of, "%H:%M %p")
    time= estimated_time.strftime('%H:%M %p')
    #calculations
    hours  =  miles // mph
    minn = ((miles - hours * mph)/ mph)* 60
    minTwo = int(round(minn, 0))
    times1 = datetime.strptime(str(hours), '%H:%M')
    #prints the results
    print('Hours:',hours)
    print('Minutes:',minTwo)
    print('Estimated Date of arrival:', date)
    print('Estimated Time of Arrival:', time)


if __name__ == '__main__':
    main()
