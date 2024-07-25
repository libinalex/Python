'''
TelephoneDiary
Given 'n' names and phone numbers, assemble a phone book that maps friends' names 
to their respective phone numbers. 
You will then be given a name to query your phone book for the number. 
If the name is queried, print the associated entry from your phone book else print Not Found

Input: 
#First Line number of entries - 'n'
# n number of Name and mobile_number
#last input is the "Name" you want to search in the dictionary.

5
prakash 9884814492
sachin 1234567899
msd 999999999
kohli 7878787878
rohit 1212121212
sachin

Output:
1234567899

Input: 
6
prakash 9884814492
sachin 1234567899
msd 999999999
kohli 7878787878
rohit 1212121212
robin 1223343490
apple

Output:
Not Found
'''

dict={}
n=int(input("Enter the number of entries: "))
for i in range(n):
    name,mobile=input("Enter the name and mobile numbers: ").split()
    dict[name]=mobile
out_name=input("Enter the name you want to search in dictonary: ")
if out_name in dict:
    print(dict[out_name])
else:
    print("Not Found")
