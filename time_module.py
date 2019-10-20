#time module in python
import time

#to check which of the two loops run faster
initial= time.time()
k=0
while(k<45):
    print("This is while loop")
    time.sleep(2)       #this stops the loop for 2 seconds. hence it wll continue the loop after 2 seconds everytime
    k= k+1
print("While loop ran in", time.time()-initial,"seconds")
initial2= time.time()
for i in range(45):
    print("This is for loop")

print("For loop ran in", time.time()-initial2,"seconds")

#to get the exact time right now
localtime= time.asctime(time.localtime(time.time()))
print(localtime)