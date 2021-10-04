# recursive function วนเวียน

# หาจุดวนซ้ำ 
# หาจุดออกจาก function
# ต้องมีparameter
#1-5 โดยไม่ใช้ loop

def addnumber(number):
    if number==5 :
        return
    print(number) # 0
    number+=1 #1
    addnumber(number)


def summation(number):
    if number==1:
        return number 
    else:
        return number+summation(number-1)

    
x=summation(10)
print(x)