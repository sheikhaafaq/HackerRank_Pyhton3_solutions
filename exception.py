
for i in range(int(input())):
      a,b =list(input().split())
      try:
            print(int(a)//int(b))
      except Exception as e:
            print ("Error Code:",e)
      
