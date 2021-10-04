#หากลุ่มเลขคู่/คี่

single=[]
dual=[]

while True:
    x=int(input("Your number :"))
    if x<0:
        break
    elif x%2==0:
        dual.append(x)
    else:
        single.append(x)

print("คู่",dual,"คี่",single)