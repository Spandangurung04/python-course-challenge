# file handling
f = open('demofile.txt','rt')
print(f.read())
f.close()

# reading a file using with statement
with open('demofile.txt','rt')as f:
    a = f.read()
    print(a)

# read characters of line
f = open('demofile.txt','rt')
print(f.read(5))
f.close()


#read line by line
f = open('demofile.txt','rt')
print(f.readline())
print(f.readline())

#write in file
f = open('demofile2.txt')
#writing a file
f = open('demofile2.txt','w')
f.write('we are learning file handling')
f.close()

#append in a file
f = open('demofile2.txt','a')
f.write('\n i am appending in a file')
f.close()

#deleting a file
import os
os.remove('demofile3.txt')