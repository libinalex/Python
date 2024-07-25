# Map Function
def cube(n):
    return n**3

l = [2, 4, 7, 3, 5]

a = map(cube, l)
for i in a:
    print(i)

b = list(map(cube, [1, 2, 3, 4, 5]))
print(b)


# Lambda Function
"""
With the help of lambda, we can create in-line functions.
Also known as anonymous function
"""


def cube(x):
    return x**3

# we can write this above function in one line as:
cube = lambda x: x**3

l = [1, 2, 3, 4, 5]
a = list(map(cube, l))
print(a)

b = list(map(lambda n: n**2, [1, 2, 3, 4, 5]))
print(b)


# Reduce Function:
"""
reduce() function is not available by default, so we need to import it
"""
from functools import reduce

l = [2, 4, 5, 7, 8, 3]
#Task is to find the summation of all the elements (OR any aggregation operation)

def summation(x, y):
    return x + y

a = reduce(summation, l)
print(a)

b = reduce(lambda x, y: x + y, l)
print(b)

"""
Hence we can perform cumulative operations on an iterable using reduce function.
Also note that the function you pass in reduce() must have exactly 2 arguments
"""


# Filter Function
l = [2, 3, 5, 8, 7, 13, 4, 7, 5, 12, 4]

# Task is to filter out all the even numbers from the given list

def isEven(x):
    if x % 2 == 0:
        return True

a = list(filter(isEven, l))
print(a)

b = list(filter(lambda x: x % 2 == 0, l))
print(b)
