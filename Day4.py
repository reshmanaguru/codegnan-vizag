Concatination
-------------------
--->The (+) for int and can add, but for the other data types it will act as concatinating in the data type


a = 90
b = 8
print(a+b)
any = "Python"
so = " is a language"
print(any+so)
an =[1,2]
am =[3,4]
print(an+am)--->[1,2,3,4]


Tuple
-------
--->Collection of different data types separated by commas, represented in () tuple is immutable


some =(1,"Python",[1,2],(3,4))
print(some)
print(some[2][1])


Methods:

i)count():

    this is used to count the particular item in the tuple
    syntax:variable_name.count (item)

some = (1,"Python",[1,2],(3,4)),"Python"
print(some.index("Python"))


ii)index:

    used to find index position of the item, and only gives the first occurance

some =(1,[1,2],(3,4),"Python")
print(some.index("Python"))


any = (1,"Python",[1,2,[34,"this is python 3rd class",78],"Python is a language",89],34,[3,4])
print(any[2][2][1][17])


Dictionary(dict)
-----------
--->Dict is a key : value pair, key and value is separated by : and pair is separated by comma
set of pairs represented by {}
syntax---> dict.key()


eg
-----

reshu_details = {"Name": "reshu",1:2,(1,2): [3,4]}
print(reshu_details)---->{'Name': 'reshu', 1: 2, (1, 2): [3, 4]}


values():
reshu_details = {"Name": "Reshu",
                 "age":20,
                 "MobN":"1234567890",
                 "Pan": "RESHM2026R"}
print(reshu_details.values())--->dict_values(['Reshu', 20, '1234567890', 'RESHM2026R'])

key():

reshu_details = {"Name": "Reshu",
                 "age":20,
                 "MobN":"1234567890",
                 "Pan": "RESHM2026R"}
print(reshu_details.keys())---->dict_keys(['Name', 'age', 'MobN', 'Pan'])


reshu_details = {"Name": "Reshu",
                 "age":20,
                 "MobN":"1234567890",
                 "Pan": "RESHM2026R"}
print(reshu_details["Name"])--->reshu


Update():
    Used to add new key value pair into dict
    synatx--> dict.update({Key:Value})

reshu_details = {"Name": "Reshu",
                 "age":20,
                 "MobN":"1234567890",
                 "Pan": "RESHM2026R"}
reshu_details.update({"Adhar":"1234567890098763647"})
reshu_details.update({"Name":"Reshma"})
print(reshu_details)-->{'Name': 'Reshma', 'age': 20, 'MobN': '1234567890', 'Pan': 'RESHM2026R', 'Adhar': '1234567890098763647'}


clear()
-------
--->Used to remove all the items


reshu_details = {"Name": "Reshu",
                 "age":20,
                 "MobN":"1234567890",
                 "Pan": "RESHM2026R"}
reshu_details.clear()
print(reshu_details)



    





































