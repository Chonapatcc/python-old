# pass in function

def numbers(number):
    pass


#lambda function (anonymous function)

'''
lambda argument : expression
'''
x=lambda name:name
sum=lambda x,y :x*y

def power(x):
    return lambda a:x**a
y=power(2)
result=y(2)

print(result)