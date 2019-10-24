#using else with for loops
foods= ["Noodles","pasta","rice","mushroom"]
for item in foods:
    print(item)
    if(item=="paratha"):
        break
    
    #if(item=="rice"):
    #    break                  this will not print else statement
else:
    print("this loop ended properly")