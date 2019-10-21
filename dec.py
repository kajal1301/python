#decorators in python: those who modify the functionality of a function

def function1():
    print("HEllo Everyone")

func2= function1
del function1   #we delete the function1 here
func2   #if function1 is deleted then also function one will print as we have created a copy of it

def funcret(num):
    if num==0:
        return print
    if num==1:
        return int

a= funcret(1)
print(a)
#we can also return a function as an argument
def executor(func):
    func("This")
executor(print)
#use of decorators:
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_am_i():
    print("Who am I")

# who_am_i = dec1(who_am_i)

who_am_i()

