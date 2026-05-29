Modules
--------
-->A modules in python is a file that contains python code such as variables
-variables
-functions
-classes
-statements

Two types of modules
----------------------
user define
built-in
------------
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
--------------------
import math
print(math.sqrt(4))
print(math.factorial(10))
print(math.pow(2,5))
---------------------------
from math import sqrt
print(sqrt(25))
----------------------------
import math as m
print(m.factorial(5))
print(m.pow(2,5))
----------------------------
import os
#os.mkdir("Demo.txt")
os.rmdir("Demo.txt")
---------------------------
import sys
print(sys.version)
print(sys.exit)
print(sys.path)
----------------------------
import random
print(random.randint(1000,9999))
-----------------------------------
from collections import Counter
data = ['a','b','c','d']
counter = Counter(data)
print(counter)
----------------------------------------
from collections import defaultdict
dd = defaultdict(int)
dd['missing'] +=1
print(dd['missing'])
print(dd)












































