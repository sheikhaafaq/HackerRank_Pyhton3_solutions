###the sum tool returns the sum of array elemens over a given axis
##import numpy
##my_array = numpy.array([ [4, 2,4], [3, 4,5] ])
##print("sum \n{}".format(numpy.sum(my_array, axis = 0) ))
##print(numpy.sum(my_array, axis = 1) )
##print(numpy.sum(my_array, axis = None) )
##my_array = numpy.array([ [4, 2,4], [3, 4,5] ])
##print("product\n{}".format(numpy.prod(my_array, axis = 0) ))
##print(numpy.prod(my_array, axis = 1) )
##print(numpy.prod(my_array, axis = None) )

import numpy
n,m = input().split()
my_array = numpy.array([input().split() for i in range(int(n))],int)
print(numpy.prod(numpy.sum(my_array, axis = 0),axis = 0 ))
      
