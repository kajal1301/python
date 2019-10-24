#is and == in python
# "==" is value equality- Two objects have the same value
# "is" is refrence equality- Two refrences have the same object

a= [7,4,5]
b=a
print(b==a)    #it returns true/false
print(b is a)
b[0]=0
print(a) 
print(b)