'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

eg. 
Search the string to see if it starts with "The" and ends with "Spain":
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


The re module offers a set of functions that allows us to search a string for a match:

Function	       Description
findall     Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
match       Returns a Match object if there is a match from the beginning of the string
split	    Returns a list where the string has been split at each match
sub	    Replaces one or many matches with a string



eg1:-
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)                          ------>   ['ai', 'ai']
​

eg2:-
import re
if re.search(".end","llend"):    	
	print("Matched")              ------>    Matched
else:    
	print("Not matched")


eg3:-
import re
if re.match(".end","llend"):    	
	print("Matched")
else:    
	print("Not matched")          ------>     Not matched


eg4:-
import re
txt = "The rain in Spain"
x = re.split("\s", txt)    # Split the string at every white-space character:
print(x)                          ------->   ['The', 'rain', 'in', 'Spain']

# You can control the number of occurrences by specifying the maxsplit parameter:-
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)   #Split the string at the first white-space character:
print(x)                          ------->   ['The', 'rain in Spain']


eg5:-
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)  #Replace all white-space characters with the digit "9":
print(x)                   ------->    The9rain9in9Spain

You can control the number of replacements by specifying the count parameter:-
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)   #Replace the first two occurrences of a white-space character with the digit 9:
print(x)                   ------->    The9rain9in Spain



                                 Match Object

Note: If there is no match, the value None will be returned, instead of the Match Object.

import re

# A Match Object is an object containing information about the search and the result.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)    #this will print an object     ------>   <_sre.SRE_Match object; span=(5, 7), match='ai'>


# .span() returns a tuple containing the start-, and end positions of the match.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x.span())                ------->    (5, 7)


# .string returns the string passed into the function
txt = "The rain in Spain"
x = re.search(“S\w+", txt)
print(x.string)                ------->    The rain in Spain


# .group() returns the part of the string where there was a match
txt = "The rain in Spain"
x = re.search("p\w+", txt)
print(x.group())               ------->    pain


# re.compile() 
import re
p = re.compile('[a-e]')
print(p.findall("I am from VIT , Chennai"))     ------->    ['a', 'e', 'a']
print(p.findall("I am from VIT , ChEnnAi"))     ------->    ['a']

p = re.compile('\d')   # \d is equivalent to [0-9].
print(p.findall("I came to camput at 08.30 A.M. on 17th November 2021"))   ----->  ['0', '8', '3', '0', '1', '7', '2', '0', '2', '1']

p = re.compile('\d+')  # \d+ will match a group on [0-9], group of one or greater size
print(p.findall("I came to camput at 08.30 A.M. on 17th November 2021"))   ----->  ['08', '30', '17', '2021']

p = re.compile('\w+')
print(p.findall("I came to him at 09.30 A.M., he said &&& is good_girl.")) 
                               ----->          ['I', 'came', 'to', 'him', 'at', '09', '30',
                                                'A', 'M', 'he', 'said', 'is', 'good_girl']

p = re.compile('VIT*')
print(p.findall("VIVITVITTTTVI"))     ------>    ['VI', 'VIT', 'VITTTT', 'VI']




               Metacharacters are characters with a special meaning:

Character	            Description	                           Example	
    []	    A set of characters	                                   "[a-m]"	
    \	    Signals a special sequence     
            (can also be used to escape special characters)	    "\d"	
    .	    Any character (except newline character)	           "he..o"	
    ^	    Starts with	                                           "^hello"	
    $	    Ends with	                                           "planet$"	
    *	    Zero or more occurrences	                           "he.*o"	
    +	    One or more occurrences	                           "he.+o"	
    ?	    Zero or one occurrences	                           "he.?o"	
    {}	    Exactly the specified number of occurrences	           "he{2}o"
    {n,m}   n to m occurances                                      "he{4,7}o
    |	    Either or	                                           "falls|stays"	
    ()	    Capture and group	 


A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	            Description	                                                        Example	
\A	Returns a match if the specified characters are at the beginning of the string          "\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the 
        end of a word                                                                           r"\bain"
        (the "r" in the beginning is making sure that the string is being treated 
        a "raw string")    	                                                                r"ain\b"	
            
\B	 Returns a match where the specified characters are present, but NOT at the beginning 
        (or at the end) of a word                                                               r"\Bain"
        (the "r" in the beginning is making sure that the string is being treated as
        a "raw string")    	                                                                r"ain\B"
            	
\d	Returns a match where the string contains digits (numbers from 0-9)                     "\d"	
\D	Returns a match where the string DOES NOT contain digits	                        "\D"	
\s	Returns a match where the string contains a white space character                       "\s"	
\S      Returns a match where the string DOES NOT contain a white space character	        "\S"	
\w      Returns a match where the string contains any word characters (characters from 
        a to Z,digits from 0-9, and the underscore _ character)                                 "\w"	
\W      Returns a match where the string DOES NOT contain any word characters	                "\W"	
\Z      Returns a match if the specified characters are at the end of the string                "Spain\Z"


A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	                    Description	
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	    In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + 
            character in the string	

        

'''