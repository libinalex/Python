'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours 
worked above 40 hours.
'''

hrs = float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
n=hrs-40
if n>0:
    pay=rate*40 + n*rate*1.5
if n<0:
    pay=hrs*rate

print("The pay is: ",pay)
    