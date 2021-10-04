# crack password 
import random

atmpassword="132"

result="" # keep result

while result!=atmpassword:
    result=""
    for letter in range(len(atmpassword)):
        crack=random.choice("123456789")
        result="".join(crack)+str(result)
        print("serch =",result)

print("password is =",result)

