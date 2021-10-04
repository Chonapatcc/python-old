# function check ตัวอักษร ใหญ่ เล็ก

def word(title):
    result={"upper":0,"lower":0}
    for i in words:
        if i.isupper():
            result["upper"]+=1
        else:
            result["lower"]+=1
    return result

words="Catter"
x=word(words)
print(x)
