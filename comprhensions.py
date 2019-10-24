#Python Comprehensions

l1= []
for i in range(100):
    if i%3==0:
        l1.append(i)

print(l1)

#this can be done in one line using comprehension
l1= [ i for i in range(100) if i%3==0]
print(l1)
# Above was list comprehensions
#-------------dictionary comprehensions---------------
# one way to print dictionary upto 10 items is- {0:"item0", 1:"item1"......upto 100 items}
#using comprehension-
dict1={i: f"item{i}" for item in range(1,100) if i%3==0}
print(dict1)
# to reverse dictionary
dict2={value:key for key,value in dict1.items()}
print(dict2)
#-----------------------set comprehensions-----------
dresses= { dress for dress in ["dress1","dress2","dress1","dress3","dress4","dress1"] }
print(dresses)


#-------------------generator comprehensions---------------
even= (i for i in range(100) if i%2==0)
for items in even:
    print(items)
#or we can print like this:
#print(even.__next__())