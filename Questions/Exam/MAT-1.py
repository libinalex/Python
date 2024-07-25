'''
ScoreCard
You are playing a board game, and you have to find the total score at last from the scorecard list.

The scorecard format should be 

The list consists of numbers [1 to 6] and three alphabets [ "S" and "L" ].
No two consecutive alphabets like S L or S S or L L or S S in the scorecard
The scorecard always starts with a number.
The scorecard ends with a unique alphabet E.
Scorecard Examples


3 2 5 S 1 E
2 S 3 5 5 6 L 3 L E
3 3 L 2 S 3 4 5 E
2 2 2 2 2 E
1 2 S 3 4 S 5 L E

The final score will be calculated based on the actions concerning two alphabets, S and L.

If you read S, remove the last number from the list.
If you read L, then add the last number to the list.
If it reaches E, add all the digits in the list based on the alphabets S and L update on the original scorecard list.
Input: #One line sting as list 3 2 5 S 1 E


3 2 5 S 1 E


Output: # Sum of the numbers in the updated list.
6
# The reason is that [ 3 + 2 + 1] = 6, 5 is removed from the list because the following item is S after five.


Input:
3 4 L 2 S 3 4 5 E
Output: # [ 3 + 4 + 4 + 3 + 4 + 5] , 3 first three, 4 second four, next #four is due to L , then 2 is removed because of S, then 3 4 5 . 
23


Input:
2 S 3 5 5 6 L 3 L E
Output:
#Updated list 3 5 5 6 6 3 3 
31

Input:
1 2 S 3 4 S 5 L E

Output:
# 1 3 5 5 
14

Input:
2 2 2 2 2 E


Output:
10
'''

scorecard=input().split()
final=[]
for i in range(len(scorecard)):
    if scorecard[i]=="S":
        final.pop()
    elif scorecard[i]=="L":
        final.append(scorecard[i-1])
    elif scorecard[i]=="E":
        updated=list(map(int,final))
    else:
        final.append(scorecard[i])
s=sum(updated)
print(s)