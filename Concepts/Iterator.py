"""
strings, list,...(data accessed via indexes) are iterable objects
So we can convert the into iterator
Inside for loop, iterable objects are converted to iterator, that's why we're able to iterate over them.

iter() can convert iterable object to iterator object
next() can extract iterator object one-by-one 
"""

"""
a = iter("Libin")
print(type(a))      -->  'str_iterator'

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))      --> error : next() function doesn't know when to stop!
"""

"""
generator is an object which keeps on generating new data keeping in mind what it generated last time
eg. range() function

a = range(10)
d = iter(a)

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

To create a custom generator:


def generate_cube(n):
    for i in range(n):
        yield i**3          

for i in generate_cube(9):
    print(i)

a = generate_cube(8)
print(a)

b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
"""


"""
Eg. Write a program to give a generator function to obtain first n fibonacci numbers

def generate_fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b

fibonacci = generate_fibonacci(15)
for i in fibonacci:
    print(i)
"""

"""
map() function also acts as a generator function"""

