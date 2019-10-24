#setter and property decorators
class Employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname
        #self.email= f"{fname}.{lname}@kmail.com"

    def explain(self):
        return f"This employee if {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@kmail.com"

    
    @email.setter
    def email(self, string):
        print("Setting now..")
        names= string.split("@")[0]
        self.fname= names.split(".")[0]
        self.lname= names.split(".")[0] 

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

emp1= Employee("Raj","Malhotra")
emp2= Employee("Simran","Pandey")
print(emp1.email)

emp1.fname= "Rahul"
print(emp1.email)   #it wll not change 
#it will change with the help of setter

#if we use property decortor before email function then we can change the email without calling the function
emp1.email= "this.that@gmail.com"
print(emp1.email)
del emp1.email
print(emp1.email)
