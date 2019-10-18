#sets in python

#create an empty set
s= set() 
#create a set from a list
list1= [2,3,5,7]
s= set(list1)
print(type(s))

#add a new element in a set
s.add(11)
print(s)
#set returns unique value so we cannot add repeated elements

#for union of sets
s1= s.union({1,2,3})
print(s,s1)

#for intersection of two sets
s1= s.intersection({1,2,3})
print(s,s1)

#print length of set
print(len(s))

#disjoint set
print(s.disjoint(s1))

#to remove an element
s.remove(5)
print(s)
