'''
Username and Password
To get the username and password from the user and check whether it is valid or not.

Rules for the user name is it should contain only alphanumerics [alphabets, numbers]. 
It should not start with numbers. The underscore is also permitted in any position of the username. 
Length should range from five to eight. The username must contain at least one alphabet. 

Rules for the password are that It should contain digits, alphabets, and special characters like [!@#$%^&*()-+].
The length of the password must be 8. 
Password should have at least one uppercase, one lowercase, one special character and one digit. 


Input: # Two Lines - One User Name, Second Line: Password
Npprak1_
vit@123C

Output: #One Line
Valid User 


Input: # Two Lines - One User Name, Second Line: Password
12344144
CSE@123C

Output: #One Line
Not a Valid User


Input: # Two Lines - One User Name, Second Line: Password
Npprak1_
vit@123C

Output: #One Line
Valid User 


Input: # Two Lines - One User Name, Second Line: Password
_Npprak1
CSE@123C

Output: #One Line
Not a Valid User


Input: # Two Lines - One User Name, Second Line: Password
_Npprak1
CSE@c123

Output: #One Line
Valid User 
'''

import sys
import re
temp = 0
sp_chr="!@#$%^&*()-+"
user = input("Enter the Username: ")
pas = input("Enter the Password: ")
if re.match("[a-zA-Z_]\w{4,7}$",user):
    if len(pas)==8:
        for i in pas:
            if i.isdigit():
                temp=1
            if temp==1:
                for i in pas:
                    if i.isupper():
                        temp=2
            if temp==2:
                for i in pas:
                    if i.islower():
                        temp=3
            if temp==3:
                for i in pas:
                    if i in sp_chr:
                        print("Valid User")
                        sys.exit(0)
        else:
            print("Not a Valid User")
            sys.exit(0)
else:
    print("Not a Valid User")     

