#classes and object:

# classes- Templates
# objcts- Instance of a class

#----------------------class-----------------------------
#creating our first class
class Student:
    pass

mini= Student()
nini= Student()
#print(mini, nini)
mini.name= "Mini"
mini.std= 12
mini.section= 1
nini.std= 9
nini.section= 2
nini.subjects= ["Hindi", "English"]
print(mini.name, nini.subjects)

#-------------------------instances and class variable-----------------------
class Employee:
    no_of_leaves=8
    pass

rohan=Employee()
sohan= Employee()
rohan.name="Rohan"
sohan.name="Sohan"
rohan.salary=455
rohan.role="Instructor"
sohan.salary= 500
sohan.role= "Monitor"
print(rohan.name, sohan.salary)
print(rohan.no_of_leaves)
Employee.no_of_leaves= 9
print(rohan.no_of_leaves)
print(Employee.__dict__)
