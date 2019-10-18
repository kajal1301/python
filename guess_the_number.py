
n= 18
j=0
while j<=5 :
    i= int(input("Guess a Number"))
    if i> n:
        print("Your number is greater")
    elif i<n:
        print("Your number is Smaller")
    else:
        print("Your Guess is Correct")  
        break
    j=j+1
print("Game Over")