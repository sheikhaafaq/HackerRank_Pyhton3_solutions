import string
arr = []
for _ in range(int(input())):
      x=input().split()
      cmd = x[0]
      args = x[1:]
      if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("arr."+cmd)
      else:
            print(arr)
