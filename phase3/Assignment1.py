#ฝากเงินธนาคาร

account={"Chonapatc":1000,"kilito":2000}

def balance():
    accountname=input("accountname :")
    print("ยอดเงิน :",account[accountname])

def deposit(money):
    accountname=input("accountname :")
    if money<=0:
        raise Exception ("ต้องมีค่าเป็นบวก ")
    print("ฝากเงินเข้าบันชี:",money)
    account[accountname]+=money

def withdraw(money):
    accountname=input("accountname :")
    if money<=0:
        raise Exception ("ต้องมีค่าเป็นบวก ")
    elif money>account[accountname]:
        raise Exception ("ยอดเงินไม่พอ")

    print("ถอนเงิน",money)
    account[accountname]-=money

def transfer(money):
    accountname=input("accountname :")
    if money<=0:
        raise Exception ("ต้องมีค่าเป็นบวก ")
    elif money>account[accountname]:
        raise Exception ("ยอดเงินไม่พอ")

    print("โอนเงิน",money)
    account[accountname]-=money
    nameaccounttotransfer=input("accountname to  transfer:")
    account[nameaccounttotransfer]+=money

numbers=int(input("1:ดูยอดเงิน 2:ฝาก 3:ถอน 4:โอน ="))
try:
    if numbers==1:
        balance()
    elif numbers==2:
        money=int(input("จำนวนเงิน :"))
        deposit(money)
    elif numbers==3:
        money=int(input("จำนวนเงิน :"))
        withdraw(money)
    elif numbers==4:
        money=int(input("จำนวนเงิน :"))
        transfer(money)
except Exception as a:
    print(a)

