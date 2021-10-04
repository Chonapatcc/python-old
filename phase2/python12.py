# ค้นหาและนับจำนวนดสมาชิก ด้วย (count)
#count
tup=(1,2,3,4)

tup=list(tup)

x=tup.count(4) # หาจำนวน 
print(x)

#ค้นหาสมาชิกด้วย index 

y=tup.index(4) # อยุ่ที่ index อะไร
print(y)

# การ sort 
name=(1,2,4,2,5,6,7,8,3,2,123,43)
# tuple ใช้ sort ไม่ได้ เปลี่ยน ไปเป็นlist 

name=list(name)
name.sort() # .reverse 

name=tuple(name)
print(name)
# นำค่าใน tuple => ตัวแปร
axis=(2,4,5)
x,y,z=axis 
print(x,y,z)
# สลับ tuple 
x=(23,34)
y=(1,2)
print("before :",x,y)
x,y=y,x
print("after :",x,y)

#tuple => string 
x=("a","b","c")
name="".join(x)
print(name)
#reversed  tuple 
y=(1,2,3,4) 
x=reversed(y)
print(tuple(x)) 
# string to tuple
name="Phuree penhirun"
print(name[::-1])
name=tuple(reversed(name))
name="".join(name)
print(name)


