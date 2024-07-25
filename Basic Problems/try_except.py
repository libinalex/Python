''' 
When you don't want traceback error in your pragram and want it still to be executed
or want to put an error msg instead use try and except
Helps when you have a line of code that you know is dangerous.
'''

'''
str=input("Enter a number: ")
try:
    istr=int(str)        # Error if input is not in digits
except:
    istr=-1              # If any error, take default istr as -1
if istr>0:
    print("Good Job")
else:
    print("Not a number")
'''


output=0
while output==0:
    try:
        num=int(input("Enter a number: "))
        output=1
    except:
        print("Not a valid input! Enter only a number")
          
print("Your number is:",num)
