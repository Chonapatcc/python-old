#return กระโดออกจาก function

def number(x):
    if len(str(x))<3:
        return
    
    if x==100:
        print("ถูกรางวัล")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0

x=int(input("Put your number :"))
money=number(x)
print("รางวัล",money) 