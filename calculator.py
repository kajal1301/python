def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def squareTheNumber(x,y):
   return x*x + 2*x*y +y*y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square sum of numbers")


choice = input("Enter choice(1/2/3/4/5): ")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))	
if choice == '1':
   print(x,"+",y,"=", add(x,y))
elif choice == '2':
   print(x,"-",y,"=", subtract(x,y))
elif choice == '3':
   print(x,"*",y,"=", multiply(x,y))
elif choice == '4':
   print(x,"/",y,"=", divide(x,y))
elif choice == '5':
   print("square of the sum of numbers is =", squareTheNumber(x,y))
else:
   print("Invalid input")
