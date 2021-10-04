# สร้าง exception ด้วย raise

while True:
    try:
        name=input("yourname :")
        if name=="Chonapatc":
            raise Exception("มีชื่อนี้แล้ว")
        
        num1=int(input("num1 :"))
        num2=int(input("num2 :"))
        if num1==0 and num2==0:
            break
        if num1<0 and num2<0:
            raise Exception("ใส่ค่ามากกว่า 0")
        result=num1/num2
        print(result)
    except Exception as a:
        print(a)
    finally:  
        print("done")  