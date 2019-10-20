def function_name_print(a,b,c,d):
    print(a,b,c,d)

function_name_print("manu","shalu","name_a","tanu")

def funargs(normal,*args, **kwargs):     #elements wll b store in args as tuple
    print(normal)
    for items in args:
        print(args[i])
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

normal= "This is a normal argument"
lst= ["Maria","larry","Liza","lina"]
kw= {"Rohan": "Cordinator","Sohan":"Fitness Instructor","Carry":"Monitor"}

funargs(normal, *lst, **kw)       #normal argument should b passed first then args and then kwargs otherwize it wll give error





