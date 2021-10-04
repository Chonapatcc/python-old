# หาค่าเลขยกกำลัง

number=[1,2,3,4,5]
#ปกติ 
for i in range(len(number)):
    number[i]=number[i]**2
print(number)

# แบบ ลด รูป

number=[i*i for i in number]
print (number)