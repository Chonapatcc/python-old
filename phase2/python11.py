# การสร้างและเพิ่มข้อมูล (join)
#สร้าง
x=("cat",)

#เพิ่ม

name=("cat","jojo")
new=("nut",)
name+=new
print(name)
#ทำงานร่วมกับ list

cat=(1,2,3,4)
dog=[2,5,7,8]

cat+=tuple(dog)
print(cat)
#การลบข้อมูล del,การลบแบบ list
y=(2,3,4)
del x 
        # x หายไป
#เปลี่ยน เป็น list แล้ว ลบ 
lis=list(y) # กลายเป็น list
print(lis)
lis.pop() # pop ลบ ขวาสุด
print(lis)
lis.remove(3) # remove("")
print(lis)
lis.clear() # เอา ออกหมด
print(lis)