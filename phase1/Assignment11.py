#ตัวเลข ขั้น บันได

last=int(input("จำนวนที่ต้องการ :"))

for row in range(1,last+1):
    for colum in range(1,row+1):
        print(colum,end=(""))
    print("")