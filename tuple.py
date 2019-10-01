tuple1=('kajal', 'mishra')
print(tuple1)
#to print a first item of tuple
print(tuple1[1])
#to print last item of tuple
print(tuple1[-1])

tuple1= ('list','set','dictionary','tuple','strings','variables','operators')
print(tuple1[2:4])

#convert tuple into list
x= ('apple','mango','banana')
y= list(x)
y[1]= "pineapple"
x= tuple(y)
print(x)

#check if item exists
if "set" in tuple1:
    print("yes it exists")

#tuple length
print(len(tuple1))
print(len(x))

#tuples are unchangable. we cannot add or remove items from tuple

#join two tuples
tuple2= tuple1+ x
print(tuple2)

