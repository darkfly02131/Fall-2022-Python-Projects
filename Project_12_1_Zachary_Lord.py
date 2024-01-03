#Zachary Lord
from Rectangle import Rectangle
def main():
    print('Rectangle Calculator')
    while True:
        height = input('{:11}'.format('Height:'))
        width = input('{:11}'.format('Width:'))
        p1 = Rectangle(height, width)
        print('{:8}'.format('Perimeter:'),p1.perimeter())
        print("{:10}".format('Area:'),p1.area())
        p1.createRectangle()
        print()
    
        choice = input('Continue? (y/n):')
        if choice == 'n':
            break
        
if __name__ == '__main__':
    main()

        
    
            
        


    
