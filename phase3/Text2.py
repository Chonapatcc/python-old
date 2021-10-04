#การสร้้าง w= เขียน x =สร้าง
'''try:
    f = open("Tanawit.txt", "w",encoding="utf-8")
    f.write("Hello World")
    f.writelines("Cat")
    f.close()
    
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")'''

try: #w จะเขียนทับเลย แต่ถ้าต้องการเพิ่มข้อความต้องใช้ a
    fw=open("Tanawit.txt","a",encoding="utf-8")
    fw.write("ชาวโลก\n")
    fw.writelines(["cat","dog\n"])
    fw.close()
    fr=open("Tanawit.txt","r",encoding="utf-8")
    f=fr.read()
    fr.close()
    print(f)    
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")