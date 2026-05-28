List comprehension
-------------------
--> LC offers a shortest syntax when we want to create a new list from existing list

-->syntax--> vari_name = [expression loop condition]

old = [1,2,3,4,5]
new = [so for so in old]
print(new)

old = [1,2,3,4,5]
new = [so for so in old if so%2==0]
print(new)#-->even ouput

old = [1,2,3,4,5]
new = [so if so%2!=0 else "even" for so in old]
print(new)

Generators
------------
--> Generators in python are a special type of itterable,allowing users to iterate over data efficiently without storing everything in memory
-->They generate the values lazily yeild keyword


why to use gen
----------------------
-->Generators does not store the entire dataset in memory, they generate values on the run time
-->Avoiding unnecessary storage of data speed up execution
-->This is also used in pipelines topic

How it works
------------
-->It looks like nrml function but uses the yield keyword instead of return
-->When the function is called, it does execute immediately. Instead, it return a generator object which can be iterated using loop or the next() function  

1)def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    yield 4
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


2)def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

3)def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))


so = 'Quantum computing is an advanced field of technology that harnesses the laws of quantum'
any = ''
for i in so:
    if i not in "AEIOUaeiou":
        any +=i
print(any)

    





        



























