'''
A basic code for matrix input from user


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
for i in range(R): # A for loop for row entries
    a =[]
    for j in range(C): # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
print()


Enter the number of rows:2
Enter the number of columns:3
Enter the entries rowwise:
1
2
3
4
5
6
1 2 3 
4 5 6 
print(matrix[i][j], end = " ")
print()




# Program to add two matrices using nested loop
X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]
Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

     
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
# iterate through rows
for i in range(len(X)):
# iterate through columns
for j in range(len(X[0])):
result[i][j] = X[i][j] + Y[i][j]
for r in result:
print(r)

[17, 15, 4]
[10, 12, 9]
[11, 13, 18]
 '''