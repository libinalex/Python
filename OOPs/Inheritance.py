'''
One class can inherit properties (attributes, functions) from another class
'''

'''

class Parent:
    parent_attribute = True
    def __init__(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()                  #accessing parent function
        print("This is a child class")
        print(self.parent_attribute)        #accessing parent attribute


child1 = Child()

'''

'''
Create a Bus child class that inherits from the Vehicle class. The default charge of any vehicle is seating capacity*100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintanance charge. So total fare for the bus instance will become the final amount = tatal fare + 10% of the total fare.
Eg. Vahicle fare: Rs. 5000
then, Bus fare: Rs. 5500.0


class Vehicle:

    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        return self.seating_capacity*100
    

class Bus(Vehicle):

    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
        
    def get_fare(self):
        vehicle_fare = super().get_fare() 
        maintenance_fare = 0.1 * vehicle_fare
        total_fare = vehicle_fare + maintenance_fare
        return total_fare
    
vehicle1 = Vehicle(50)
print("Vehicle fare:", vehicle1.get_fare())

bus1 = Bus(50)
print("Bus fare:", bus1.get_fare())
'''


# Multiple Inheritance
class A:
    def testA(self):
        print("This is class A")

class B:
    def testB(self):
        print('This is class B')

class C(A, B):
    def testB(self):
        print('This is class C')

objc = C()
objc.testA()
objc.testB()
objc.testC()

# Object of subclass C can access methods of both classes A and B

