
# A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.

'''
# For numbers:
num=int(input("Enter the number: "))
rev=0
temp=num
while num>0:
    rev=rev*10 + num%10         # Reverse the no.
    num=num//10
if rev==temp:
    print("Yes, its a Palindrome")
else:
    print("No, its not a Palindrome")
'''
# For anything
n=input("Enter to be checked: ")
rev=n[::-1]
if rev==n:
    print("Yes, its a Palindrome")
else:
    print("No, its not a Palindrome")
