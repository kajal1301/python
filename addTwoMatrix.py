#program to add two matrices
x= [[2,7,5],[3,7,2],[76,23,12]]
y= [[8,6,4],[43,12,40],[12,34,56]]
result= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]= x[i][j] + y[i][j]

for r in result:
    print(r)        
