#finally  #ทำงานต่อไป 
#run คำสั่งที่ทำงานตลอดเวลา

try:
    number1=int(input("ใส่เลข :"))
    number2=int(input("ใส่เลข :"))
    sum=number1/number2
    print(sum)
except Exception as e: # บอกจุดผิดพลาด
    print(e)
finally:
    print("ทำงานต่อไป")