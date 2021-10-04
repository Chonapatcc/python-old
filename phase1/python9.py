#นับจำนวนคำ count
name="ไก่ แมว ไก่ ไก่ หนู"

print(name.count("ไก่"))

#เช็คคำขึ้นต้น 
name = "นาย นหกาดกนยมอแมห ยนากยด"

print(name.startswith("นาย"))
#เช็คคำลงท้าย 
name ="dog dog cat"
print(name.endswith("cat"))
if name.endswith("cat") :
    print("สุดยอด")
else :
    print("แย่")