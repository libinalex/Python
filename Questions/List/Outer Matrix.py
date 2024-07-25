'''
FenceHouse
Mr. UNK planned to build a fence  3 * 3 ( 3 rows and 3 columns). 
You have to help Mr.UNK to check whether that fence is properly constructed or not.

The rule for the proper fence is that all the outermost element is represented by one 
[Other elements ranges from 0-9]. If anyone of the outermost value is other than one then 
the fence is not proper.

Example for the proper fence.
1 1 1 
1 0 1
1 1 1 

Example for the fence which is not proper.
1 0 1
1 0 0
0 0 0 

You have to write a python program to check whether the fence is proper or not.

Input # Nine numbers - Rowwise in matrix 
1
1
1
1
1
1
1
1
1

Output : One line # Proper Fence / Not a Proper Fence 
Proper Fence

 

Input # Nine numbers - Rowwise in matrix 
0
1
1
1
1
1
1
1
0

Output : One line # Proper Fence / Not a Proper Fence 
Not a Proper Fence
'''
lst=[]
for i in range(9):
    n=int(input("Enter the number: "))
    lst.append(n)
if lst[:4]==[1,1,1,1] and lst[5:]==[1,1,1,1]:
    print("Proper Fence")
else:
    print("Not a Proper Fence")

