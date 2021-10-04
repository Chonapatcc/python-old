try:
    f = open("student.txt", "r",encoding="utf-8")
    print(f.read()) #(num) ให้อ่านกี่ตัว #encoding="utf-8" ใช้ภาษาไทย
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")