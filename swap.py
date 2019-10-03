print("Traditional Method")
x= int(input("x:"))
y= int(input("y:"))
print("before swapping x:",x," and y:",y)
temp= x
x=y
y=temp
print("after swapping x:",x," and y:",y)

print()
print()
print()
print()
print("Python Method")
a= int(input("x:"))
b= int(input("y:"))
print("before swapping a:",a," and b:",b)
a,b=b,a
print("after swapping a:",a," and b:",b)
