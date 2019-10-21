#self and init constructors
class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):
        self.name= aname
        self.salary= asalary
        self.role= arole


    def print_details(self):
        return f"Name is: {self.name}. salary is {self.salary}. and role is {self.role}"

    

rohan= Employee("Rohan", 455, "Instructor")
rohan.name="Rohan"
rohan.salary=455
rohan.role="Instructor"

sohan= Employee("Sohan", 500,"Monitors")
sohan.name="Sohan"
sohan.salary= 500
sohan.role= "Monitor"

print(rohan.print_details())
print(rohan.Employee)