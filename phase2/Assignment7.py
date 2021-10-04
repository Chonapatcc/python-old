# จับ คู่คำ ทักทาย 
first=["hello","hi","nihao"]
second=["hell","hill","cao ni ma"]
twin=[]

# แบบปกติ
#for i in first :
#    for y in second :
  #      twin.append(i+y)

#print(twin)
 
# ลดรูป

result=[ i+y for i in first for y in second]

print(result)