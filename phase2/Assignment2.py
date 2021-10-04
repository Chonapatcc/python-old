#หาค่าตัวเลขต่ำสุดมากสุด

number=[]

while True:
    x= int(input("put your number :"))
    if x<0:
        break
    number.append(x)

number.sort()
print(number)
print("ค่าน้อยสุด :",number[0])
print("ค่ามากสุด",number[-1])
print("น้อย",min(number),"มาก",max(number)) 