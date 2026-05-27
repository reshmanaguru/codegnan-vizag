Assert
------------------
-->this is debugging statement
--->used to test whether a conditon is True or not
-->we dont use semicolon at the end 
-->AssertError

num = 10
assert num>5
print("True")
---------------------------------------------------

Function
-------------
-->A function is block of code which only execute when it is called
-->You can pass data,know as parameters into a function
-->To avoid repeated lines in code

def function_name(parameters):--->definition line 
    after writing the code
function_name(arguments)---->calling function

1)num = 9
def even(num):
    print(num)
even(num)
--------------------------------------------------------------
2)num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} EVen")
    else:
        print(f"{num} Odd")
even(num)
even(109,90)

Ways to pass arguments:
-------------------------------------------------------------
1)Required arguments
---> A function must be called with the same number of arguments asa parameters

def even(num,num1,num2):
    if num1  %2==0:
        print("even")
    else:
        print("odd")
even(5,10,15)

---------------------------------------------------------------
2)Default arguments:
--->By default values are defined at paraments even though it will take from arguments

def details(name = "reshu"):
    print(name)
details("reshma")
details("reshu")

---------------------------------------------------------------
3)Keyword arguments:
-->we can send arguments with key=values syntax .by this,the order of arguments does not matter

def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even(name = "reshu",age = 22,sal = 750000)
--------------------------------------------------------------
4)variables length arguments:
-->ding a star(*) before the parameter name in the function, recevice a tuple of arguments and can access items with indexes

def even(*name):
    print(name[4])
even("reshu","reshma","mohana","nitya","sravani")
--------------------------------------------------------------
5)reference arguments:
-->

name = "reshu"
def even(any):
    print(any)
even(name)

--------------------------------------------------------------


for i in range(2,100):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"{i} is a prime")

--------------------------------------------------------------
1)Program for tables

def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {i*num}")
table(9)

---------------------------------------------------------------

2) program for palindrome:

def palindrome(so):
    empty_str=""
    for i in so:
        empty_str = i + empty_str
        print(empty_str)
    if empty_str == so:
        print(f"{so} is palindrome")
    else:
        print(f"{so} is not a palindrome")
palindrome("reshma")
palindrome("python")

---------------------------------------------------------------

3) program for amstrong:

def amstrong(num):
    amstro =0
    length = len(str(num))
    for i in str(num):
        amstro += int(i) **length
    if amstro == num:
        print(f"{num} is a amstrong number")
    else:
        print(f"{num} is not a amstrong number")
amstrong(153)

--------------------------------------------------------------

4)program for prime number :

def prime():
    for num in range(2,101):
        count=0
        for j in range(1,num+1):
            if num%j ==0:
                count+=1
        if count==2:
            print(f"{num} is a prime")
prime()

--------------------------------------------------------------

5)program for prime number :

def prime(num,count):
    for h in range(1,num+1):
        if num % h == 0:
            count += 1
    if count == 2:
        print(f"{num} is prime number")
prime(11,0)

---------------------------------------------------------------

6)program for pattern:

def pattern(num):
    for i in range(1,num+1):
        print("*"*i)
pattern(5)

-------------------------------------------------------------------

7)
def pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(chr(64+j),end=" ")
        print()
pattern(5)

------------------------------------------------------------------

8)
def pattern(num,count):
    for i in range(1,num+1):
        for j in range(1,i+1):
            count += 1
            print(count,end=" ")
        print()
pattern(5,0)

---------------------------------------------------------

9)

def pattern(star):
    for i in range(1,star+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
pattern(5)

-----------------------------------------------------------

10)
def pattern(star):
    for i in range(star,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
pattern(5)

-----------------------------------------------------------

11)
def pattern(star):
    for i in range(1,star+1):
        print(" "*(star-1),end=" ")
        for j in range(1,star+1):
            print("*",end=" ")
        print()
pattern(5)

--------------------------------------------------------------

12)PROGRAM FOR PERFECT NUMBER:
def perfect_num(num,perfect):
    for j in range(1,num):
        if num%j==0:
            perfect += j
    if perfect == num:
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not perfect number")
perfect_num(28,0)

----------------------------------------------------------------

13)PROGRAM FOR PRIME NUMBERS:
def prime():
    for i in range(2,6):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
prime()

-----------------------------------------------------------

14)PROGRAM FOR ATM:
    
user_info = {"Name":"Deepthi",
             "MOBILE NO":"7416364639",
             "ATM PIN":" 2004",
             "BALANCE" : 76345,
             "TRANSACTION HISTORY":[]
             }

def atm():
    print("please insert your ATM card")
    remaining_attempts = 3
    while remaining_attempts >0:
        user_pin = input("please enter 4 digit pin:")
        if len(user_pin) == 4:
            if user_pin in user_info["ATM PIN"]:
                a = int(input("enter \n1.withdrawl \n2.check balance \n3.mini statement \n4.deposit"))
                if a == 1:
                    w_a = int(input("enter withdrawl amount:"))
                    if w_a > user_info["BALANCE"]:
                        print("insufficient balance")
                    elif w_a < 100:
                        print("please enter minimum amount")
                    elif w_a %100 !=0:
                        print("enter amount without change")
                    else:
                        print("please take your cash")
                        break
                elif a == 2:
                    print("your balance amount is :")
                    break
                elif a == 3:
                    print("your mini statement:")
                    break
                elif a == 4:
                    print("withdrawl amount:")
                    break
            else:
                remaining_attempts -= 1
                if remaining_attempts > 0 :
                    print(f"you have {remaining_attempts} chances left.please enter correct pin")
                else:
                    print("your card has been temporarily blocked")

atm()

------------------------------------------------------------------------

15)PROGRAM FOR GREATER NUMBER:
    
def greater(a,b,c):
    if a > b and a > c:
        print(f"{a} is greater")
    elif b > a and b > c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
greater(5,8,10)

---------------------------------------------------------------

16)PROGRAM FOR STUDENTS GRADE:
    
def grade(stu_marks):
    if stu_marks >= 90:
        print("A+")
    elif stu_marks >= 80:
        print("A")
    elif stu_marks >= 70:
        print("B+")
    elif stu_marks >= 60:
        print("B")
    elif stu_marks >= 50:
        print("C+")
    elif stu_marks >= 35:
        print("pass")
    else:
        print("fail")
grade(87)

-----------------------------------------------------------------------------------

17)PROGRAM FOR LEAP YEAR:
def leap(year):
    if (year%4==0 and year%100!=0) or year%400 == 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
leap(2024)

-----------------------------------------------------------------------------------

18)PROGRAM FOR TRAFFIC SIGNAL:
def traffic():
    signal = int(input("enter \n1.red \n2.green:"))
    if signal == 1:
        print("pls stop")
    else:
        print("go")
traffic()

--------------------------------------------------------------------------

19)Program for ATM PIN:

def SBI(pin):
    SBI_bank = {"ATM PIN":"2005"}
    if len((pin)) == 4:
        if pin in SBI_bank['ATM PIN']:
            print("welcome to SBI ATM")
        else:
            print("Invalid pin")
    else:
        print("pls enter 4 digit pin")
SBI("2005")

---------------------------------------------------------------------------
20)program for fibanocci

num = 0
num_2 = 1
def fibanocci(num,num_2):
    limit = int(input("Enter the limit:"))
    print(num,num_2,end=" ")            
    for i in range(1,limit):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3, end=" ")
fibanocci(num,num_2)

-----------------------------------------------------------------------------
21) program for removing duplicates

list = [2,4,5,6,7,2,4]
any = []
def duplicate(list,any):
    for i in list:
        if i not in any:
            any.append(i)
    print(any)
duplicate(list,any)

22)program for count letters in string:

count =0
so ="quantum computing is an advanced field of technology that harnesses the laws of quantum".split()
def word_str(so,count):
    for i in so:
        count +=1
    print(count)
word_str(so,count)








        

    
    
            



                
    
    
    

    

























































