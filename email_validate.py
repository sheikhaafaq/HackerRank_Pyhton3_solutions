import re

def validate(x):
      if re.search(r'^<[a-zA-Z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$',x):
       #re.match(r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$', y):
            print(name,email)
for _ in range(int(input())):
      name,email = input().split()
      validate(email)

