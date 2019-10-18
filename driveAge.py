#to check whether a person has permission of driving a car or not

age= int(input("Enter Your Age:-"))
if age< 18:
    print("You are not eligible for driving a car")
elif age>18:
    print("Congrats!!! You are eligible to drive a car")
else:
    print("Your age is just 18, So we cant decide...")