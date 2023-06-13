class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
 
    def square(self):
        return self.height * self.width
 
 
Rect = Rectangle(4, 9)
print(Rect.square())