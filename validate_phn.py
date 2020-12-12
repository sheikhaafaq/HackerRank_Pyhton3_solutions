import re
for i in range(int(input())):
      print('YES' if re.search(r"^[7-9]\d{9}$",input()) else 'NO')

##
##import re
##for i in range(int(input())):
##      s = str(input())
##      
##      print('YES' if (s[0] == '9' or s[0] == '8'or s[0] == '7') and s.isnumeric() and len(s) == 10 else 'NO')
