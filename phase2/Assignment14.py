#tower of hanoi
a={"adish1":1,"adish2":2,"adish3":3}
b={"bdish1","bdish2","bdish3",}
c={"cdish1","cdish2","cdish3",}


def dish(n,a,b,c):
    if(n==0):
        return
    dish(n-1,a,c,b)
    print("จานที :",n,"จาก",a,"ไป",c)
    dish(n-1,b,a,c)

dish(3,"A","B","C")
    