# random function
import random 
# number
x=random.random() #0.0 - 1.0

#for i in range(10):
#    x=random.random()
 #   print(x)

# ระบุช่วง
#for i in range(10):
   # x=random.uniform(5,10)
    #print(x)

#ร่วมกับ range เป็น I (จำนวนเต้ม) 
#for i in range(10):
   # x=random.randrange(1,10,2) #(start,stop,step)
    #print(x)                   #step เพิ่มทีละ

# randint 
#for i in range(10):
 #   x=random.randint(1,10) #1-5
  #  print(x)

# random list
#item=[1,2,3,4,5,"A","B"]
#for i in range(10):
 #   x=random.choice(item)
  #  print(x)
# ลดรูป choice
# x=random.choice([2,3,5,"acat"])
# x=random.choice("1245cawft4va")

# สุ่มแล้วสลับ
item=[1,2,3,4,5,"A","B"]
for i in range(10):
    random.shuffle(item)
    print(item)
