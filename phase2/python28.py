#function return ค่า
'''
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการรับค่าเข้าไปทำงาน
def name(a,b):

3.รับค่าเข้าไปทำงาน และส่งออกมา
def add(a,b):
    return a+b
    
#print(add(1,2))
x=add(1,2)
print(x)
4. ไม่มีการรับค่าเข้ามาแต่ส่งค่าออกไป
def shownumber():
    return 500

x=shownumber()
print(x)
'''

#เช็คถูกหวย

def randomnumber(x):
    if x==1456:
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0
money=randomnumber(145)
print("ได้เงิน :",money)