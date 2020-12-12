from fractions import Fraction
from functools import reduce

def product(fracs):
    t =  reduce(lambda x, y : x * y, fracs) #complete this line with a reduce statement
    return t.numerator, t.denominator

L =[]
M=[]
n = int (input ())
for _ in range (n):
      m = list(map(int,input().split()))
      L.append(m[0])
      M.append(m[1])
a = product(L)
b= product(M)
print("{} {}".format(*a,*b))
      
      
