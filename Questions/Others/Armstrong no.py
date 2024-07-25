'''
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits
is equal to the number itself. 153, 370, 371 and 407 are the Armstrong numbers.

For a 4 digit number, every digit would be raised to their fourth power to get the desired result.
1634, 8208, 9474 are a few examples of a 4 digit armstrong number.
'''

num=int(input("Enter the no. "))
n=num
count=0
while n>0:
    count+=1
    n=n//10
n=num
sum=0
while n>0:
    dig=n%10
    x=1
    for i in range(count):
        x=x*dig
    sum=sum+x
    n=n//10
if sum==num:
    print("Yes, the given number is an Armstrong Number.")
else:
    print("No, the given number is not an Armstrong Number.")

