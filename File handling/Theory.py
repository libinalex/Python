'''
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist
"r+"
"w+"
"a+"

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


To open a file for reading it is enough to specify the name of the file:

Open a File on the Server
Assume we have the following file, located in the same folder as Python:

demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")

print(f.read())

If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt", "r")   # \\ to avoid cases of escape sequence like \n
print(f.read())                            # if don't want to use \\ then use r" " to open as raw file

Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())

By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

readlines(): Reads all the lines and returns them in a list(every line as one element of list)
            # else read() and readline() reads as string

By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

It is a good practice to always close the file when you are done with it.
f = open("demofile.txt", "r")
print(f.readline())
f.close()

Note: You should always close your files, in some cases, due to buffering, 
changes made to a file may not show until you close the file.

.flush() :- explicitly write all the lines above flush even if it is in buffering

# A better way, not needed to close file also:
with open('demofile.txt) as f:
    for line in f:
        print(line)


Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

write() :- writes a string value to a file
writelines() :- writes a list value to the file

Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:


Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


Delete Folder
To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":

import os
os.rmdir("myfolder")

Note: You can only remove empty folders.


tell():-  tells where the file pointer is in the given file
seek(position):-  resets the file pointer to the specified position

Using With Block to open Python File:-          # Works same as:-
with open("Hello.txt") as f:                    f = open("Hello.txt","rt")
  print(f.read())                               print(f.read())
                                                f.close()




'''


'''
# Read Mode:-

file = open("E:\\Python\\Hello.txt",'r')
# for i in file:       # This will print every line one by one in the file
#     print(i)
# print(file.read())
print(file.readlines())


# Write Mode:-

# file1 = open("E:\\Python\\Hello.txt",'w')
# file1.write("Are you attending the class??\n")
# file1.write("I'm not sure what to say. \n")
# file1.close()
# print("Done")


# Append Mode:-

# file2 = open("E:\\Python\\Hello.txt", 'a')	# append mode	
# file2.write("Snacks may be added ")
# file2.close()
'''