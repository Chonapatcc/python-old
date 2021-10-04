name = ("     cho4na4pa4t     ")   # index

print(name[-2:]) # ดึงถึง 0 
print(len(name)) # len หาความยาว คำ

name= name.strip() # strip = ลบช่องว่างซ็ายขวา
# lstrip = ลบ ช่องว่างซ๋าย rstrip = ลบช่ีองว่างขวา 
print(len(name))

# แปลง case
print(name.upper()) #ใหญุ่ทุกตัว
print(name.lower()) #เลก ทุกตัว
print(name.capitalize()) # ใหญ่ตัวแรก

#การแทนที่ replace count
print(name.replace("chon", "dog"))

print(name.replace("4"," ",2))

#การเช็คข้อความ 
dad = "ไก่กินงูอยู่ข้างถนน"
x= "ไก่" in dad
print(x)