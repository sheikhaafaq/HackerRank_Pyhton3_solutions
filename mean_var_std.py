from numpy import mean,std,var,array
import numpy

numpy.set_printoptions(legacy='1.13')
n,m = input().split()
my_array =array([input().split() for i  in range(int(n))],int)
print(mean(my_array, axis = 1)) 
print(var(my_array, axis = 0))
#numpy.around(my_array,decimals=11)
print(std(my_array,axis = None))

