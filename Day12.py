Built-in functions

---------------------------------

print():

n = 5
print(n)

------------------------------------

input():
    
n = int(input())
print(n)

---------------------------------------

len():

a = [1,2,3,4]
print(len(a))

-------------------------------------------

max():

a = [3,4,5]
print(max(a))

-------------------------------------------------

min():

a = [4,5,6]
print(min(a))

---------------------------------------------

m = [3,4,6,2]
m.sort()
print(m)--->[2, 3, 4, 6]


m = [3,4,5,6,7,2,3]
m.sorted()
print(m)--->object has no attribute

---------------------------------------

Recursive functions:
--->A recursive function that calls itself to slove a problem by breaking it into small or simple sub-problem

def fac(num):
    if num == 1:
        return 1
    return num *fac(num-1)
print(fac(5))

--------------------------------------------

return():

------------
-->this end a function execution and sends a value back to the code that called the function

def add(a,b):
    return a+b
res = add(10,5)
print(res)

Lambda functions

----------------------------------
--> A lambda function is a small anonamus functions
--> lambda can take n number of arguments, but only one expression
-->syntax--> lambda arguments : expression


so = lambda a,b,c: a+b+c+a
print(so(3,4,5))

so = lambda a,b: a-b
print(so(6,3))

so = lambda a,b: a%b
print(so(4,5))

















































