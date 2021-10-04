# math function
x=min(3,4,5,6,7,-18,-10) #น้อย สุด min
print(x)

y=max(3,4,5,7,8,-13) # มาก สุด max
print(y)

z=abs(-50) # absolute
print(z)

p=pow(5,2) # ยกกำลัง
print(p)

import math
result=math.sqrt(64) #square root 
#ปัดลง = floor(<=80) ปัดขึ้น = ceil(>80) 
score=math.ceil(80.0000001)
print(score)
print(math.pi)

#ค่าทางตรีโกณ
convert=math.radians(30) # degree =>rad
print(convert) #rad
x=math.sin(convert)
y=math.cos(convert)
z=math.tan(convert)

print(x,y,z)
point1=[2,-3]
point2=[7,-3]
# คำนวนหาระยะทาง
d=math.dist(point1,point2)
print(d)

# log
log=math.log2(32)
print(log)