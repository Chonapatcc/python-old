import math
n=100
n2=0
t1=int(input())
t2=int(input())
p=[]
p2=[]
while n>0:
    n-=100/(24-(t1-t2))
    p.append(math.ceil(n))
while n2<100:
    n2+=100/(t1-t2)
    p2.append(math.ceil(n2))
print(p,p2)

    