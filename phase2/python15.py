#subset กลุ่มของ set ย่อย 
animal={"cat","dog","rabbit","shark"}
x={"cat","dog"}

print(animal.issuperset(x)) # animal เป็น superset ของ x

print(x.issubset(animal)) # x is subset ของ animal

# max min 
number={1,2,3,4,5,6,8,9,23,245,25,-2}

print("ค่าน้อยสุด",min(number))
print("ค่ามากสุด",max(number))
