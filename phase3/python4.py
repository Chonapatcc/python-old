#try except ร่วมกับ while

while True:
    try:
        number1=int(input("ใส่เลข :"))
        number2=int(input("ใส่เลข :"))
        if number1==0 and number2==0:
            break
        sum=number1/number2
        print(sum)
    except Exception as e: # บอกจุดผิดพลาด
        print(e)
    finally:
        print("ทำงานต่อไป")