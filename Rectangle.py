#Zachary Lord
#The rectangle module for Project_12_1
#intializes Class
class Rectangle:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
    #creates area
    def area(self):
        return self.height * self.width
    #creates perimeter
    def perimeter(self):
        return (2*(self.height+self.width))
    #Creates rectangle based on L, W, & H.
    def createRectangle(self):
        firstLine= "* " * self.width
        middleLine = '*' + '  '* (self.width - 2) + " *"
        lastLine= [firstLine] + [middleLine]*(self.height - 2) + [firstLine]
        print('\n'.join(lastLine))
