'''
CovidDashboard
During this pandemic, assume that the number of COVID19 cases is varying day by across your city.  
You are requested to analyze the COVID19 situations. 
The ten consecutive days of COVID19 instances are given to you. 
You have to check for which day (including the 10th day) the number of cases was higher than or 
equal to its previous consecutive days. You will report the final result for each given ten days.

Sample Input and Output:

Input:#Two Lines
10  #First Line 10 Days
223 143 155 354 483 599 701 701 601 133  #Second Line - 10 days of COVID Count

Output: #Display the date on which the number of cases is high compared to the current day
1 1 1 4 5 6 7 8 8 8

#Explanation
#for example first day 223, which is highest, so 1 on day1.
#next day 143 which is less than 223, so day1 is higher compared to day2 so display 1 as it is.
#3rd day 155 still is less than day 1, so display 1 as it is
#4th day 354 which is higher than day1(223) --> display 4 and keep going........




Example 2
10
1 2 3 4 5 6 5 4 3 2

1 2 3 4 5 6 6 6 6 6
'''

n=int(input("Enter no. of days: "))
cases=input("Enter covid count of these days: ").split()
max=0
for i in range(n):
    if int(cases[i])>=max:
        count=i+1
        max=int(cases[i])
    print(count,end=" ")



