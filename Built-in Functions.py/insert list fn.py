'''
list.insert(index,value)
'''

a=input("Enter the list: ").split()
a.append(None)
pos=int(input('Enter the position in which you want to insert:'))
val=input('Enter the value you want to insert:' )
for i in range(len(a)-2, pos-2, -1):
        a[i+1]=a[i]         

a[pos-1]=val
print("List after inserting value:",a)
''