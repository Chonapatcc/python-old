# รับและเรียงลำดับข้อมูล
collector=[]

while True:
    number=int(input("ใส่เลข :"))
    if number<0:
        break
    collector.append(number)

print("before sort",collector)
collector.sort()
print("น้อยไป มาก",collector)
collector.reverse()
print("มากไปน้อย",collector)
print("End")

