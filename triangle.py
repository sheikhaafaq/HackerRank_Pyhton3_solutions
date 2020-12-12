AB = int(input())
BC = int(input())

from math import degrees, atan2
print( str(int(round(degrees(atan2(AB,BC)))))+'°')
