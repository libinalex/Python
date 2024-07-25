'''
Failure_Count
A University has published the results of the term-end examination conducted in April. 
A list of failures in physics, mathematics, and chemistry, and computer science is available. 
Write a program to find the number of failures in the examination. 
This includes the count of failures in one or more subjects.

Input:
# Register number of failures in Physics, maths, chemistry, CS

Example :

19bai1023,19bai1024
19bai1028,19bai1027
19bai1023,19bai1024,19bai1029
19bai1023,19bai1024,19bai1025

Output:
#Count

6
'''

phy=input("Enter Reg no. of failures in Physics: ").split(",")
math=input("Enter Reg no. of failures in Maths: ").split(",")
chem=input("Enter Reg no. of failures in Chemistry: ").split(",")
cse=input("Enter Reg no. of failures in Computer Science: ").split(",")
total=phy+math+chem+cse
set_total=set(total)
print("No. of failures in the examination: ",len(set_total))