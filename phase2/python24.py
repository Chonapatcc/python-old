#arbitrary arguments (*args)

#args
def add(*args):  #*args = tuple
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    print(sum)

add(1,2,3,4,5)



