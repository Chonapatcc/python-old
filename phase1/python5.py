# if ซ้อน if
name=input("ชื่อของคุณ :")

age= int(input("ป้อนอายุของคุณ :"))

sex= int(input("เพศของคุณ ชาย= 1 หญิง = 2 :" ))

if age<= 15 : 
    if sex==1 :
        print ("เด็กชาย ",name)
    elif sex==2 :
        print("เด็กหญิง",name)
elif age >= 16 :
    if sex==1 :
        print ("นาย ",name)
    elif sex==2 :
        print("นางสาว",name)
