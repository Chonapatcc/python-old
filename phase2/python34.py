#fibonacci number

# Fn=Fn-1 +Fn-2
#f1=0 f2=1 f3=0+1=1 f4=2

def fibonacci(number):
    if number<=1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)

for i in range(10):
    print("รอบที่ ",i+1,fibonacci(i))
