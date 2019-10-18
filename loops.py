#for loop
list1= ["One","Two", "Three","Four"]
tp= ("One","Two", "Three","Four")
list2= [["Anu",1],["Payal",4],["Bill"],5]
dict1= dict(list2)

#for loop for list:
for item in list1:
    print(item)
for item,number in list2:
    print(item, number)

#for loop for tuple:
for item in tp:
    print(item)

#for loop for dictionary:
for item in dict1:
    print(item) #prints only key elements

#while loop

i=0
while i<45:
    print(i)
    i= i+1