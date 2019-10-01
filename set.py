#set
x= {"set","tuple","lists"}
#to add items
x.add("dictionaries")
print(x)
# to update set
x.update(["apple","mango","banana"])
print(x)

#to print length of set
print(len(x))

#to remove an item from set
x.remove("banana")
print(x)

#to empty the set
x.clear()
print(x)
x= {"set","tuple","lists"}
#to delete the set completely
del x



#join two sets
x1= {"a","b","c"}
x2= {1,2,3}
x3= x1.union(x2)
print(x3)
#update the set
x1.update(x2)
print(x1)
