# File I/O Basics
"""
"r"= open file for reading
""
 """
#file read
f= open("hello.txt","r")
content= f.read()   #for reading in a  file
f.close()

f= open("hello.txt","r")
print(f.readlines())    #it will print all lines of file in a list
print(f.readline()) #readline
content= f.read()   #for reading in a  file
#for reading line by line
for line in content:
    print(line,end=" ")


f.close()

#file writing
f= open("hello2.txt","w")   #this will create a new file
f.write("This is example of writing in a file") #this will replace all teh contents of file and write this line
f.close()

#file appending

f= open("hello.txt","a")   
f.write("This is example of writing in a file") #this will add this line in the file
f.close()

#handle read and write both
f= open("hello2.txt","r+")  #this will read and write both in the file
print(f.read())
f.write("Thank You")
print(f.read())
f.close

#tell() function and seek() function
f= open("hello.txt")
print(f.tell()) #tell functn tells about where the location of file pointer is
print(f.readline())
f.seek(10)      #it resides the file pointer to the given location
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

#using with block
#we dont need to close the file now. 
with open("hello.txt") as f:
    a= f.read(4)
    print(a)
