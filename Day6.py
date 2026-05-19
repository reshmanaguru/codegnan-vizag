Type conversion
------------------

1)int-->it can be converted into str and float

an = 78
us = str(an)
om = float(an)
some = list(an)
print(om)
print(type(om))---><class str>
print(type(us))--->class float>
print(type(some))-->type error

-----------------------------------------

2)str-->it can be coverted into int,list

an = "Python"
some = int(an)
print(some)-->value error

an = "60"
some = int(an)
print(some)--->60

an = "90"
some = list(an)
print(some)--->['9', '0']

----------------------------------------------------

3)Float--->float can be converted into int,str,

car = 90.68
print(int(car))--->90

car =60.67
print(type(str(car)))--><class 'str'>

car = 90.56
print(str(car))-->90.56

--------------------------------------------

4)List--> can be coverted into tuple and string

any = [1,10]
some = str(any)
print(str(any))
print(tuple(any))

---------------------------------------------

5)Tuple--> convert into list 

how = (4,5)
print(list(how))-->[4,5]
print(str(how))(4,5)

-----------------------------------------------

user inputs

1)int as a user input

n = (input("enter a number:"))
print(89+n)-->enter a number:30
               #119

-----------------------------------------------

2)str as a user input

any = input("enter a number:")
print(any)-->enter a number:40

----------------------------------------------------------------

3)List as a user input

any = input("enter number :").split()
print(any)--->enter number :3 45 67
                #['3', '45', '67']

any = list(map(int,input("Enter numbers: ").split()))
print(any)-->Enter numbers: 4 5 6
              #[4, 5, 6]

-----------------------------------------------------

4)Tuple as a user input

an = tuple(map(int,(input("enter a values:").split())))
print(an)--->enter a values:9 9 0 8
             #(9, 9, 0, 8)

an = eval(input("enter:"))
print(an)-->56          

























































 


















































































