K  = int(input())
rooms = list(map(int,input().split()))
s1 = set()
s2 = set()
for i in  rooms :
      if i in s1:
            s2.add(i)
      else:
            s1.add(i)
print(*(s1 - s2) )
