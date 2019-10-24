# Generators in python
#----------Iterable------ __iter__() / __getitem__()---------------
#----------Iterator------ __next__()-------------------------------
#----------Iteration- process of Iterate is Iteration
#Generators are the Iterators tht can be traversed only once\

# For Example- range() is a Generator
#for i in range(1000):
#    print(i)

def gen(n):
    for i in range(n):
        yield i #it generates value on the fly

g= gen(345422682)
print(g)

#---- Iterators
h= gen(3)
h.__next__()
print(h)
h.__next__()
print(h)
h.__next__()
print(h)
#h.__next__()
#print(h)
#this will not print 4 times as range is till 3

#--------Iterables----
i= "Isha"
for j in i:
    print(i)
    #one more way to print-
#print(iter(i))      #it gives string iterator
ier= iter(i)

print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
#it wll not print integrs