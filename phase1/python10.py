#fahrenheit and celsius 
#formulas c=(f-32)*(5/9)
# f=c*(9/5)+32

temp=input("ป้อนองศา :")

degree=int(temp[:-1])
unit=temp[-1].upper()

if unit=="C":
    degree=(degree*9)/5+32
    print(degree,"F")

if unit=="F":
    degree=(degree-32)*(5/9)
    print(degree,"C")
