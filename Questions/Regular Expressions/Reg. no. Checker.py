'''
YourRegNumber
Consider the VIT university Register number is listed as follows

<digit><digit><alphabet>< alphabet>< alphabet><digit><digit><digit><digit>

Your task is to figure out if the VIT University Register number is valid or not. 
A valid Register number will have all its letters in uppercase and digits in the same order as listed above. 
Use only regular expression for this program.

Input: #VIT register number
21BCE1999

Output:#Print Valid or Invalid
Valid


Input:
09BAI2001

Output:
Invalid


Input:
21BC12345

Output:
Invalid


Input:
19CSE9870

Output:
Valid
'''

import re
regno=input("Enter the registration no.: ")
if re.match("^[1-9][0-9][A-Z]{3}[0-9]{4}$",regno):
    print("Valid")
else:
    print("Invalid")

