#count the number of bits from 0 to N

num = int(input("Enter the value of 'N' : "))
count = 0

for i in range(0,num):
    p = str(bin(i))
    q = p.replace("b","").lstrip("0")
    for j in q:
         count += 1
         
print(count)
