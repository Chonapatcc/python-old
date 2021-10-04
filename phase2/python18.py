# การลลบ dict
animals=dict(cat="แมว",dog="หมา")
animal=dict(cat="แมว",dog="หมา")

animals.pop("cat") #(key)
animals.popitem() # ลบขวาสุด
print(animals)
animals.update(animal) 
print(animals)
animals.clear() # ลบด้านในทั้งหมด and .del ลบ ตัวแปร 
print(animals)
# copy 
x=animals.copy()
print(x)