#program to calculate fibonaci sequence using recursion

num= int(input("Enter a number"))

def fibonacci(num):
    if(num<=1):
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(num))

