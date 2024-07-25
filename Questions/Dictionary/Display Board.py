'''
DisplayBoard
You are going to build a display board to display the words for the given number.

Must use the dictionary concepts.

Example: 
123

Output: 
One Two Three

Example:
9999

Output:
Nine Nine Nine Nine
'''

dict={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
number=input("Enter the number: ")
for i in number:
    print(dict[i], end =" ")