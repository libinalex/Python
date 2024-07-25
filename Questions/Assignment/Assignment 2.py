"""
1. 
Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', 'L', ' D']
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

a = [i for i in "ACADGILD"]
b = [x*i for x in "xyz" for i in [1,2,3,4]]
c = [i*j for i in [1,2,3,4] for j in "xyz"]
d = [[i] for i in [2,3,4,3,4,5,4,5,6]]
e = [[i, i+1, i+2, i+3] for i in [2,3,4,5]]
f = [(i,j) for j in [1,2,3] for i in [1,2,3]]
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
"""


"""2.
Implement a function longestWord() that takes a list of words and returns the longest one.

def longestWord(lst):
    max = lst[0]
    for word in lst:
        if(len(word)>len(max)):
            max = word
    return max

lst = ["hello", "libin Alex", "sifh", "skhfudsh", "Hello world"]
print("The longest word in the given list of words is:", longestWord(lst))
"""


"""3
Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.

class Triangle:
    def set_length(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Area(Triangle):
    def calculate_area(self):
        self.s = (self.a+self.b+self.c)/2
        return (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5

t1 = Area()
t1.set_length(3,4,5)
area = t1.calculate_area()
print("The area of the given triangle is:", area)
"""


"""4
Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.

def filter_long_words(l, n):
    return list(filter(lambda x:len(x)>n , l))

l = ["Hii", "Libin", "Elephant", "Ravi Raahul", "Anandakrishnan"]
n = 5
filtered_words = filter_long_words(l, n)
print(filtered_words)
"""


"""5
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words .
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.

def lengths(l):
    return list(map(lambda x:len(x), l))

l = ["ab", "cde", "qwerty", "asdf"]
length = lengths(l)
print(length)
"""


"""6
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
a vowel, False otherwise.

def checkVovel(ch):
    if(ch.lower() in ["a", "e", "i", "o", "u"]):
        return True
    return False
    
print(checkVovel("a"))
print(checkVovel("z"))
print(checkVovel("C"))
print(checkVovel("E"))
print(checkVovel("q"))
print(checkVovel("u"))
"""