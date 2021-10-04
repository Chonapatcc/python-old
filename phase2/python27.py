#list and tuple parameter 
# ใช้ function ร่วม กับ list

def animal(item):
    for i in range(len(item)):
        print("ตัวที่",i+1,"=",item[i])
    
animals=["cat","dog"] # ใช้ tuple หรือ list
animal(animals)