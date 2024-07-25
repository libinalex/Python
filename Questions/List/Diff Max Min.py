'''
MixMaxList

Write a Program to find the difference between the maximum and minimum number from the list of 5 numbers.

Input: 5 numbers in an array - Fixed
1 6 4 2 3 

Output: One Line number: Difference between the maximum and minimum number.
5


Input:
20 30 10 50 40

Output:
40
'''

lst=input("Enter the list: ").split()
mx=int(max(lst))
mn=int(min(lst))
print(mx-mn)