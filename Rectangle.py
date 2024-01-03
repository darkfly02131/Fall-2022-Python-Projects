#Zachary Lord
class Rectangle:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return (2*(self.height+self.width))
    def createRectangle(self):
        firstLine= "* " * self.width
        middleLine = '*' + '  '* (self.width - 2) + " *"
        lastLine= [firstLine] + [middleLine]*(self.height - 2) + [firstLine]
        print('\n'.join(lastLine))
