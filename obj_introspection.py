#object Introspection in python:- this means to know something about any object

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
skillf= Employee("skill","F")
print(skillf.email)
print(type(skillf))     #it returns the type of skillf
print(id("This is a string"))    #this will return id
#dir- it shows all the methods that can be defined in a string
o= "This is a string"
print(dir(o))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
