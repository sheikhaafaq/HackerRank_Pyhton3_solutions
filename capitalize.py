def solve(s):
    
    return (' '.join((word.capitalize() for word in s[:].split())))
 
result= solve(input())
print(result)