#Functions and docstrings in python


#user defined function
def function1(a,b):
    print("Hello")
    print(a+b)
def function2(a,b):
    """This is a function"""
    avg= (a+b)/2
    print(avg)
    return avg

print(function1(4,3))
print(function2(4,3))
print(function2._doc_)  #function to print doc string