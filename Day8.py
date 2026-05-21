elif
---------------
----> used to check more conditions

stu_marks = 90
if stu_marks >=90:
    print("A+")
elif stu_marks >=80:
    print("A")
elif stu_marks >=70:
    print("B+")
elif stu_marks >=60:
    print("B")
elif stu_marks >=50:
    print("C+")
elif stu_marks >=35:
    print("pass")
else:
    print("Failed")

---------------------------------
program to find maximum number from three numbers:

a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


nested if
---------------------------------

problem for SBI ATM
---------------------------------
SBI_bank ={"ATM PIN": "6600"}
pin = input("Enter 4 digit ATM pin:")
if len(str(pin)) ==4:
    if pin in SBI_bank['ATM PIN']:
        print("Wel come to SBI ATM")
    else:
        print("Invalid pin")
else:
        print("pls enter 4 digit pin")

--------------------------------------------------

FOR LOOP :
--------
for statement
---------------
-->used to itterate over a squence


any = "python"
hm = [1,2,3,4]
re = [5,6,7,8]
for how in any:
    print(how)
    
--------------------------------------------------

Range():
----------
--> range is in-built function use to generate number in sequence manner
syntax:range(start,end,step)
for i in range(1,6)
     print(i)#---->#1 2 3 4 5

------------------------------------------------

else in for loop
--------------------------

for i in range(1,10):
    print(i)
else:
    print("Code ended Here")

------------------------------------------------------
While loop:
----------------
---> while is the combination of for and if


i = 1
while i < 5:
    print(i)
    i +=1
---------------------------------------------------
Conditional Statements:
-----------------------
1)Break:
------------    
usedto exit from the loop based on the condition

for i in range(1,10):
    if i == 6:
        break
    print(i)
---------------------
2)Continue():
----------------------
used to skip the current iteration based on the condition


for i in range(1,10):
    if i == 5:
        continue
    print(i,end=" ")

3)Pass():
----------------------
pass is a space holder

for i in range(1,10):
    if i == 3:
        pass
    print(i,end=" ")




























    
    
    
    
        















    

    
    
