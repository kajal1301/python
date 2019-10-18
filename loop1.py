#make a list and print only numbers>6

list1= ["Hello","python","55,3,4,1,76,9,8,6]

for item in list1:
    if str.isnumeric() and item> 6:
        print(item)