#function เรียก function

def comparemaxthree(x,y,z):
    return comparemax(comparemax(x,y),z) 
#a=comparemax(x,y)  
#b=comparemax(a,z)   
#return b
def comparemax(x,y):
    if x>y:
        return x
    else:
        return y

max=comparemaxthree(10,20,30)
print("ค่ามากสุด :",max)