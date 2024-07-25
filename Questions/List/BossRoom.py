'''
BossRoom
From Zulu company, they arranged the summer camp for the 31 employees 
( 30 team members + 1 boss) at White Star resort which comprises 6 rooms. 
The company decided to give a separate room to the boss.  
All other employees should stay in the remaining 5 rooms. 
The room will accommodate the different numbers of people, with no fixed size.

The resort manager comes up with a random list that comprises the room numbers of 31 employees, 
including the boss.  You have to develop the software to find the boss's room from that manager's list.

Input: # Sinlge line with random room numbers including boss's room number - so 31 entries.
1 1 6 3 4 5 5 4 4 3 3 6 6 4 4 3 3 3 5 5 1 1 5 1 1 5 2 6 6 6 4 

Ouput: #Boss Room
2

Input: # Sinlge line with random room numbers including boss's room number - so 31 entries.
1 1 1 4 4 4 6 4 4 3 3 5 5 5 4 3 3 3 5 5 1 1 5 1 1 5 2 2 2 2 4 

Ouput: #Boss Room
6
'''
room_no = input("Enter the room number of all 31 employees: ")
lst = list(map(int, room_no.split()))
for i in range(1,7):
    if lst.count(i)==1:
        print("The room of Boss is:",i)
