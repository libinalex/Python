n=int(input("Enter the no. to be checked: "))
for i in range(2,n):
    if n%i==0:
        print("Composite Number")
        break
else:
    print("Prime Number")
