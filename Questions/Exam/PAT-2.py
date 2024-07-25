'''
You have to design an application to find the Topper in each subject. 
There are three subjects like Machine Learning, Deep Learning, and Cloud Computing. 

"N" number of students registered for all three courses. 
After the CAT-1, they know the score for each subject out of 100 marks.

The faculty wants to know who is the topper in that list of students for individual subjects.

So your application should get input as "N" number of students with their marks as: 
Register_number followed by three marks - separated by spaces. [Ex. 1 87 67 54]

Note: If more than one student is in that topper list for the corresponding subject, 
the last student's register number will be printed. Marks should be in the range from 0 to 100. 

Any student's mark is less than 0 may not be considered for the ranking process.

Input: 
# First line - number of students [N]
# Next "N" lines have- Register_number mark1 mark2 mark3 - as single line separated by spaces


4
1 67 78 99
2 43 53 65
3 92 66 47
4 89 87 78

Output: #Three students' register numbers who secured top in that subject.
3    # 92 is maximum in 1st subject, So 3rd student
4    # 87 is maximum in 2nd subject, So 4th student
1    # 99 is maximum in 3rd subject, So 1st student

Input:
5
1 34 44 55 
2 66 77 88
3 99 98 67
4 99 96 95
5 88 78 69

Output:
4  #99 is the maximum - it is in 3rd and 4th, So 4th student
3  #98 is maximum - 3rd Student
4  #95 is maximum - 4th student

Input:
3
1 23 -8 99
2 77 90 89
3 66 43 92

Output:
2
2 
3  #Even though 99 is maximum,but in one of the subject 1st student got negative
    marks so that student may not be considered for the evaluation process.
'''

n = int(input("Enter the number of students: "))
max1=-1
max2=-1
max3=-1
for i in range(n):
    reg_numer, mark1, mark2, mark3 = input().split()
    regnumber = int(reg_numer)
    m1= int(mark1)
    m2= int(mark2)
    m3= int(mark3)
    if(m1 < 0 or m2 < 0 or m3 < 0):
        continue
    if(m1>=max1):
        max1 = m1
        index1 = i+1
    if(m2>=max2):
        max2 = m2
        index2 = i+1
    if(m3>=max3):
        max3 = m3
        index3 = i+1
print("The maximum marks in 1st subject is scored by student",index1)
print("The maximum marks in 2nd subject is scored by student",index2)
print("The maximum marks in 3rd subject is scored by student",index3)












'''
MovieGenreFinder
You plan to identify who likes what kind of movie genres in your class 
based on their movie genre rating ranges from 1 to 10[Integer]. 

Films are classified into three genres  "Comedy," "Romance," and "Action."

There are "N" students in your class, and you are getting data in the form of 
student_register number and rating of three genres like:
1 3 4 7
2 7 9 10

Note: If any rating is less than or equal to 1 may not be considered for the process- 
That person may not be counted for the average calculation

Find the average rating of each genre and display which kind of movie will be liked by your classmates.

Sample Input: 
# First Line Number of students - N
# Next "N" lines - RegisterNumber  genre1(Comedy)  genre2(Romance)  genre3(Action)
3
1 8 9 9
2 5 7 8
3 6 6 8

Output: 
6.33 7.33 8.33
Action  # Second line to be as "Action" because 8.33 is greatest among all three

Input :
4
1 8 9 6
2 8 7 5
3 2 5 2
4 8 7 2

Output:
6.5 7.0 3.75
Romance

Input :
5
1 10 10 7 
2 9 7 5
3 1 8 10
4 10 6 5
5 10 6 6 

Output: # Third person gives one as rating that person may not be considered for the average computation
9.75 7.25 5.75
Comedy

'''
n = int(input("Enter the no. of students: "))
sum1=0
sum2=0
sum3=0
count=0
for i in range(n):
    reg, rate1, rate2, rate3 = input().split()
    regno = int(reg)
    m1= int(rate1)
    m2= int(rate2)
    m3= int(rate3)
    if( m1<=1 or m2<=1 or m3<=1 ):
        continue
    sum1= sum1 + m1
    sum2= sum2 + m2
    sum3= sum3 + m3
    count = count + 1
avg1 = float(sum1/count)
avg2 = float(sum2/count)
avg3 = float(sum3/count)
if (avg1 >= avg2) and (avg1 >= avg3):
   max = 'Comedy'
elif (avg2 >= avg1) and (avg2 >= avg3):
   max = 'Romance'
else:
   max = 'Action'
print()
print (round(avg1,2), round(avg2,2), round(avg3,2))
print("The most popular Movie Genre in your class is",max)