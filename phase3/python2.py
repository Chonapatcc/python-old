# exception บอกจุดผิดพลาด

try:
    number1=int(input("ใส่เลข :"))
    number2=int(input("ใส่เลข :"))
    sum=number1/number2
    print(sum)
except Exception as e: # บอกจุดผิดพลาด
    print(e)
else:
    print("จบโปรแกรม")
    