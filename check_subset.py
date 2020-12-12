# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    num_A = int(input())
    A = set(list(map(int,input().split()))[0:num_A])
    num_B = int(input())
    B = set(list(map(int,input().split()))[0:num_B])
    if A-B ==set():
          print("True") 
    else: 
        print("False")
