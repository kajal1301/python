#program to multiply two matrices
x= [[2,3,4],[3,4,5],[4,5,6]]
y= [[9,8,7],[8,7,6],[6,5,4]]
result= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
       for k in range(len(x)):
           result[i][j] += x[i][k] * y[k][i]

for r in result:
    print(r)  



