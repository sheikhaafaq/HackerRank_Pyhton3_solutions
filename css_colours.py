import re
for _ in range(int(input())):
       #pattern = re.findall(r'#[a-fA-F0-9]\{3,6}',input())
       pattern = re.findall(r':?.(#[0-9a-fA-F]{3,6})', input())
       if pattern:
             print(*pattern ,sep = "\n")
