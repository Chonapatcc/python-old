animal = ["cat","dog","giraff"]

anime =["naruto","one peice","ao no exocist"]

#การลบข้อมูล remove,pop,del,clear
#remove ลบไปเลย
print("before",anime)
anime.remove("naruto")
print("after",anime)

#pop เอาตัว ขวาสุดออก
print(animal)
animal.pop()
print(animal)
#del เอาออก ตามindex หรือ จะลบทั้งหมดเลย
del animal[1]
print(animal)
del animal #deleted

#clear ลบสมาชิกออกเท่านั้น
anime.clear()
print(anime)