'''
# 1. Program to read contents of a file line by line:
f=open("Hello.txt","r")
str=" "
while str:
    str=f.readline()
    print(str)
f.close()



# 2. Program to find the number of lines in a file

fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines in the file is:",num_lines)
'''

'''
# 3. Program to count the no. of characters in a file 
# and also the no of characters excluding any ul characters and leading & trailing white spaces 

f=open("Hello.txt","r")
str=" "
size=0
tsize=0
while str:
    str = f.readline()
    size = size + len(str)
    tsize = tsize + len ( str.strip() )
print("The total number of characters in the given file is: ",size)
print("The no. of characters excluding any ul characters or leading & \
       trailing white spaces in the given file are: ",tsize)
f.close()



# 4. Program to find the longest Word in a file

file = open("vovel.txt", "r")
longest=""
data = file.readlines()
for lines in data:
    words = lines.split()   #splits the variable when space is encountered
    for i in range(len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
print("The longest word in the file is: ",longest)       
file.close()      



# 5. Program to count the frequency of a word in a file

file = open("vovel.txt", "r")
name=input("Enter the word whose frequency you want to calculate: ")
freq=0
data = file.readlines()
for lines in data:
    words = lines.split()   #splits the variable when space is encountered
    freq = freq + words.count(name)
            
print("The frequency of the given word is: ",freq)       
file.close()    

'''

# 3. Program to count the frequency of words in a file

file = open("vovel.txt", "r")
freq={}
count=0
data = file.readlines()
for lines in data:
    words = lines.split() 
    for i in words:
        if i in freq:
            freq[i] +=  words.count(i)
        else:
            freq[i] = words.count(i)

file.close()
print("The frequency of words in the file is: ")   
for j in sorted(freq):
    print(j,":",freq[j])


'''
# 7. Program to write input names into file using writelines()

f=open("Hello.txt","w")
n=int(input("Enter no. of values: "))
lst=[]
for i in range(n):
    val = input("Enter the value: ")
    lst.append(val + "\n")
f.writelines(lst)
f.close()


'''



