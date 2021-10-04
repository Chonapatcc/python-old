# formula mg/h**2
#input
weight=int(input("Your weight(kg) :"))
height=int(input("Your height(cm)"))
# แปลง cm to m
height=height/100
#proccess
bmi=weight/(height**2)
print("BMI",bmi)
