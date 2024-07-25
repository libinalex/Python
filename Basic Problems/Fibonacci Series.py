'''
num=int(input("Enter required no. of digits in sequence: "))
if num>0:
    a=0
    b=1
    if num==1:
        print(a)
    
    else:
        print(a)
        print(b)
        for i in range(num-2):
            c=a+b
            print(c)
            a=b
            b=c
else:
    print("Invalid Number")
'''
num=int(input("Enter the number: "))
x=0
y=1
z=0
if num>0:
    for i in range(num):
        print(z)
        x=y
        y=z
        z=x+y
else:
    print("Invalid Number")