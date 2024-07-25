'''
Write a program that repeatedly prompts a user for integer numbers 
until the user enters 'done'. Once 'done' is entered, print out the largest and smallest 
of the numbers. If the user enters anything other than a valid number catch it 
with a try/except and put out an appropriate message and ignore the number. 
'''
max=None
min=None
while True:
    num = input("Enter the number: ")
    if num=="done":
        break
    try:
        number=float(num)
    except:
        print("Invalid Input !")
    if max is None and min is None:
        max = min = number
    elif number>max:
        max = number
    elif number<min:
        min = number
print("The maximum number is: ",max)
print("The minimum number is: ",min)
    