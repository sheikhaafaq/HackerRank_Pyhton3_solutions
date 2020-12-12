import numpy as np
arr = list(map(float,input().split()))
x =int(input())
coeff = np.polyval(arr,x)
print(coeff)
                   
