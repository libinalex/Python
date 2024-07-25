'''
DistinctAverageMarks
Mr.Raju wants to find the average of n marks with distinct values from the list of marks. 
The input two lines, number of students, and next line details of the mark.

Input: #Two Lines, the first line number of students, Second-line marks list 
10
10 10 20 40 50 20 10 30 100 10 

Output:
41.66


Input:
5
20 10 20 40 40 

Output:
23.33
'''

num=int(input("Enter the number of students: "))
mrk=list(map(int,input("Enter the marks: ").split()))
mrk_set=set(mrk)
sum=sum(mrk_set)
count=len(mrk_set)
avg=sum/count
formated="{:.2f}".format(avg)
print("The average marks are: ",formated)