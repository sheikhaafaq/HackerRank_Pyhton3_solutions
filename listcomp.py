n = int(input())
arr = []
arr = list(map(int, input().split()))
d= max(arr)

while d in arr:
      arr.remove(d)

print(max(arr))

