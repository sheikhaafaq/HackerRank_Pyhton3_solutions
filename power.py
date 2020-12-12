from math import pow
x = []
for _ in range (3):
    x += [int(input())]


power = pow(x[0],x[1])
mod = power % x[2]
print(int(power))
print(int(mod))
