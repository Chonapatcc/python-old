# หา ค่า bmi fomular = weight/height**2(m)

weight=int(input("น้ำหนักของคุณ ="))
height=int(input("ส่วนสูงของคุณ ="))/100

bmi = weight/(height**2)

if bmi<= 18.4 :
    print("ค่า bmi =",bmi,"น้ำหหนักต่ำกว่าเกณ")
elif bmi >=18.5 and bmi <= 22.9 :
    print("ค่า bmi =",bmi,"สมส่วน")
elif bmi >=23.0 and bmi <= 24.9 :
    print("ค่า bmi =",bmi,"น้ำหนักเกิน")
else :
    print("ค่า bmi =",bmi,"โรคอ้วน")