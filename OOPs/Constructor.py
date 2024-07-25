# Special function that gets envoked every time an object is created for that class.


class Rectangle:
    def __init__(self, height, width):  # Parameterized  Constructor
        print(f"A rectangle is created with height:{height} and width:{width}")
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

    def __str__(self):      # must return a string object to print
        return "I'm now printing the class object. \nThe area of rect is: %d" %(self.height*self.width)     
        # Here we have overriden the __str__ method to print our custom output

rect1 = Rectangle(3, 4)
rect2 = Rectangle(6, 2)
rect3 = Rectangle(4, 10)

print("The height and width of the rectangle 1 are:", rect1.height, rect1.width)
print("The area of the rectangle 1 is:", rect1.area())
print("The area of the rectangle 3 is:", rect3.area())

print()

print(rect1)   # by default would give object location, but using __str__() now we'll get required output
print(rect1.__dict__)