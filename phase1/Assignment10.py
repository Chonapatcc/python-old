#ค่าน้อยสุด มากสุด

max,min =0,0
while True :
    number=int(input("ป้อนค่าของคุณ :"))
    if number<=0:
        break
    if number>max :
        max=number
    if number<min :
        min=number
print("ค่ามากสุด:",max,"ค่สน้อยสุด:",min)