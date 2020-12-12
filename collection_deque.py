##
####d.append('5')
##d.extend('0123489')
##print(d)
####d.reverse()
##d.rotate(9)
####d.popleft()
####d.remove('4')
##print(d)
##
from collections import deque
d = deque()
for _ in range(int(input())):
      method= input().split(" ")
      cmd = method[0]

      if  cmd !="pop"and cmd !="popleft" :
     # or cmd !="popleft":
            args = method[1] 
            cmd += "(args)"
            eval("d."+cmd)
            
          
      else:
            eval("d."+cmd +"()")
print(*d)
 
