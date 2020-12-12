from itertools import combinations
n = int(input())
letters = input().split()
k= int(input())
C = list(combinations(letters,k))
f= filter (lambda c: 'a' in c,  C)
print("{:.3}".format(len(list(f))/len(C)))
