'''
Allows objects of diffrent classes to behave as objects of the same class
'''

class Animal:
    def speaks(self):       #abstract method which will e overwritten
        pass

class Dog(Animal):
    def speaks(self):
        print("Bark")

class Cat(Animal):
    def speaks(self):
        print("Meow")

class Cow(Animal):
    def speaks(self):
        print("Mooo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speaks()
cat.speaks()
cow.speaks()

'''
same function "speaks" is called, but different action is performed.
'''


# Compile-Time Polymorphism - Method overloading, Operator overloading

# In python, the last created function will only run, so function overloading doesn't work
'''
class Add:
    def sum(self, a, b):
        print(a+b)
    
    def sum(self, a, b, c):
        print(a+b+c)

sum1 = Add()
sum1.sum(3,5)
'''
# Run-time Polymorphism - method overriding