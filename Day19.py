Polymorphism
------------
-->This means 'many forms'..it allows the same function,method, or operator to behave differently depending on the object...

1.Method overloading
----------------------
--> Method overloading means defining multiple methods with the same name but different parameters
eg
class calcu:
    def add(self,a,b,c=0):
        return a+b+c
An = calcu()
print(An.add(23,6))
print(An.add(23,6,34,45))
           #(or)
class calcu:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
An = calcu()
print(An.add(23,6))

2.Method overriding
-------------------
-->This occurs when a child class provides its own implementation of a method already defined in the parent class

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
        super().sound() #to access the parent class method
ntg = dog()
ntg.sound()

3.operator overloading
----------------------
-->This allows operators such as +,-,* etc,, to perform different actions for user-defined objects
note:-
-------
-->The operator inside the method will overload a special method or operator given in the call
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,b):
        return self.marks + b.marks
so1 = stu(4)
so = stu(78)
print(so1 + so)

Data Abstraction
----------------
-->This is the process of hiding internal implementation details and showing only essential features to user
-->It focuses on what an object does rather than how it does it...


from abc import ABC, abstractmethod
class Shape(ABC):
    
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimeters(self):
        return 2*(self.a + self.b)
an = Rec(10,5)
print(an.area())
print(an.perimeters())
    









































