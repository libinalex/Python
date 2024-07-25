'''
100s(OneTwoZeros)
You are required to check whether given number consisting of 1 and 0 s is valid or not. 

The numbers should be 100, 110000........1^n(00)^n, n ranges from 1 to 3 

The numbers should start with 1 followed by zeros. 
One constraint is all the ones should come before zeros. 
So, the number of zeros is equal to the number of 1s * 2.

Invalid numbers are 101, 11, 1000, 111000,........1000000.............'''

num=input("Enter the number : ")
for i in range(1,4):
    x=("1"*i)+("00"*i)
    if x==num:
        print("Yes")
        break
else:
    print("No")
        