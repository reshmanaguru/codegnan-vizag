'''
1.Program to convert 24h clock into nrml clock
'''
'''
time = input("enter 24 hours time: ")
parts= time.split(":")
hour= int(parts[0])
min= int(parts[1])
print(f"{time} is converted into {hour - 12}:{min} pm")'''


'''

2.List
---------------
-->List is collection of diffteent data types
-->[] and separated by,
-->mutable


any = [1,"Python",[1,2,[34,"this is python 3rd class",78],"Python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])



Methods
----------
append()
----------
-->this method is used to add new item into list, and it will in the last index position
syntax ---->variable_name.append(item)

mutable
---------------
-->Can able to modify on that particular variable
eg:"list'''
'''
any = [1,2,3]
any.append(6)
print(any)
any.append([20,90])
print(any)

Immutable
------------
-->Could not able to modify on that particular variable 

so = "Python is a"
print(so.replace("Python","Java"))
print(so)
any = [1,2,3]
print(any.append(6))
print(any)


3.Extend()
------------
-->this method is used to add itterable into list, and it will in the last index position, each value or substring is each index in the list

syntax-->variable_name.extend(itterable)



any = [1,2,3]
any.extend("Python")
any.extend([1,2,4])
print(any)


4.Pop()
---------
-->used to remove the item from the list, but will mention here index position in the pop method

any = [1,2,3]
print(any.pop(2))-->it gives what value is deleted in the output
any = [1,2,3]
any.pop(2)
print(any)-->it gives the list after removing the value


5.Remove()
------------
 used to remove item from the list, but will mention here direct in the remove method
 syntax-->variable_name.remove()
'''
 
any = [1,2,3]
any.remove(2)
print(any)
any=[1,2,3]
print(any.remove(2))




















































