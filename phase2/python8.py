# การคัดลอกข้อมูล
animal=["cat","dog","hippo"]
number=[1,2,3,4,5,6,5,4,4,6]
x=[]
print(x)
x=animal.copy()
print(x) 

# การรวมข้อมูล (x)
allgroup=animal+number
print(allgroup)
animal.extend(number)
print(animal)

#แสดงจำนวนสมาชิก

y=number.count(4)
print(y)
