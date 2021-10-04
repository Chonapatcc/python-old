# function หาผลรวม / ค่าเฉลีย

def number(x):
    total=0
    for i in x:
        total+=i
    avg=total/len(x)
    return avg,total

        
    


x=[1,2,3,4,5,6,7,8]
y,z=number(x)
print("ค่าเฉลีย :",y,"total",z)