'''
MaxPackage
The "n" number of students received "m" number of offers at VIT, Chennai. 
You need to find the maximum package out of all n students with m offers.

The input contains the number of students followed by Name of the students and the packages of each offer.

NOTE: Program should use function concepts and global keyword 


For example

Input: # n number of students >> n lines with the name of  the student followed by m offers
5
relu 2000 1500 7500 890 750 550
zulu 200 150 750 350 790 
tanh 100 500 1500
sinx 1000 1500 2000 250
cosx 900 800 700 200 500 

Output: # Maximum salary 
7500

 

Input: # n number of students >> n lines with the name of  the student followed by m offers
3
sinx 1000 1500 
cosx 900 800 700 200 500 
ohms 5000 750 9999 

Output: # Maximum salary 
9999

'''


def maximum():
    # global maximum_salary
    maximum_salary = max(salary)
    if maximum_salary > maxsal:
        return maximum_salary
    else:
        return maxsal


maxsal=0
n=int(input("Enter number of students: "))
for i in range(n):
    offers = input("Enter the name of student followed by offer: ").split()
    salary = list(map(int,offers[1:]))
    maxsal = maximum()
    
print(maxsal)