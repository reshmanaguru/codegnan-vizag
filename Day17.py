OOPS
------
1) class
---------
--> It is a blueprint or a template used to create object

class stu :
    name = "Reshma"

s1 = stu()
print(s1.name)

------------------------------------------------------------

class stu:
    def edu(self):
        print("I am studing B.Tech")
    def sports(self):
        print("cricket")
        print("Vall")
s1 = stu()
s1.sports()

------------------------------------------------------------
2) object
---------
--> An object is an instance of a class

eg
---
class stu():
    name = 'Reshma'
s1 = stu()
print(s1.name)

---------------------------------------------------------------

Attributes
------------
--> Attributes are the variables that belongs to a class or an object
class stu:
    name = "Reshma"
    age = 47
s1 = stu()
print(s1.name)
print(s1.age)

methods
-------
-->The functions defined inside the class is methods

class PFS_DA:
    def python(self):
        PFSp_DA ='Batch_03'
        print('This PFS and DA batch_03')

    def Flask(self):
        PFS = 'Batch_03'
        print('This PFS batch03')
all = PFS_DA()
all.python()
all.Flask()

------------------------------------------------------------

Constructor()
-------------
--> A constructor is a special method that is automatically called when an object is created

class ATM:
    def __init__(self, Balance, name):
        self.Balance = Balance
        self.name = name
    def Bal_check(self):
        print(f"{self.name}your total balance is {self.Balance+ 700}")
    def name_(self):
        print(self.name)
card = ATM(Balance = 50000,name='Reshma')
card.Bal_check()
card.name_()

---------------------------------------------------------------------------------------------

Access Specifiers
-----------------
1.Public(no underscore)
2.protected(_)
3.Private(__)

1)Public()
----------
-->This can be accessed anywhere in the program
-->no underscore
class stu_:
    name='Reshma'
s1=stu_()
print(s1.name)

2) Protected
----------------
-->This is represented using a single underscore(_)

class stu_:
    _name = 'Reshma'
s1 = stu_()
print(s1._name)

3) Private
----------
-->This is represented using a double underscore(__)

class stu_:
    __name='Reshma'
s1=stu_()
print(s1._stu___name)

-----------------------------------------------------------------
Encapsulation
-------------
-->Is the process of binding data and methods together

class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo_(self, amount):
        self.__balance += amount
    def get_bal(self):
        return self.__balance
acc = Bank(1000)
acc.depo_(10000)
print(acc.get_bal())









































































































































    
