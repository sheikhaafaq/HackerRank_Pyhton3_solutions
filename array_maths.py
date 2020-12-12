import numpy
##a  = numpy.array([1,2,3,4],float)
##b = numpy.array([5,6,7,8],float)
##print(a+b)
##import numpy as np
####n, m = map(int, input().split())
##a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
##print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
##x = numpy.add(a,b)
##print(x)

n,m = input().split()
a,b  = (numpy.array([input().split(" ") for i in range(int(n))],int) for j in range(2))
print(a+b,a-b,a/b,a%b,a**b)
