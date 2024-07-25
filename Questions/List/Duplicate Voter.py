'''
Duplicate_Voter_ID
You are the chief election commission officer for your ward election. 
You have asked to develop an application that removes the duplicate voter ids from the list.

Input: #List of voter Ids[5 digits followed by 2 alphabets] with comma separation
12345ab,12345ab,23456cb,33445db,12346bb,66245ab,12346bb

Output: Unique Voter Ids.
12345ab,23456cb,33445db,12346bb,66245ab


Input:
78961zz,12345ab,78961zz,12345ab,55555gf

Output:
78961zz,12345ab,55555gf
'''

lst=input("Enter the list: ").split(",")
new_lst=[]
for i in range(len(lst)):
    if lst[i] not in new_lst:
        new_lst.append(lst[i])
nlst=",".join(new_lst)
print(nlst)