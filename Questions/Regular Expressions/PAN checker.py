'''
In any of the country's official documents, the PAN number is listed as follows:
<alphabet> <alphabet> <alphabet> <alphabet> <alphabet> <digit> <digit> <digit> <digit> <alphabet>
Your task is to figure out if the PAN number is valid or not.
A valid PAN number will have all its letters in uppercase 
and digits in the same order as listed above.

ABCDE1234R
Valid

ABCDE12345
Invalid

ABCD01234R
Invalid

Abcde1234r
Invalid
'''



'''
#1
pan=input("Enter the PAN number :")
status="Valid"
if len(pan)!=10:
    status='Invalid'
else:
    for i in pan[0:5]:
        if i.isupper()==False:
            status='Invalid'
            break
    for i in pan[5:9]:
        if i.isdigit()==False:
            status='Invalid'
            break
    for i in pan[9]:
        if i.isalpha()==False:
            status='Invalid'
            break
print(status)  
'''
        


#2 
import re
pan = input("Enter the registration no.: ")
if re.match("^[A-Z]{5}[0-9]{4}[A-Z]$", pan):
    print("Valid")
else:
    print("Invalid")