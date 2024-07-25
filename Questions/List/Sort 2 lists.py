'''
ConsolidatedItems
Zulu was the departmental store which was located near Chennai. 
It has two sections, with different items. 
You have to help Zulu to consolidate the list of items from the two different sections in a sorted manner.

Input 
# n1 - number of items in section 1
# n2 - number of items in section 2
# Followed by n1 number of lines represent the each items
# Followed by n2 number of lines represent the each items

3
2
Amul
Five Star
KitKat
Pepsi
Coke

Ouput : # List of items in sorted manner - Ascending order 
Amul
Coke
Five Star
KitKat
Pepsi

 

Input 
# n1 - number of items in section 1
# n2 - number of items in section 2
# Followed by n1 number of lines represent the each items
# Followed by n2 number of lines represent the each items

4
2
Gems
Five Star
KitKat
Pepsi
Coke
Orange

Ouput : # List of items in sorted manner - Ascending order 
Coke
Five Star
Gems
KitKat
Orange
Pepsi
'''

n1=int(input("Enter the no. of items in section 1: "))
n2=int(input("Enter the no. of items in section 2: "))
n=n1+n2
item=[]
for i in range(n):
    itm=input()
    item.append(itm)
item.sort()
for j in item:
    print(j)
