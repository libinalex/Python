'''
VIT_ShoppingCart
Initially, you have an empty shopping_bag =[] in VITMART which has all the food items,
Start adding food items into that shopping_bag from the VITMART. 
After adding a few items there may be a possibility to remove the items from that shopping_bag.
This will be implemented  based on the commands like addItem #itemName and removeItem #itemName
At last, your program should print the items in the shopping_bag

Note: Create two functions, one if addItem and another one is for removeItem


Input: # Sequence of "N" commands and Next "N" lines start with addItem followed by either 
         addItem or  removeItem
5
addItem diarymilk
addItem munch
removeItem diarymilk
addItem 5star
addItem kitkat

Output: # List of items in that shopping_bag
munch
5star
kitkat


Input: # Sequence of "N" commands and Next "N" lines start with addItem followed by either addItem or  removeItem
6
addItem diarymilk
addItem bournville
addItem goodday
addItem 5star
removeItem bournville
removeItem diarymilk

Output: # List of items in that shopping_bag
goodday
5star
'''

shopping_bag =[]

def addItem():
    shopping_bag.append(item)

def removeItem():
    shopping_bag.remove(item)

n=int(input("Enter the number of items you wish to add or remove: "))
for i in range(n):
    action,item=input("add or remove Item followed by name: ").split()
    if action=="addItem":
        addItem()
    if action == "removeItem":
        removeItem()
for j in shopping_bag:
    print(j)