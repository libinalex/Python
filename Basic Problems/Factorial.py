'''
# using while loop
num=int(input("Enter the number: "))
fac=1
while num>0:
    fac=fac*num
    num=num-1
print(fac)
'''
num=int(input("Enter the number: "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)