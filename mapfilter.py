#map , filter and reduce in python
from functools import reduce 
#-----------------map function-----------------------------
numbers= ["3","72","5","1","15","64"]
#for i in range(len(numbers):
#    numbers[i] = int(numbers[i])

#numbers[2]= numbers[2]+1
#print(numbers[2]) 

#this can be done in one line using map filter
numbers= list(map(int, numbers))
num= [2,3,4,1,5,2,6]
square= list(map(lambda x: x*x, num))
print(square)

def square(a):
    return a*a
def cube(a):
    return a*a*a

func= [square, cube]
#num= [2,3,4,1,5,2,6]
for i in range(5):
    val= list(map(lambda x: x(i), func))
    print(val)
#---------------------------------------filter--------------------------------------------------------#
#filter function: It filters the progams i.e. it make a list which returns the given function true
list_1= [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
greater_than_5= list(filter(is_greater_5,list_1))
print(greater_than_5)

#-------------------------------------reduce--------------------------------------------------------
l1= [1,2,3,4]
num=0
for i in l1:
    num= num+i
print(num)
#this can be done in one line
num= reduce(lambda x,y:x+y, l1)
print(num)