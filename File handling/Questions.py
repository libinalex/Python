'''
1. Program to get the name and birth year from users and write their name and age into the file
format:< Name Age > {Name of the file: age}.
'''
'''
file = open("age.txt","w+")
n=int(input("Enter the number of users: "))

for i in range(n):
    name=input("Enter the name: ")
    year=int(input("Enter their birth year: "))
    age=2021-year
    file.write(name + " ")  
    file.write(str(age) + "\n")

file.close()
f=open("age.txt","r")
print(f.read())

'''

'''
2. Write a function in python to count the number of lines from a text file that does not start with vowels. 
The function should take the name of the file as an argument.

vovel:

A boy is playing there.
There is a playground.
An airplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password.



Input: # Read the name of the file
vowel

Output: #  No of lines not starting with vowels 
2


name = input("Enter the name of the file(followed by '.txt'): ")
vovel=["a",'e','i','o','u','A','E','I','O','U']
file = open(name,"r+")
count=0
for line in file:
    if line[0] not in vovel:
        count+=1
print(count)





3. Program to write input < Roll no., Name, Marks scored > into a file in the given format {csv format}
also read the data in python 


file = open("student.txt","w+")
n=int(input("Enter the number of students: "))

for i in range(n):
    roll=input("Enter the Roll Number: ")
    name=input("Enter the Name: ")
    mark=input("Enter the marks scored: ")
    data = roll + ", " + name + ", " + mark + "\n"
    file.write(data)

file.close()
f=open("student.txt","r")
print(f.read())





'''
'''
4. Create a students.txt file which contains: 
Roll_no, Name, M1, M2 and M3

Generate a result.txt file which contains:
Roll_no, Total , Average and Grade [ above 80 % “O” , 60 to 79% “A” and others in “P”]

'''

file = open("students.txt","w+")
n=int(input("Enter the number of students: "))
for i in range(n):
    roll = input("Enter the Roll no.: ")
    name = input("Enter the name: ")
    m1 = input("Enter the marks scored in 1st subject(out of 10): ")
    m2 = input("Enter the marks scored in 2nd subject(out of 10): ")
    m3 = input("Enter the marks scored in 3rd subject(out of 10): ")
    output = roll +" "+ name+" "+m1+" "+m2+" "+m3 + "\n"
    file.write(output)
file.close()

f = open("students.txt","r+")
data = f.readlines()
for j in data:
    rol,nam,m1,m2,m3 = j.split()
    total = int(m1)+int(m2)+int(m3)
    avg = round(total/3 , 1)
    percent = (total/30)*100
    if percent >= 80:
        grade = "O"
    elif percent >= 60:
        grade = "A"
    else:
        grade = "P"
    with open("result.txt", 'a') as result:
        result = open("result.txt","a")
        output = rol + " " + str(total) + " " + str(avg) + " " + grade +"\n"
        result.write(output)
f.close()




