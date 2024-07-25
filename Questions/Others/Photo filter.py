'''
VTopPhoto
You want to change your profile picture on VTop which has some restrictions over the dimension of the
 picture that you can upload. You need to select the appropriate photo using Python programming.

The minimum dimension of the picture can be L x L, where L is the length of the side of the square.

Now you have N photos of various dimensions.
Dimension of a photo is denoted as W x H
where W - width of the photo and H - Height of the photo

When any photo is uploaded following events may occur:

[1] If any of the width or height is less than L, the user is prompted to upload another one. 
        Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
    (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
    (b) else the user is prompted to crop it. Print "CROP IT" in this case.

Given L, N, W, and H as input, print appropriate text as output.

Input:
#First-line contains L.
#Second-line contains N, the number of photos.
#The following lines(N) have the dimensions of each image

180
5
640 480
120 300
180 180
400 400
200 180
##HINT: use input().split() to get the numbers from each line

var1,var2=input('').split() # This line will take the input 640 480 and assign var1=640 and var2=480

Output: #Print appropriate text for each photo in a new line.

CROP IT
UPLOAD ANOTHER
ACCEPTED
ACCEPTED
CROP IT'''

len=int(input("Enter minimum lenght of side: "))
num=int(input("Enter the number of available photos: "))
for i in range(num):
    width,height=input("Enter the dimensions(width height) of the photo: ").split()    
    if int(width)<len or int(height)<len:
        print("UPLOAD ANOTHER")
    elif width==height:
        print("ACCEPTED")
    else:
        print("CROP IT")