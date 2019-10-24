# else and finally in try and except

try:
    f=open("hello.txt")
except EOFError as e:
    print(e)
except IOError as i:
    print(i)
    

else:
    print("this will run only when except will not run")
finally:                    #it is used for code cleanup. wheather try block runs or not, finally will run in all cases
    print("Run this anyway")
    f.close
print("Important stuff")

#if except block runs then else block will not run. else will run only when except will not run
#we can write more than one except in one program