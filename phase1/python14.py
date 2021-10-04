j=0
for i in range(2,100):
    if not i%2 ==0 :
        if not i%3 == 0 :
            if not i%5 == 0:
                if not i%7 == 0:
                    print(i) 
                    j+=1
print(j)              
