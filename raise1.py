#raise in python
a= input("Enter you name")
if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"HEllo {a}")
#zero division error
b= input("Enter a number")
if int(b)==0:
    raise ZeroDivisionError("B is zero so program is stopped")
c= input("Enter your name")
try:
    print(a)
except Exception as e:
    if c=="Abcd":
        raise ValueError("This name is blocked, try another")
    print("Exception Handled")