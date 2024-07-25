'''
TopGradeChances
The median is the value separating the higher half from the lower half 
of a data sample, a population, or a probability distribution.

If the data set has an odd number of observations, the middle one is selected. 
For example, the following list of seven numbers:
1, 3, 3, 6, 7, 8, 9
has a median of 6, which is the fourth value.

If the data set has an even number of observations, there is no distinct middle value, 
and the median is usually defined to be the arithmetic mean of the two middle values.
For example, this data set of 8 numbers
1, 2, 3, 4, 5, 6, 8, 9
has a median value of 4.5, that is (4+5)/2 = 4.5

From the given list of marks, you need to identify 
how many of them are greater than or equal to median + 20 marks 
which help to understand how many of them are in Top Grade.

Input: # Marks 
55 66 43 36 92 21

Output: # Two lines - First line median, Second-line how many students are above (median + 20) 
# Median
# Number of students is greater than or equal to median + 20

49
1


Input: 
87 76 54 88 74

Output: 
76
0
'''


mrk=input("Enter the Marks: ").split()
count=0
mrk.sort(key=int)
if len(mrk)%2 != 0:
    x=len(mrk)//2
    med=mrk[x]
else:
    x=len(mrk)//2
    med=(int(mrk[x-1])+int(mrk[x]))/2

for i in mrk:
    if int(i) >= (int(med)+20):
        count+=1
print(med)
print(count)
        
    


