'''
PasswordChecker
You joined a social networking site to stay in touch with your friends.
The signup page required you to input a name and a password. However, the password must be strong.
The website considers a password to be strong if it satisfies the following criteria:

Its length is at least 5.
It contains at least one digit.
It contains at least one lowercase English character or one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+

Your Program should find whether the password is STRONG or NOT

Input - password
Output - Strong or Not Strong

Input: // Passw0rd String
praN12$

Output :
Strong


Input :
p123

Output:
Not Strong
'''



pas=input("Enter the Password: ")
sp_chr="!@#$%^&*()-+"
temp=0
if len(pas)<5:
    status="Not Strong"
else:
    for i in pas:
        if i.isdigit():
            temp=1
        if temp==1:
            for i in pas:
                if i.isalpha():
                    temp=2
        if temp==2:
            for i in pas:
                if i in sp_chr:
                    status="Strong"
                    break
        else:
            status="Not Strong"
print(status)