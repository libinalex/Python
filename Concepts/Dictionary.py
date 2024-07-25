'''

Creating and Printing the Dictionary in various ways:-

# initializing dictionary
test_dict = {"CSE" : 1, "IT" : 2, "Mech" : 3}

# Printing dictionary
print ("Dictionary is : " + str(test_dict))            ---->  Dictionary is : {'CSE': 1, 'IT': 2, 'Mech': 3}

# using in operator to get key and value

for i in test_dict :
    print(i, test_dict[i])

CSE 1
IT 2
Mech 3


for key, value in test_dict.items():
    print (key, value)

CSE 1
IT 2
Mech 3



print([(k, test_dict[k]) for k in test_dict])

[('CSE', 1), ('IT', 2), ('Mech', 3)]


sample = dict(name='Prakash', age='40')

print(sample)
{'age': '40', 'name': 'Prakash'}


sample2 = dict([('name','Prakash'), ('age',40)])

print(sample2)
{'age': 40, 'name': 'Prakash'}


for item in marks.items():
print(item)

('Math', 0)
('English', 0)
('Science', 0)



D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

{'a': 1, 'b': 2, 'c': 3}


D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

{1: 1, 2: 4, 3: 9, 4: 16}


D = {c: c * 4 for c in 'VIT'}
print(D)

{'V': 'VVVV', 'I': 'IIII', 'T': 'TTTT'}


D = {c.lower(): c + '!' for c in ['MSD', 'CSK', 'Neeraj']}
print(D)

{'msd': 'MSD!', 'csk': 'CSK!', 'neeraj': 'Neeraj!'}


print(f'zebras: {hash("zebras")}')
print(f'lions: {hash("lions")}')
print(f'birds: {hash("birds")}')

zebras: 3923224834497940240
lions: -8300711012095782792
birds: 7210607209619514265









Method      	Description
clear()	    Removes all the elements from the dictionary
copy()  	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()   	Removes (and Retrives the value) the element with the specified key
popitem()	Removes (and retrives the key-value pair) the last inserted key-value pair
setdefault()	Returns the value of the specified key. 
                If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


Functions in Dictionary:-

Dictionary = { 'A': 'CSE', 'B': 2021, 'C': 'BigData' }
 
print(Dictionary.items())    ---------->   dict_items([('A', 'CSE'), ('B', 2021), ('C', 'BigData')])

print(Dictionary.values())   ---------->   dict_values(['CSE',2021,'BigData'])

print(Dictionary.keys())     ---------->   dict_keys(['A','B','C'])

print(Dictionary.get('C'))      --------->   BigData

print(Dictionary.get('E'))      --------->   None

print(Dictionary['E'])         ---------->  !!! <Key Error> !!!



keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys)
print(vowels)                ------>   {'e': None, 'a': None, 'i': None, 'u': None, 'o': None}


value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)                ------->   {'e': [1], 'a': [1], 'i': [1], 'u': [1], 'o': [1]}

# updating the value
value.append(2)
print(vowels)    ------>   {'e': [1, 2], 'a': [1, 2], 'i': [1, 2], 'u': [1, 2], 'o': [1, 2]}

keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]
vowels = { key : list(value) for key in keys }
print(vowels)         -------->     {'e': [1], 'a': [1], 'i': [1], 'u': [1], 'o': [1]}

# Does not Update  ???
value.append(2)
print(vowels)         -------->     {'e': [1], 'a': [1], 'i': [1], 'u': [1], 'o': [1]} 



marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)                          --------------->    {'Math': 0, 'English': 0, 'Science': 0}

print(list(sorted(marks.keys())))  -------->   ['English', 'Math', 'Science']





squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))      --------->   16     

# remove an arbitrary item, return (key,value)
print(squares.popitem())     --------->  (5, 25)

del squares[1]
print(squares)          --------->    {2: 4, 3: 9}

# remove all items
squares.clear()
print(squares)         --------->   {}

# delete the dictionary itself
del squares
print(squares)         --------->   !!! <Error> !!!


'''