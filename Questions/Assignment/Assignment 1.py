
'''1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.

for i in range(1999, 3201):
    if(i%7 == 0 and i%5 != 0):
        print(i, end=",")
'''


'''2.
Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.

first = input("Enter the first name: ")
last = input("Enter the last name: ")
print('{} {}'.format(last, first))
'''


'''3.
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3

import math
diameter = int(input("Enter the diameter of the sphere: "))
volume = 4/3 * math.pi * ((diameter/2) ** 3)
print(volume)
'''


'''4.
Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.

numbers = input("Enter comma separated elements for the list: ").split(',')
numbers_list = list(map(int, numbers))
print(numbers_list)
'''


'''5.
Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

n = 5
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()
for i in range(5,0,-1):
    for j in range(i-1):
        print("* ", end="")
    print()
'''


'''6.
Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA

str = input("Enter the string: ")
print(str[::-1])
'''