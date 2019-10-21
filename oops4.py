#Inheritance in python

class Employee:
    no_of_leaves = 8
    var=8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)
#single inheritance
class Programmer(Employee):
    def __init__(self, aname, asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages= languages
        
        
    def printprog(self):
        return f"The Programmer's name is {self.name}. salary is {self.salary}, and role is {self.role}. The laanguages are {self.languages}"


sohan = Employee("Sohan", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
shubham= Programmer("Shubham",1000,"Programmer",["python"])
karan= Programmer("Karan",1200,"Programmer",["python", "cpp"])
print(karan.printdetails())
print(shubham.printprog())

#multilevel inheritance
class Players:
    no_of_games= 4
    var=9
    def __init__(self, name,game):
        self.name= name
        self.game= game
    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}"
class Coolprogrammer(Employee, Players):
    var=10
    language= "C++"
    def printLanguage(self):
        print(self.language)

player1= Players("Player1", ["cricket"])
player2= Coolprogrammer("Player1", 1400, "coolProgrammer")
det = player2.printdetails()
print(det)
player2.printLanguage()
print(karan.var)