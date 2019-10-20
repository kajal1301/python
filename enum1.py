#enumerate function
l1= ["tamato","noodels","egg","mushroom"]
i=1
for item in l1:
    if i%2 !=0:
        print(f"Pleasy buy {item}")
        i+=1
print()

#this function can be written using enumerwated function
for index, item in enumerate(l1):
    if index%2==0:
         print(f"Pleasy buy {item}")
       