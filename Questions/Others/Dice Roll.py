'''
Write a program to find which number you got the maximum number of times out of 6 trials.

If you threw more than one number equally, then the least among that number to be printed.

The input is the sequence of 6 trails, 
output to be the number which came as many times as compared to other numbers in that 6 trails. 
-1, if the sequence is Invalid
'''

roll=input("Enter the 6 trials : ")
count=c1=c2=c3=c4=c5=c6=0
for i in roll:
    count+=1
    a=int(i)
    if a<=6:
        if a==1:
            c1+=1
        elif a==2:
            c2+=1
        elif a==3:
            c3+=1
        elif a==4:
            c4+=1
        elif a==5:
            c5+=1
        elif a==6:
            c6+=1
    else:
        print("-1")
        break
    if count==6:
        m=max(c1,c2,c3,c4,c5,c6)
        if m==c1:
            print("1")
        elif m==c2:
            print("2")
        elif m==c3:
            print("3")
        elif m==c4:
            print("4")
        elif m==c5:
            print("5")
        elif m==c6:
            print("6")
    if count>6:
        print("Enter only 6 trials")
        break
        

