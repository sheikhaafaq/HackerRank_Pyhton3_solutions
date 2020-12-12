A = set(map(int,input().split()))
result = list()
h = "True"
for i in range(int(input())):
      B= set(map(int,input().split()))
      if B-A == set() and A-B !=set():
            result .append(1)
      else:
            result .append(0)
      for i in set(result):
            if i== 0:
                  h = "False"
                  break
print(h)
      
