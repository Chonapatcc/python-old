# สร้างขอบตาราง

number=int(input("ป้อนข้อความ :"))

for i in range(number):
    for y in range(number):
        if i==0 or i==number-1 or y==0 or y==number-1 :
            print("x",end="")
        else:
            print(" ",end="")
    print("")