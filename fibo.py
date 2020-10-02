#program to calculate fibonaci sequence using recursion

num= int(input("Enter a number"))
def fib(n):
    return 1 if n<=1 else n*fib(n-1)
def fibonacci(num):
    if(num<=1):
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(num))

