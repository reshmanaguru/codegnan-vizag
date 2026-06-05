Inheritance
-----------
--> The inheritance allows one class to aquire the properrties and methods of another class

Types
------
1.Single Inheritance
2.Multiple Inheritance
3.Multi-level Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance

1)Single Inheritance
--------------------
-->A child class inherits from a single parent class

class father:
    def Land(self):
        print("My father  has 5A")
class Reshma (father):
    def my_own(self):
        print('i have 2 A')
fam = Reshma()
fam.Land()
  
2)Multiple Inheritance
----------------------
-->child class inherit from more than one class

class father:
    def Land(self):
        print("My father has 5 A")
class mother:
    def gold(self):
        print("My mother have 1kg gold")
class reshma(father,mother):
    def mine(self):
        print("i have nothing")
fam = reshma()
fam.Land()
fam.gold()

3)Multi-level inheritance
-------------------------
-->Inheriting from a child class of a parent class to acquire the properties and methods of another class

class grandfather:
    def land(self):
        print("grandfather has 5A of land")
class father(grandfather):
    def flat(self):
        print("Have flat at BNG")
class son(father):
    def Ntg(self):
        print("I own both of their p")
fam = son()
fam.land()
fam.flat()
fam.Ntg()

4)Hierarchical Inheritance
--------------------------
-->multiple child classses inherit from a single parent class
eg



class father:
    def land(self):
        print("10 A land")
class reshma(father):
    def mine(self):
        print("job")
class sister(father):
    def sis(self):
        print("jobless")
fam = reshma()
s = sister()
fam.land()
s.land()

5)Hybrid inheritance
--> This is the combination of two or more types of inheritance

class A:
    def some(self):
        print('Class A')
class B(A):
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')
class D(B,C):
    def All(self):
        print('Class D')
alpha = D()
alpha.some()
alpha.any()
alpha.so()
alpha.All()

Super() method
--------------
--> Super() is used to access methods and constructor od the parent class from the child class

class parent:
    def display(self):
        print('Method parent')
class child(parent):
    def display(self):
        super().display()
        print('method child')
any = child()
any.display()


class person:
    def __init__(self,name):
        self.name = name
class stu(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll}")
any = stu('Reshma',50)
any.show()

























































