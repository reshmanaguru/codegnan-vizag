FILE HANDLING
--------------
-->File handler is an object of file to maintain several function of file like, creating, reading, updating and deleting the file..

Open a File
-----------
1.open()
2.with open()

name = open('file', 'mode') as name
---------------------
---------------------
name.close()

modes
-----
'r'--> is used to reading the file, error if file does not exit....
'a'--> is used to add the text into file, if file does not exit....
'w'--> is used to add the text into file but it will override of all text inside file...

so = open('demo.txt','r')
print(so.read())
so.close()

so = open('demo.txt','a')
print(so.write('reshmanaguru'))
so.close()

so = open('demo.txt','w')
print(so.write('java'))
so.close()

so = open('dm.txt','w')
print(so.write("python"))
so.close()

with open('demo.txt','w') as so :
    print(so.write('java'))


Method
------
write()
read()
------
-->This method can read entire file chunk by chunk where we can specify the side

readline()
----------
-->Can read only one line at a time in a file...

readlines()
-----------
-->It will read entir file and gives in a list where each line is each index in the list




with open('dem.txt','w') as any:
    any.write('hello')

so = open('demo.txt','r')
print(so.read())

with open('demo.txt','r') as any:
    print(any.read(30))
    any.close()

any = open('demo.txt','r')
print(any.readline())
any.close()

any = open('demo.txt','r')
print(any.readlines())
any.close()

import os
os.remove('dem.txt',)












          




























