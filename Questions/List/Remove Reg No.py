"""
Remove_Reg_Number

Remove the even register number from the list.


Input:
5  # Number of elements in the list
21BAI1022 21BAI1231 21BAI1245 21BAI1222 21BAI1344 # Register Numbers in the list

Output:
21BAI1231 21BAI1245
"""
n=int(input("Enter the number of elements: "))
lst=input("Enter the register numbers: ").split()
even=['0','2','4','6','8']
odd=[]
for i in range(n):
    if lst[i][-1] not in even:
        odd.append(lst[i])
nlst=" ".join(odd)
print(nlst)