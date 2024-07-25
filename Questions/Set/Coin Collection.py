'''
CoinCollection
Your friend has a huge collection of coins across different countries.
He/She asked you to give a python program to find the total number of distinct counties coins.

Input:
# First Line, Number of coins( N) 
#Next N lines - country names

5
India
India
Nepal
Pakistan
USA

Output: # NUmber of distinct countries coins
4

Input:
6
India
Brazil
Brazil
USA
USA
USA

Output: # Number of distinct countries coins
3
'''

n=int(input("Enter the number of coins: "))
country=set()
for i in range(n):
    inp=input("Enter the country name: ")
    country.add(inp)
print("The number of distinct country coins is:",len(country))