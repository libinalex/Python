'''
list.remove(value)
'''
lst=input("Enter the list: ").split()
val=input("Enter the value to delete: ")
flag=0
for i in range (len(lst)):
    if lst[i]==val:
        flag=1
        pos=i
        break
if flag==0:
    print("Element Not Found")
else:
    for j in range(pos , len(lst)-1):
        lst[j]=lst[j+1]
    lst.pop()
    print("List after deleting first occurance of given element: ",lst)