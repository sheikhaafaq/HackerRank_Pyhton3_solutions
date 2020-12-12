Eng = int(input())
RE = set(map(int,input().split()))
Fre = int(input())
RF = set(map(int,input().split()))

print(len(RE.difference(RF)))
