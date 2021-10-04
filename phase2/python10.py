#การแก้ไขข้อมูล
#ใช้ tuple ควบคู่กับ list

tup=(1,2,3,4,5)

lis=list(tup)
lis[0]="kangaroo"
tup=tuple(lis)
print(tup)

#การแสดงผลด้วยloop
cat=(1,2,3,4,5)

for x in cat:
    print(x)

# การตรวจสอบข้อมูล
if "cart" in cat :
    print("Yes")
else:
    print("no")

# การนับ สมาชิก
print(len(cat))
# len ทำ งานร่วมกับ loop for
for i in range(len((cat))):
    print(i)
