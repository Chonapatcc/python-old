# เกมทายลูกเต๋า

import random 

myrandom=random.randrange(1,7)

while True:
    number=int(input("ทายตัวเลข :"))
    if number<=0 :
        break
    correct=(number==myrandom)
    if correct:
        print("won")
    else:
        print("lose")