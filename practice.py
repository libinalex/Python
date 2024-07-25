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
3   # 92 is maximum in 1st subject, So 3rd student
4    # 87 is maximum in 2nd subject, So 4th student
1    # 99 is maximum in 3rd subject, So 1st student

Input:
5
1 34 44 55 
2 66 77 88
3 99 98 67
4 99 96 95
5 88 78 69

Output:
4  #99 is the maximum - it is in 3rd and 4th, So 4th student
3  #98 is maximum - 3rd Student
4  #95 is maximum - 4th student

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

words = ["Hello", "Alex"]
for word in words:
    if word[0] in ['A', 'E']:
        word = word + 'ma'
    else:
        word.replace()