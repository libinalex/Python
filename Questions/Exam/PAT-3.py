'''
You installed a multipurpose sensor in your farmland to collect environmental data like 
the year, month, timestamp, temperature level, and air quality.

The sample data is given below as a single line.
'0029029070999991902010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00331+99999098351ADDGF102991999999999999999999'

The red color captures the year of the data, purple color represents the temperature on that day. 
The light green represents the air quality on that day.

You have to write the program to check which year you have a minimum temperature out of given "N" days and 
apply that year along with the Year, Temperature as well as the quality of the air[1- 10 1 for  low, 10 for high].

Input:

# Number of sensor data "N"

# "N" number of sensor data as given above.

2

0029029070999991902010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00331+99999098351ADDGF102991999999999999999999

0029029070999991982010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00213+99999098351ADDGF102991999999999999999999

Ouput: # print one line - Minimum temperature of ____ during the year _____ with the air quality of __

Minimum temperature of 21 during the year 1982 with the air quality of 3

Input:

# Number of sensor data "N"

# "N" number of sensor data as given above.

3

0029029070999991921010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00431+99999098351ADDGF102991999999999999999999

0029029070999991922010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00413+99999098351ADDGF102991999999999999999999

0029029070999991992010720004+64333023450FM-12+000599999V0202501N027819999999N0000001N9-00515+99999098351ADDGF102991999999999999999999

Output: # print one line - Minimum temperature of ____ during the year _____ with the air quality of __

Minimum temperature of 41 during the year 1922 with the air quality of 3
'''

import re
number = int(input("Enter no. of Sensor data: "))
min1=None
temp1=None
air_qulaity=None
for i in range(number):
    n = input("Enter sensor data: ")
    year=n[15:19]
    temp=n[89:91]
    air=n[91:92]
    #print(year)
    #print(temp)
    if temp1 is None:
        temp1=int(temp)
        air_quality = air
    elif(int(temp)<temp1):
        year1= year
        temp1= int(temp)
        air_quality = air
        #print(air_quality)
print("Minimum temperature of "+ str(temp1) + " during the year "
+ year1 + " with the air quality of " + air_quality)









'''
Barcode was generated for every student who attempted the VITEE 2021. It comprises lots of data such as 
username, password, course applied, marks obtained, and so on.

The example data was given below, 

0029029070999991902010720004+npprakashFM-12+000599999V0202501N027819999999N0000001N9-00331+99999098351ADDGF34.45102991999999999999999999

The light blue highlights the user name of the applicant and the red color points out the marks scored out of 100.
You have to program to find the user who scores less and print the user name and the marks among all "N" students.

Example: 

Input :

# First Line number of applicants "N" 

# "N" number of applicants VITEE details.

2
0029029070999991902010720004+npprakashFM-12+000599999V0202501N027819999999N0000001N9-00331+99999098351ADDGF34.45102991999999999999999999
0029029070999991999010720004+vitcsecheFM-12+000599999V0202501N027819999999N0000001N9-00345+99999098351ADDGF45.56102991999999999999999999

Output:

npprakash user scored 34.45

Input :

4
0029029070999991902010720004+npprakashFM-12+000599999V0202501N027819999999N0000001N9-00331+99999098351ADDGF34.45102991999999999999999999
0029029070999991999010720004+vitcsecheFM-12+000599999V0202501N027819999999N0000001N9-00345+99999098351ADDGF45.56102991999999999999999999
0029029070999991903010720004+iitramusuFM-12+000599999V0202501N027819999999N0000001N9-00356+99999098351ADDGF55.55102991999999999999999999
0029029070999991999010720004+testuseruFM-12+000599999V0202501N027819999999N0000001N9-00468+99999098351ADDGF12.34102991999999999999999999

 Output:

testuseru user scored 12.34
'''