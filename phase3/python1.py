# try exception
'''
try:
    คำสั่งรันโปรแกรมปกติ 
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
'''

try:
    number1=int(input("ใส่เลข :"))
    number2=int(input("ใส่เลข :"))
    sum=number1/number2
    print(sum)
except ValueError:
    print("ต้องป้อนตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("หารศูนย์ไม่ได้")
except TypeError:
    print("ชนิดข้อมูลไม่ตรง") # 100+"100"
#valueError =>ค่าผิดพลาด
#zerodivisionError