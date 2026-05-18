sets
--------
-->A set is a collection of unique and it is unordered elements
-->Duplicate values are not allowed
-->items are not stored in index order
-->{}


any = {1,2,2,3,4}
print(any)
output-->{1, 2, 3, 4}

ex: any = {1,2,2,3,3,4,7,6,8,9,}
print(any)
output-->{1,2,3,4,6,7,8,9}

Methods
-----------
i)union()
-----------
-->it will give all values from 2 sets together in once 

any = {1,2,2,3,4}
an={81,34}
print(any | an)
print(any.union(an))
output-->{1, 2, 3, 4, 81, 34}
{1, 2, 3, 4, 81, 34}
----------------------------------------------------------

ii)Intersection()
-----------------
-->to get the common elements from both sets

syntax-->Variable_name.intersection(another var)


set = {1,2,2,4,4,5,5,6,7,8,}
se = {2,3,4,7,34,67,89}
print(set.intersection(se))
output-->{2, 4, 7}-->if there a common value it will gives common values only


set = {1,2,3,4,5,6}
se = {7,8,9,0}
print(set.intersection(se))
output-->set()-->if there is no common values then output will come as set()
-----------------------------------------------------------------------------------------

iii)Difference()
-----------------
---> To get the different values from the set
syntax--->variable_name.difference(another var)


any = {1,2,2,3,3,4,5}
an = {3,86,34}
print(any-an)-->{1, 2, 4, 5}
print(an.difference(any))-->{34, 86}
------------------------------------------------
Functions
------------
i)add
-------------
-->to add new element into set
syntax-->variable_name.add(element)


any = {1,2,2,3,4}
any.add(41)
print(any)-->{1,2,3,4,41}

any = {1,2,2,3,4}
any.add(4)
print(any)-->{1, 2, 3, 4}-->if there is a common value it will not give that value for 2 times
--------------------------------------------------------------------------------------------------------

ii)Update
------------
-->to add multiple elements into set
syntax-->variable_name.update([elements])


any = {1,2,2,3,4,5}
any.update([41,45])
print(any)
output--->{1, 2, 3, 4, 5, 41, 45}

iii)sum()
-----------
any = {1,2,2,3,4}
print(sum(any))

iv)remove()
--------------
used to remove element from the set. but it through (key)error if the element not in the set

any = {1,2,3,3,4,5,5}
any.remove(5)
print(any)
output-->{1, 2, 3, 4}












































