##from collections import Counter as ct
##mylist= [1,2,3,4,5,6,7,8,1,2,3,1,2,4,5,4,5,6,7,9]
##x=ct(mylist)
##print(*x.items())
##print(*x.keys())
##print(*x.values())
##
##
##print("____________________________________________________")

from collections import Counter as ct
numshoes = int(input())
shoes = ct(map(int,input().split()))
customer = int(input())

amount = 0

for i in range(customer):
      size,price =map( int,input().split())
      if   shoes[size]:
            amount += price
            shoes[size] -= 1
print(amount)
      
      
      
