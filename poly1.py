#polymorphism: 
print(5+6)
print("5"+"6")

#------------overriding methods------------------
class A:
    classvar1= "I am a variable in class A"
    def __init__(self):
        self.var1="I am inside class A constructor"
        self.classvar1="Instance var in constructor A"
        self.special= "special"

class B(A):
    classvar1= "I am in class B"
    def __init__(self):
        self.var1= "I am inside class B constructor"
        self.classvar1= "Instance var in class B"
        super().__init__()
        print(super().classvar1)

a= A()
b= B()
print(b.special, b.var1, b.classvar1)