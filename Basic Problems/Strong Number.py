'''
A number is called a strong number if the sum of the factorial of its digit is equal to the number itself. For example 145 since
1! + 4! + 5! = 1 + 24 + 120 = 145
'''
num=input("Enter the number: ")
n=int(num)
sum=0
for i in num:
    fac=1
    for j in range(1,(int(i)+1)):
        fac=fac*j
    sum=sum+fac
if sum==n:
    print("YES, the given number IS a strong number")
else:
    print("NO, the given number IS NOT a strong number")
