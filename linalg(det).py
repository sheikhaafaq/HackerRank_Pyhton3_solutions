##from numpy import linalg
##import numpy
##numpy.set_printoptions(legacy = "1.13")
##arr = numpy.array([input().split() for i in range(2)],int)
##print(linalg.det(arr))
##print(linalg.eig(arr)[0],"\n",linalg.eig(arr)[1])

from numpy import linalg
import numpy as np
n = int(input())
arr = np.array([input().split() for i in range(n)],float)
result  = linalg.det(arr)
print(round(result,2)
)
