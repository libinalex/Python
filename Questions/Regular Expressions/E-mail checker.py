'''
Check validity of the email id using regular expressions.

xyz@cts.com
ab12@in.co
a@a.in
libinalex10@gmail.com

'''

'''
import re
email=input("Enter the E-Mail: ")
if re.match("[a-z0-9]+[@][a-z]{1,3}[\.][a-z]{2,3}$",email):
    print("Valid")
else:
    print("Invalid")
'''

import re
email=input("Enter the E-Mail: ")
if re.match("[a-z0-9]+[@][a-z]+[\.][a-z]{2,3}$",email):
    print("Valid")
else:
    print("Invalid")