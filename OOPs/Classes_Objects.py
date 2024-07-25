class Student:
    def setName(self, name):
        self.name = name        # class attribute

    def getName(self):
        return self.name


student1 = Student()
student1.setName("Libin Alex")
print(student1.getName())

student2 = Student()
student2.setName("Ravi")
print(student2.name)
student2.marks = 40     # Instance attribute


class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle()
rect2 = Rectangle()

rect1.set_dimensions(4, 8)
rect2.set_dimensions(3, 4)

print("The area of rectangle 1 is:", rect1.area())
print("The perimeter of rectangle 2 is:", rect2.perimeter())
print("The area of rectangle 2 is:", rect2.area())

