'''
PrintEvenOdd
You are going to print the numbers based on the input. 
[Program must have Two different functions called even and odd]

For example,
if your input is
even 2

The output should print the first two even numbers
0 2

odd 3 means output should print the first three odd numbers
1 3 5

Input
#First Line number of time invoke either odd or even prints
# Next "n" lines are either odd # | even #

3
odd 2
even 3
even 5

Output: # Print the results accordingly.
1 3
0 2 4
0 2 4 6 8

Input
#First Line number of time invoke either odd or even prints
# Next "n" lines are either odd # | even #

3
odd 3
even 2
odd 6 

Output: # Print the results accordingly.
1 3 5
0 2
1 3 5 7 9 11
'''


'''
def even():
    k=0
    i=0
    while k<n:
        if i%2 == 0:
            print(i,end=" ")
            k=k+1
        i+=1


def odd():
    k=0
    i=0
    while k<n:
        if i%2 != 0:
            print(i,end=" ")  
            k=k+1
        i+=1


count=int(input("Enter the number of times you want to evoke even or odd: "))
for j in range(count):
    type,num=input("Enter either even or odd following how many numbers: ").split()
    n=int(num)
    if type=="even":
        even()
    if type=="odd":
        odd()

'''



def even():
    k=0
    i=0
    evenlst=[]
    while k<n:
        if i%2 == 0:
            evenlst.append(str(i))
            k=k+1
        i+=1
    print(" ".join(evenlst))

def odd():
    k=0
    i=0
    oddlst=[]
    while k<n:
        if i%2 != 0:
            oddlst.append(str(i))  
            k=k+1
        i+=1
    print(" ".join(oddlst))

count=int(input("Enter the number of times you want to evoke even or odd: "))
for j in range(count):
    type,num=input("Enter either even or odd following how many numbers: ").split()
    n=int(num)
    if type=="even":
        even()
    if type=="odd":
        odd()
       





