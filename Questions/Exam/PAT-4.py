'''
IPLPurseMoney
You have to develop a python program that displays the remaining amount left out for 
each IPL team[8 IPL Teams] after the player retention assumed that each team 
retained at least one player with a maximum of four players.

The input format to be like - 
#TeamName, TotalBudget[100 Cr], First_player_retention_amt, Second_player_retention_amt, 
Third_player_retention_amt, Fouth_player_retention_amt 

#Note : Not always four players - Minimum of one , maximum of four.

CSK,100,15,12,10,8
DC,100,12,8
KKR,100,12,12
MI,100,17,10,8,8
PBKS,100,12
RR,100,12,12,7
RCB,100,10,10,7,7
SRH,100,8,7

Output: #List the team Names, remaining purse amount, Maximum amount spend for a single player

CSK 55 15
DC 80 12
KKR 76 12
MI 57 17
PBKS 88 12
RR 69 12
RCB 66 10
SRH 85 8
'''


for i in range(8):
    team=input("Enter the team info: ").split(",")
    amt=list(map(int,team[2:]))
    max_amt=max(amt,key=int)
    rem_amt=100-sum(amt)    
    print(team[0],rem_amt,max_amt)