'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, print "$$" instead of the empty string.

Example :

Input :
vit chennai

output
viai

Input:
so

Output:
soso

Input
a

output
$$
'''

str=input("Enter string: ")
a=str[0:2]
b=str[-2:]
if len(str)>1:
    print(a+b)
else:
    print("$$")