#python program to solve quadratic equation
from math import sqrt

print("Quadratic Equation: a*x^2 + b*x + c=0")
a= float(input("Coeff. of x^2   a: "))
b= float(input("Coeff. of x     b: "))
c= float(input("constant term   C: "))
r= b**2 - 4*a*c
if r>0:
    number_of_roots= 2
    x1= (-b + sqrt(r))/(2*a)
    x2= (-b - sqrt(r))/(2*a)
    print("the Equation has two roots: ",(x1,x2))
elif r==0:
    number_of_roots= 1
    x= -b/(2*a)
    print("the Equation has repeated root: ", x)
else:
    number_of_roots= 0
    print("no roots as discriminant < 0")
    exit()
