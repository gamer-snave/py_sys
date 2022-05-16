import math
import cmath
a=10
b=8
c=30
print(cmath.sqrt(20))
print(pow(2, 3))
print(math.pow(2, 3))
print(math.pow(8, 1/3))
print(math.cos(a))
print(math.sin(c))
print(math.log2(2))

print(3%4)

import operator
print(operator.add(a, b))
print(operator.mod(10, 2))
print(operator.mod(a, b))

print(a is not b)

def counter():
    num=0
    def incrementer():
        nonlocal num
        num+=1
        return num
    return incrementer
k=counter()
print(k)
print(k)
print(k)
print('foo'>'FOO')