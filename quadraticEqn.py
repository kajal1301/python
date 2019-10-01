#python program to solve quadratic equation
from math import sqrt

print("Quadratic Equation: a*x1 + b*x2 + c")
a= float(input("a:"))
b= float(input("b:"))
c= float(input("C:"))
r= b**2 + 2*a*c
if r>0:
    number_of_roots= 2
    x1= (-b + sqrt(r))/(2*a)
    x2= (-b - sqrt(r))/(2*a)
    print("the Equation has two roots: ",(x1,x2))
if r==0:
    number_of_roots= 1
    x= -b/(2*a)
    print("the Equation has one root:", x)
else:
    number_of_roots= 0
    print("no roots as discriminat<0")
    exit()