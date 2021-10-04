# ค้นหา เบอ โทรสับ
data={"เหตุด่วน":191,"ตำรวจทางหลวง":1193}

def serchnumber(text):
    for key,value in data.items():
        if x==key:
            print("เบอร์ติดต่อ",value)
            return
        else:
            print("ไม่มีข้อมูล")
            return 
        
x=input("ใส่ข้อความ :")

serchnumber(x)
