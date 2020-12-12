from itertools import combinations_with_replacement as cwr
s,r = input().split()
s=sorted(s)
x =["".join (i) for i in cwr(s,int(r))   ]
for i in x:
      print(i,sep = "\n")
