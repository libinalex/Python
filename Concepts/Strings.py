'''
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.


str.capitalize()	Converts the first character to upper case
str.casefold()    	Converts string into lower case
str.center()    Returns a centered string
str.count()	    Returns the number of times a specified value occurs in a string
str.encode()    Returns an encoded version of the string
str.endswith()	    Returns true if the string ends with the specified value
str.expandtabs()	Sets the tab size of the string
str.find()      	Searches the string for a specified value and returns the position of where it was found
str.format()    	Formats specified values in a string
str.format_map()	Formats specified values in a string
str.index()	        Searches the string for a specified value and returns the position of where it was found
str.isalnum()	 Returns True if all characters in the string are alphanumeric
str.isalpha()	 Returns True if all characters in the string are in the alphabet
str.isascii()	 Returns True if all characters in the string are ascii characters
str.isdecimal()	 Returns True if all characters in the string are decimals
str.isdigit()	    Returns True if all characters in the string are digits
str.isidentifier()	Returns True if the string is an identifier
str.islower()	    Returns True if all characters in the string are lower case
str.isnumeric()	    Returns True if all characters in the string are numeric
str.isprintable()	Returns True if all characters in the string are printable
str.isspace()	Returns True if all characters in the string are whitespaces
str.istitle()	Returns True if the string follows the rules of a title
str.isupper()	Returns True if all characters in the string are upper case
str.join()	    Converts the elements of an iterable into a string
str.ljust()	    Returns a left justified version of the string
str.lower()	    Converts a string into lower case
str.lstrip()	Returns a left trim version of the string
str.maketrans()	Returns a translation table to be used in translations
str.partition()	Returns a tuple where the string is parted into three parts
str.replace()	Returns a string where a specified value is replaced with a specified value
str.rfind() 	Searches the string for a specified value and returns the last position of where it was found
str.rindex()	Searches the string for a specified value and returns the last position of where it was found
str.rjust()	    Returns a right justified version of the string
str.rpartition()	Returns a tuple where the string is parted into three parts
str.rsplit()	Splits the string at the specified separator, and returns a list
str.rstrip()	Returns a right trim version of the string
str.split() 	Splits the string at the specified separator, and returns a list
str.splitlines()	Splits the string at line breaks and returns a list
str.startswith()	Returns true if the string starts with the specified value
str.strip()	    Returns a trimmed version of the string
str.swapcase()	Swaps cases, lower case becomes upper case and vice versa
str.title()	    Converts the first character of each word to upper case
str.translate()	Returns a translated string
str.upper()	    Converts a string into upper case
str.zfill()	    Fills the string with a specified number of 0 values at the beginning
'''

str = "Hello! My name is Libin Alex" 
a = 9

print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.split())
print(str.split('e'))
print(str.partition('Alex'))    #separator is mandatory and it will be a part of the 3 parts of the tuple
print(str.find('in'))
print(str.center(40, '*'))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print('My name is {}. I am {} years old.'.format(name, age))
print("My name is %s and I am %d years old." %(name, age))

print()

s = "HelloWorld"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.istitle())
print(s.endswith('rld'))

print(len(s))
