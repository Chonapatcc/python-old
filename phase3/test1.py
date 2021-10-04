n=input()
num=0
for i in range(int(n)):
    if i==0:
        num+=12
    else:
        num+=12/(2*i)
print(num)