'''
Program to shift all the elements of a list to given step left
'''
lst=input("Enter the list to shift all the elements given step left: ").split()
n=int(input("How many positions you want to shift left: "))
for j in range(n):
    t=lst[0]
    for i in range(len(lst)-1):
        lst[i]=lst[i+1]
    lst[-1]=t
print(" ".join(lst))


'''
Program to shift all the elements of a list to given step right
'''
lst=input("Enter the list to shift all the elements given step right: ").split()
n=int(input("How many positions you want to shift right: "))
for j in range(n):
    t=lst[-1]
    for i in range(len(lst)-2,-1,-1):
        lst[i+1]=lst[i]
    lst[0]=t
print(" ".join(lst))
