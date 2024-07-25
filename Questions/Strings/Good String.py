'''
GoodString
A string S is called a good string if and only if two consecutive letters are not the same.
For example, abcab and cda are good while abaa and accba are not.

Input: #[Length of the string is minimum 2 ]
ab

Output: #[Good String | Bad String]
Good String

Input:
abcab

Output:
Good String

Input:
accba 

Output:
Bad String
'''


'''
import re
str=input("Enter the string: ")
if re.match(".{2,}",str):
    print("Bad String")
else:
    print("Good String")
    
'''

str=input("Enter the string: ")
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        print("Bad String")
        break
else:
    print("Good String")

