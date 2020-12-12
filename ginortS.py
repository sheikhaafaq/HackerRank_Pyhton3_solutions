##from __future__ import print_function

upper = []
lower = []
even = []
odd = []

def separator(x):
      for a in x:
            if a.isalpha():
                  if a.isupper():
                        upper.append(a)
                  else:
                        lower.append(a)
            else:
                  if int(a)%2 == 0:
                        even.append(a)
                  else:
                        odd.append(a)
      return
    
separator(input())  


upper.sort()
lower.sort()
even.sort()
odd.sort()
t = lower+upper+odd+even
print("".join(t))

