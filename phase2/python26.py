#default parameter 
#กำหนด ค่าdefault => def cat(a,b,c=dog)
def data(a,b,c="กรุงเทพ"):
    print("ชื่อ",a)
    print("นามสกุล",b)
    print("เมือง",c)

data("chonapat","chotikulrat") # ไม่กรอก อัน c ทำให้ใช้ค่า default
#or
data(b="chotikulrat",a="chonapat") # ไม่กรอก และ ไม่เรียงลำดับ

