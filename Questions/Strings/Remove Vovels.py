'''
RemoveChars
Remove the vowels from the given string using Regular Expression.

Vowels to be represented like vowel_pattern =[aeiouAEIOU]

Example : 

Hello World

Hll Wrld 

Happy Days

Hppy Dys
'''


str=input("Enter the String: ")
vov="aeiouAEIOU"
out=""
for i in str:
    if i not in vov:
        out+=i
print(out)