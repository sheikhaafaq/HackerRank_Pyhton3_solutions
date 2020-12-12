num_A  = int(input()) #no. of elements in set A

A = set(list(map(int,input().split()))[0:num_A]) # input element in A of length num_A

for i in range(int(input())): # no. of operations performed
       cmd,L=  input().split() # operation , length of set B
       B =  set(list(map(int,input().split()))[0:int(L)])  # set B of length L
       eval('A.{}({})'.format(cmd,B))  #evaluate expression
       #getattr(A, cmd)(B)

print(sum(A))  # Display sum
