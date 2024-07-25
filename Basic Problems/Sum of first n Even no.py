n=int(input("Enter the number: "))
i=1
sum=0
count=0
while count<n:
    if i%2==0:
        sum=sum+i
        count+=1
    i+=1    
print("The sum of first",n,"Even numbers is",sum)
