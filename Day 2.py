'''
a = 3
b = 6
print(a//b)

operators
-----------
i)Arithmetic operator

        +,-,*,%,/,//,**

a = 2
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**)

ii)Assignment operator

        =,+=,-=,>=,<=,%=,*=


count = 0
for j in range (1,10):
    count += 1
print(count)


iii)Comparision operator
---------------------------------------------------
------>looks for the both values equal or not  

        == ,!= ,>= ,<= ,> ,< ,!=

a = 4
b = 6
print(a==b)

iv)Identity operator
-----------------------------
------->this operator looks for the object is same or not 

a = [1,2]
b = [1,2]
c = a
print(type(a))
print(a == b)
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a is not b)


v)Logical operator
--------------------
and , or , not
and-->this is used to check both should be true

a = 15
if a%3==0 and a%5==0:
    print("True")
    



or--->if any condition is ture then it is true


a = 15
if a%3==0 or a%5==0:
    print("True")

    
vi)Membership operator
-----------------------------
in,not in
a = 3
b =[1,2,3,]
c = 5
print(a in b)
print(a not in b)



vii)Bitwise operator
-------------------------
&,|, <<,>>


print(5&3)
print(5|3)
print(5<<)
print(5>>3)



-->String
------------------
-->String is squence of characters that are enclosed in 
-->it should be '', "", ''' '''(only comments)
-->String is inmutable(not changable) 
name ="Python78"
for j in name:
    print(j)


methods
---------
1)Replace()
---------
-->Used to replace with new substring

syntax--->Variable_name.replace("old string","new string")


any = "Python is a language"
print(any.replace("Python", "Java"))
print(any)


2)Split():
----------- 
used to separate into parts, and it will split based on the substring where before the substring is one index and after is another index in the list form


any = "Python is a language"
print(any.split("a"))


3)len()
    gives the length of the string
any = "Python is a language" 
print(len(any))

4)Slicing():
----------------
-->Slicing can give the access to get particular index form the string

syntax--->variable_name[starting index : ending index]


any = "Python is a language"
print(any[3:11])


5)Indexing:
------------
-->Used to get substring present in that index position ....'''


any = "Python is a language"
print(any[8])
print(any.index("ang"))

      




 



















