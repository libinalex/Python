'''
CountWord
Count the word from the given sentence using python dictionary.

Example. 
Input : #Line - statement 
Vit is in Chennai

Output: #Displays word: frequency 
Chennai : 1
in : 1
is :1
Vit : 1

Example 2:
Input:
learning to code is learning to create and innovate

Output:
and : 1 
code : 1 
create : 1 
innovate : 1 
is : 1 
learning : 2 
to : 2
'''

sentence=input("Enter the sentence: ").split()
print(sentence)
dict={}
for i in sentence:
    dict[i]=sentence.count(i)
for j in sorted(dict):
    print(j,":",dict[j])
