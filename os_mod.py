# os module
#os is operating system and python has a buildin module 
import os
print(dir(os))
#this tells what can we do with os module
print(os.getcwd)
#this tells about the current working directory. current working directly means the folder we are working with. 
# but is can not always be the same. we can change the current working directory also.
os.chdir("D://")
#by this we can change our current working directory
print(os.getcwd)
#f= open(hello.txt)
#this line wll give error as this file is not in the changed current working directory
print(os.listdir())
#os.listdir() will gives the names of all the files and folders in our current working directory
#we can also see all the contect of any other directory -
print(os.listdir("D://"))
#this will list all the contents of stated directory
os.mkdir("This")
#os.mkdir will create a new folder of name "This" in the current directory
os.makedirs("Hello/Heyy")
#this will make a folder named hello and inside hello it will make a folder named heyy in our current directory
os.rename("hello.txt","rename.txt")
#this will rename the name of  file from hello.txt to rename.txt
print(os.environ.get('Path'))
#this will print the environment variable of the path which is set
print(os.path.join("c://","hello.txt")
#this joins the path of these two files
print(os.path.exists("C://Program Files//UNP"))
print(os.path.exists("C://Program Files//ABC"))

#this function tells whether the given path exists or not. if exists then it returns true otherwise false
print(os.path.isdir("C://Program Files//UNP"))
#if there is a directory of such path then it will return true
print(os.path.isfile("C://Program Files//UNP"))
#is there is a directory of such path then it will return true

