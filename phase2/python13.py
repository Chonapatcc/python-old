#set {} ข้อมูลซ้้ำกันไม่ได้ ลำดับไม่แน่นอน แก้ไขไม่ได้
# set เร็วสุด (ไม่คิดอันดับ )
# ปกติ
name={5,4,3,2}
namer={12,113,145,51}
tup=("catter","dogo")
lis=[5.34,134,53]


# เพิ่มข้อมูลสมาชิก 
name.add("Cat")
#เพิ่มข้อมูลสมาชิก หลายๆตัว
name.update(namer,tup,lis)

print(name)
#loop 
for item in name:
    print(item)
# นับจำนวน 
print(len(name))

#if 
if 2 in name:
    print("nice")

# ลบ 
name.pop()
print(name)
name.remove("Cat")
print(name)
# discard ลบ ก็ต่อเมื่อมี 
name.discard(5)
print(name)
# clear ลบ ด้านในทั้งหมด 
# del ลบ ตัวมันเลย 