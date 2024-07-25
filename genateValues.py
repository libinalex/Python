'''

# generate random positive numbers
import random
n = 5000
with open("random_" + str(n) + ".txt","w") as fp:
	fp.write(str(n)+"\n")  
	for i in range(1,n):
	    x = random.random()
	    fp.write(str(int(x*n))+"\n")  
	x = random.random()
	fp.write(str(int(x*n))+"\n")  
fp.close()



# generate random alphabets
import random
import string
n = 500
with open("random_letter" + str(n) + ".txt","w") as fp:
    fp.write(str(n)+" ")
    for i in range(1, n):
        x = random.choice(string.ascii_lowercase) # choose a random lowercase letter
        fp.write(x + " ")
    x = random.choice(string.ascii_lowercase)
    fp.write(x)
fp.close()




# generate random positive and negative numbers
import random
n = 10
with open("random_pos_neg" + str(n) + ".txt","w") as fp:
    fp.write(str(n)+" ")  
    for i in range(1, n):
        x = random.randint(-100,100)
        fp.write(str(int(x))+" ")  
    x = random.randint(-100,100)
    fp.write(str(int(x))+" ")  
fp.close()




#generate random coordinates
import random
n = 5000
with open("random_coordinates" + str(n) + ".txt","w") as fp:
    fp.write(str(n)+"\n")
    for i in range(n):
        x = round(random.uniform(-50, 50), 2)
        y = round(random.uniform(-50, 50), 2)
        fp.write(str(x) + " " + str(y) + "\n")
fp.close()




#generate random activity starting and ending time
import random
n = 1000
fp = open("randomact_"+str(n)+".txt","w")
fp.write(str(n)+" "+'\n')  
for i in range(1,n+1):
    x = random.uniform(0,0.5)
    y=random.uniform(0.5,1)
    fp.write('a'+str(i)+" "+str(int(x*n))+" "+ str(int(y*n))+'\n') 
fp.close()




#generate random strings
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

    


    
# Generate two random strings
random_str1 = generate_random_string(10)
random_str2 = generate_random_string(15)

# Write the random strings to the same file, separated by a newline character
with open("random_strings.txt", "w") as file:
    file.write(random_str1 + "\n" + random_str2)
'''