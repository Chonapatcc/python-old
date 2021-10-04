#break = หยุด  / continue = ข้าม
a=1
print(2)
print(3)
print(5)
print(7)
for i in range(2,100):
    if i%2==0:
        continue
    if i%3==0:
        continue
    if i%5==0:
        continue
    if i%7==0:
        continue
    print(i)
    a+=1
    
print(a+4) 

