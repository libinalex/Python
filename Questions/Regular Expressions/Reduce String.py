'''
ReduceString
Our target is to reduce the length of the given string [All are in lower case ]. 

The rule is:
1) If you identify any consecutive duplicate vowels, reduce like: 
aaaeiia --> aeia  , aeeiioou --> aeiou , aeiou--> aeiou , aeeeeeeee--> ae

Input String: #Lowercase small letter string
hellooooo

Output: #Reduced String
hello

Input:
amiiooyws

Output:
amioyws

Input:
aaeeiioouu

Output:
aeiou
'''


'''
import re
str=input("Enter String: ")
if re.search("[aeiou]{2,}",str):
    print("Yes")
else:
    print("no")
    
'''

'''
string=input("Enter the string: ")
vov="aeiou"
out=""
t=-1
for i in range(len(string)):
    if string[i] not in vov:
        out=out+string[i]
        t+=1
    else:
        if string[i] not in out:
            out=out+string[i]
            t+=1
        if not string[i]==string[i-1]:
            out=out+string[i]
print(out)
'''
import re
string=input("Enter the string: ")
st=re.sub("a+","a",string) 
st=re.sub("e+","e",st) 
st=re.sub("i+","i",st) 
st=re.sub("o+","o",st) 
st=re.sub("u+","u",st) 
print(st)


