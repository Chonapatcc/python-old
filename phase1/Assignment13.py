#สร้าง ตารางหมากฮอต

number=int(input("ใส่จำนวน :"))

for i in range(number):
    for y in range(number):
        if (i+y)%2==0:
            print("x",end="")
        else :
            print("o",end="")
    print("")