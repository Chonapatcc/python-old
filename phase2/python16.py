#frozen set 
# จะไม่สามารถเพิ่มลบได้ มันได้เลย แม้ จะเปลี่ยน เป็น list แล้วก็ตาม
# structor name=frozenset(list)
number=frozenset[1,2,2,4,5]
# number.add("cat") ใช้ ไม่ได้
print(number)


