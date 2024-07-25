'''
VITEEE2022_Results
The results file contains your Register Number and VITEEE entrance marks.

You have to build a python application to retrieve the VITEEE marks from the files 
and display them to the users.

The results file content is given below.
21BAI12344 34.45
21BAI34567 86.23
21BAI10001 44.44
21BAI20201 33.45
21BAI30331 67.23

You have to get the registration number from the user and check if the number 
is present in the results file, If yes display the marks else display as Invalid User

Example 

Input : # Registeration number
21BAI20201

Output: # Marks or  Invalid User
33.45



Input : # Registeration number
21BAI20222

Output: # Marks or  Invalid User
Invalid User
'''

file=open("results.txt","r+")
reg_no=input("Enter the registration number to check result: ")
data=file.readlines()
for lines in data:
    reg,marks = lines.split()
    if reg == reg_no:
        output = marks
        break
    else:
        output="Invalid User"
print(output)
file.close()