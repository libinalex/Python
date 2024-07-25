'''
n=input("Enter the number: ")
sum=0
for i in n:
    sum=sum+int(i)
print("The sum of digits of the given number is",sum)
'''
n=int(input("Enter the number: "))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("The sum of digits of the given number is",sum)