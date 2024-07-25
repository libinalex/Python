'''
AgeCalculator
Create a function called calculate_age.

The function should define with two arguments.
The first argument is the birth_year as one of the parameters 
and the next argument as current_year = 2021 as a default one.

You have to invoke the function by passing birth_year as one of the arguments and compute your age.

Input: # Birth year.
2000

Output: # Age 2021-2000
21

Input: # Birth year.
2010

Output: # Age 2021-2010
11
'''

def calculate_age(birth_year,current_year=2021):
    print('Your age is:',current_year - birth_year)

birth_year=int(input("Enter your Birth Year: "))
calculate_age(birth_year)