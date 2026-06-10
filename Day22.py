ERROR HANDLING
---------------
1.TRY BLOCK:

    it will test a block of code for error

2.EXCEPT:

    the except block let handle if the code contains error

3. ELSE BLOCK:

    this will be excuted, if the try block contain error or not

4.FINALLY:

    this will be excuted either try block contain error or not 

try:
    print(10/0)
except:
    print("this will handle ZeroDivisionError")

a = 12
b = "hai"
try:
    print(a+b)
except:
    print("this is syntaxerror")

a = 5
try:
    print(len(a))
except:
    print("this is attribute error")
--------------------------------------------------------------
a = "hi this is python"
try:
    print(b)
except:
    print("this is syntax error")
--------------------------------------------------------------
a = 7
try:
    print(b)
except:
    print("this is name error")
--------------------------------------------------------------
try:
    print("hi"+"py")
except NameError:
    print("this will handle nameerror")
else:
    print("no error")
--------------------------------------------------------------
try:
    print(45+"py")
except TypeError:
    print("it is typeerror")
else:
    print("no error")
--------------------------------------------------------------
try:
    print(5+"py")
    print(b)
except NameError:
    print("this is nameerror")
except TypeError:
    print("this is typeerror")
else:
    print("there is error")

note: it prints only the 1st error in the try block and exit the block
-----------------------------------------------------------------------
try:
    print("hai")
except:
    print("error")
else:
    print("the end")
finally:
    print("true")












    
