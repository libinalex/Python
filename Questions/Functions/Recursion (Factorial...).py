'''
RecursiveDigitSum
Calculate the sum of digits using recursion 

Example:

Input:
9875

Output:
29


Input:
23

Output
5
'''

#Sum of Digits using for loop:-

# def sum(num):
#     sum=0
#     for i in num:
#         sum=sum+int(i)
#     print(sum)
# num=input("Enter the number: ")
# sum(num)


#Sum of digits using recursion:-

def sum(n):
    if n<10 and n>0:
        return n
        
    return n%10 + sum(n//10)

n=int(input('Enter the number: '))
result = sum(n)
print(result)




# Factorial using recursion:-

# def fact(n):
"""This is a recursive function
    to find the factorial of an integer"""

#     if n==0:
#         return 1
    
#     return n*fact(n-1)

# n=int(input("Enter the number to find factorial: "))
# result = fact(n)
# print(result)




#Fabonacci Series using recursion:-

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter the no. of terms in series: "))

if nterms <= 0:       # check if the number of terms is valid
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))