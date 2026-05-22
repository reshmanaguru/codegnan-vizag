Nested Loop:
---------------------------------
For:
---------------------------------
for i in range (1,2):
    for j in range(1,2):
        print(i)
        print(j)

-----------------------------------------------
     
num = 9
for j in range(1,1):
    print(f"{num} * {j} = {j*num}")
-----------------------------------------------

so = input("Enter a word:")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a palindrome")

-----------------------------------------------------

num = 123
amstro_ = 0
length_ = len(str(num))
for i in str(num):
    amstro_ += int(i) ** length_
if amstro_ == num:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")

-----------------------------------------------------

program for perfect number:


num = 28
perfect = 0
for i in range(1,num):
    if num % i == 0:
        perfect += i
if perfect == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")

-----------------------------------------------------
program for prime number

num = 11
count = 0
for h in range(1,num+1):
    if num % h == 0:
        count += 1
if count == 2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

------------------------------------------------------
Patterns:
---------

star_ = 5
for i in range(1,star_+1):
    for d in range(1,i+1):
        print("*", end="")
    print()

------------------------------------------------------


star = 5
for i in range(1,star+1):
    for r in range(1,i+1):
        print(chr(64+r), end =" ")
    print()

---------------------------------------------------

star = 20
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(count,end =" ")
    print()

-----------------------------------------------------------------

star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        print(j,end =" ")
    print()

--------------------------------------

star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        count += 1
        print(i,end =" ")
    print()

------------------------------------------------

star = 5
count = 0
for i in range(1,star+1):
    for j in range(1,i+1):
        print("*",end =" ")
    print()
----------------------------------------------------

num = 10
for j in range(1,num+1):
    print(" "*(num-j), end="")
    for i in range(1,j+1):
        print("8",end =" ")
    print()


 




    










































