from collections import OrderedDict as od
ord_dict = od()
n = int(input())
for i in range(n):
      word = input()
      ord_dict.setdefault(word,0)
      ord_dict[word]  += 1
      
print(len(ord_dict))
print(*ord_dict.values())
      
      
