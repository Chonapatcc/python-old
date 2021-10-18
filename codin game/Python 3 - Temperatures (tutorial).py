import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
if n>0:
    temp1=[]
    temp2=[]
    temp3=[] # if t==0
    for i in input().split():
        t = int(i)
        if t>5526 or t<-273:
            pass
        else:
            if t>0:
                temp1.append(t)
            elif t==0:
                temp3.append(t)
            else:
                temp2.append(t)
    if len(temp3) > 0:
        print(0)
    else:
        if len(temp1)==0 and len(temp2)==0:
            print(0)
        elif len(temp1)==0:
            temp2.sort()
            temp2=temp2[::-1]
            t=temp[0]
            print(t)
        elif len(temp2)==0:
            temp1.sort()
            t=temp1[0]
            print(t)
        else:
            temp1.sort()
            temp2.sort()
            temp2=temp2[::-1]
            t1=temp1[0]
            t2=temp2[0]
            if t1>abs(t2):
                print(t2)
            elif t1<abs(t2):
                print(t1)
            else:
                print(t1)
            


else:
    print(0)

