# ค้นหา จำนวนตัวอักษร

name=["cat","dog","rat"]
letters=[]
letter=0

for i in name:
    x=len(i)
    letter+=x
    letters.append(i.count("a"))

print("มี a",letters,"ตัว")
print("ทั้งหมด",letter,"ตัว")
