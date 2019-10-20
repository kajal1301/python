#recursion in python

num1= int(input("Enter a number: "))
#factorial using iterative method
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac= fac*(i+1)
    return fac

#factorial using recursive method
def factorial_rec(n):
    fac= n
    if n==1:
        return 1
    else:
        return n*factorial_rec(n-1)

print("Factorial using iterative method:", factorial_iterative(num1))
print("Factorial using recursive method:", factorial_rec(num1))

