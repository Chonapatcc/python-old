# dict รวมความสามารถ ของ set และ tuple
lis=[1,2,3,4]
tup=(1,2,3,4)
print(lis)
print(tup)
#หา index แล้วเสียเวลา เลย มี dict
#dictionary => key,value
#ตัวแปร={key:value,key:value}
colors={"red":"แดง","green":"เขียว"}
print(colors["red"]) #print(ตัวแปร[key])

animals=dict(cat="แมว",dog="หมา")
print(animals["cat"])
print(animals.get("cat"))
#การแก้ไขข้อมูล
animals["cat"]="แมวสีขาว"
print(animals)
# เพิ่มข้อมูล key ซ้ำ update
colors.update({"catter":"badder"})
print(colors)
#loop
#for i in colors: เอาแค่ key

#for i in colors.values(): เอาvalues
#for i in colors.keys(): เอา keys
# เอา ทั้ง key and value
for k,v in colors.items():
    print("key :",k,"value :",v)
    






























