'''
OddMobileNumber
Write a python code to check the mobile numbers starting with only ODD numbers.
The program must use RegEx concepts.


Input: #Mobile Number.
9884814492

Output:#Valid or Not Valid
Valid


Input:
988234d456778

Output:
Not Valid


Input:
0123456789

Output:
Not Valid


Input:
4422668800

Output:
Not Valid
'''

'''
num=input("Enter the phone number: ")
if len(num)==10:
    if num.isdigit():
        if int(num[0]) %2 != 0:
            print("Valid")
        else:
            print("Not Valid")
    else:
        print("Not Valid")
else:
    print("Not Valid")
'''


import re
num=input("Enter the phone number: ")
if re.match("[13579][0-9]{9}$",num):
    print("Valid")
else:
    print("Not Valid")