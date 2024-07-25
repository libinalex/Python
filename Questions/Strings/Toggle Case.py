'''
ToggleCase
You have been given a String S consisting of uppercase and lowercase English alphabets. 
You need to change the case of each alphabet in this String. 
That is, all the uppercase letters should be converted to lowercase and 
all the lowercase letters should be converted to uppercase. 
You need to then print the resultant String to output.

Input:
ViT

Output:
vIt

Input:
Computer SCIENCE

Output:
cOMPUTER science
'''

'''
S=input("Enter String: ")
Toggled_Case=""
for i in S:
    j=i.swapcase()
    Toggled_Case+=j
print(Toggled_Case)
'''


S=input("Enter String: ")
Toggled_Case=S.swapcase()
print(Toggled_Case)