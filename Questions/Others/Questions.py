a = [1, 2, 3, 4, 5, 8]
b = [2, 4, 6, 8, 3]
c = [1, 3, 5, 7, 4, 3, 2]
'''
Task is to create a list d whose elements will be the sum of elements iat the index of a, b, c
'''

#1 - 
d = []
n = min(len(a), len(b), len(c))
for i in range(n):
    d.append(a[i] + b[i] + c[i])
    
print(d)


#2
def summation(x,y,z):
    return x+y+z

l = list(map(summation, a,b,c))
print(l)


#3
l = list(map(lambda x,y,z: x+y+z, a,b,c))
print(l)