##from collections import OrderedDict as od
##ord_dict = {}
##
##ord_dict['a'] = 1
##ord_dict['b'] = 2
##ord_dict['c'] = 3
##ord_dict['d'] = 4
##ord_dict['e'] = 5
##print(ord_dict)
##
##ord_dict1 = od()
##
##ord_dict1['a'] = 1
##ord_dict1['b'] = 2
##ord_dict1['c'] = 3
##ord_dict1['d'] = 4
##ord_dict1['e'] = 5
##print(ord_dict1)

from collections import OrderedDict as  od
ord_dict = od()
num = int(input())
for _ in range(num):
      item = input().rpartition(" ")
      ord_dict[item[0]] = int(item[-1]) +  ord_dict[item[0]] if item[0] in ord_dict else int(item[-1])
for i,j in ord_dict.items():
      
      print( i,j)
      
      
      
      


