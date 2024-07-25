'''
IdentifyVowels
You are given a string s consisting of lowercase English letters.
You have to identify the second vowel's position(index + 1).

If no vowels or only one vowel then print 0.

Input: # One line String
the vowels in english

Output: # Positon of the second vowel in the given string.
6

Input:
hi why shy

Output:
0

'''



string=input("Enter the string: ")
vovel='aeiou'
temp=""
for i in range(len(string)):
    if string[i] in vovel:
        temp = temp + str(i+1)
if len(temp)>1:
    print(temp[1])
else:
    print("0")



