'''
Python has a set of built-in methods that you can use on lists/arrays.
 
ind --> index   obj --> object

   Method	               Description

list.append(obj)	  Adds an element at the end of the list (in place)
list.clear() 	     Removes all the elements from the list (in place)
list.copy()	        Returns a copy of the list
list.count(obj)     Returns the number of elements with the specified value(frequency of obj)
list.extend([obj])  Adds multiple elements of a list (or any iterable) to the end of the list (in place)
list.index(obj) 	  Returns the index of the first element with the specified value
list.insert(ind,obj)	 Adds an element at the specified position (in place)
list.pop(ind)	    Retrives and Removes the element at the specified position (in place)
list.remove(obj) 	 Removes the first item with the specified value (in place)
list.reverse()  	 Reverses the order of the list (in place)
list.sort()        Sorts the list in ascending order. (in place)
 
list.sort(reverse=True, key=int/len/str.lower)      Sorts the list in descending order,
                                                    sort string acc to int/length/lowercase string...


type(list): It returns the class type of an object.
max(list):  It returns an item from the list with a max value.
min(list):  It returns an item from the list with a min value.
len(list):  It gives the overall length of the list.
sum(list):  It gives the sum of all the numbers in the list.


sorted (list , reverse=True):      It sorts the list in descending order(not permanent change in original list)
max/min (list , key=len/int...):   To find maximum/minimum from string list.
sum (list,10):    Adds 10 to the sum of all numbers in the list


If s is a list then the following operations will have the corresponding results:

Operation     Result

s[i] = x        item i of s is replaced by x
s[i:j] = t      slice of s from i to j is replaced by the contents of the iterable t
del s[i:j]      same as s[i:j] = []
s[i:j:k] = t    the elements of s[i:j:k] are replaced by those of t
del s[i:j:k]    removes the elements of s[i:j:k] from the list
del s           deletes the entire list
s.append(x)     appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
s.clear()       removes all items from s (same as del s[:])
s.copy()        creates a shallow copy of s (same as s[:])
s.extend(t)     extends s with the contents of t                            
or s += t       (for the most part the same as s[len(s):len(s)] = t)
s *= n          updates s with its contents repeated n times
s.insert(i, x)  inserts x into s at the index given by i (same as s[i:i] = [x])
s.pop() or s.pop(i)     retrieves the item at i and also removes it from s
s.remove(x)     remove the first item from s where s[i] is equal to x
s.reverse()     reverses the items of s in place



# To convert string to list use split function:

line = 'VIT IIT SSN Amrita'
university=line.split()
print(university)                   = ['VIT', 'IIT', 'SSN', 'Amrita']

line = 'VIT,IIT,SSN,Amrita'
university=line.split(',')
print(university)                   = ['VIT', 'IIT', 'SSN', 'Amrita']


# To convert list to string use join function:

s=['s', 'p', 'a', 'x', 'x', 'y']
new_str = "".join(s)
print(new_str)                            =  'spaxxy'


print(' '.join(['IIT','ANNA','SSN']))     =  'IIT ANNA SSN'



# To create a integer list using string input numbers

a=[int(x) for x in input().split()]  
a=list(map(int,input().split()))
 

# To create list:

a=[2,4,'fg']
a=[x for x in "libin"]
a=list(range(2,14,3)) or [x for x in range(2,14,3)]
a=[x**2 for x in range(1,11)]






'''