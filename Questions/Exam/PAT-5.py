'''
WhoScoreIsThis
Three students [Zulu, Relu, Tanh] are writing three different exams for their IAS post-doctoral selection. 
Exams are Technical, Program, and Verbal. 
After the exams, we need to find who scored the particular total mark out of these three students.

Input: # Seven Lines 
#First six lines for student name followed by the marks scored by three different exams.
#Seventh line consists of the total score in which the program should display who scored that total score
# Student name followed by the three exam marks

Zulu
10 10 10
Relu
12 11 10 
Tanh
8 7 8 
30 # Seventh line - Party input - corresponding vote count to be displayed as output

Output :
Zulu

Input:
Zulu
15 11 11
Relu
8 12 8 
Tanh
8 8 8 
24 # Seventh line - Total Score - corresponding student name  to be displayed as output

Output :
Tanh
'''










'''
VoteCount
Three parties [PPK, SSM, MMK ]are conducting the local panchayat elections in Chennai with different wards. 
After the election, we need to find the number of votes secured by the given party.

All the parties may not contest in all the wards due to the unavailability of the candidates.

NOTE: MUST USE DICTIONARY Concepts 

Input: # Seven Lines -
# First six lines for party name followed by the number of votes scored by the party in each ward
# Seventh line consists of a party name in which the program should display the number of votes 
  secured by the party.
# Party name followed by the votes scored in different wards [Number of wards need not be the same], 
  repeats for the five parties

PPK
12 34 45 10
SSM
12 11 10 
MMK
5 10 8 9 10
SSM             # Seventh line - Party input - corresponding vote count to be displayed as output

Output :
33

 
Input:
PPK
10 10 15 
SSM
10 10 10 10 10 10  
MMK
5 5 5 5 5
MMK

Output :
25
'''


dict={}
party1=input("Enter the name of 1st party: ")
votes1=list(map(int,input("Enter the Votes secured by 1st party: ").split()))
party2=input("Enter the name of 2nd party: ")
votes2=list(map(int,input("Enter the Votes secured by 2nd party: ").split()))
party3=input("Enter the name of 3rd party: ")
votes3=list(map(int,input("Enter the Votes secured by 3rd party: ").split()))
party_output=input("Enter the name of party you want to know the vote count: ")
dict[party1]=sum(votes1)
dict[party2]=sum(votes2)
dict[party3]=sum(votes3)
print(dict[party_output])
