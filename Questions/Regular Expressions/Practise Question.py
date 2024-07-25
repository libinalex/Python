'''
Assume that you are writing a python program that should verify an official document’s doc_id, 
you are asked to create a regex patent to check the doc_id’s validity by 
satisfying all the below conditions, if not, print ‘invalid’.

The doc_id has the fixed length of 17 digits and the format is listed as follows:
The first five digits of doc_id  represent either any uppercase alphabets 
or numerical value 9 (Digit 1-5: Letters A-Z or 9's)
The next six digits of doc_id  represent any numerical values between 0 and 9 (Digit 6-11: Numbers 0-9)
The next two digits of doc_id  represent either any uppercase alphabets between A and D 
or numerical value from 1 to 3 (Digit 12-13: Letters A-D or 1-3)
The next digit of doc_id  represent any numerical value (Digit 14: Number 0-9)
The next digit of doc_id  represent any of the following 
special characters @#$&* (Digit 15: special character @#$&* )
The last two digits of doc_id  represent any uppercase or lowercase alphabets 
(Digit 16-17: Two letters A-Z or a-z)

A 17-digit ‘valid’ doc_id will have all its digits in the same order as listed above, 
otherwise display an ‘invalid’ message.

[Note: You are allowed to use only “RegEx” related syntax to solve this problem]

 

Input Format:

#In a single line, read a doc_id as a string

Output Format:

#Print whether it is valid or invalid.

Sample Test Case Input-1
ABC99123456C24@Qq

Sample Test Case Expected Output-1
valid



Sample Test Case Input-2
aABC9678943446*Wf 

Sample Test Case Expected Output-2
invalid
'''
