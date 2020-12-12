from collections import namedtuple
#code 1 exp
##point  = namedtuple('point','x,y')
##pt1= point(1,2)
##pt2 = point(3,4)
##dot_product = (pt1.x *pt2.x) +  (pt1.y *pt2.y)
##print(dot_product)

# code 2 exp

##car = namedtuple('car','mileage ,price, colour, Class')
##sentro = car(mileage = 30, price = 100000, colour = 'cyan',  Class= 'X')
##print(sentro)
##print(sentro.mileage)
###HackerRank problem

n=int(input())
student = namedtuple('student',input().strip().split())
ans=sum(float(student(*input().strip().split()).MARKS) for _ in range(n))/n
print("{}0".format(ans))
