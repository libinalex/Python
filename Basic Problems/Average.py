# Program to calculate the average of numbers:
n = int(input("Enter the no. of terms: "))
sum = 0
for i in range(n):
    num = int(input("Enter the number: "))
    sum = sum + num
avg = sum / n
print("The average of given numbers is:", avg)
