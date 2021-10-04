#keyword argument
def displaydata(fname,lname,city):
    print("ชื่อ",fname)
    print("นามสกุล",lname)
    print("เมือง",city)

displaydata("chonapat","chotikulrat","city")
displaydata(city="city",fname="chonapat",lname="chotikulrat")
#สามารถ กำหนดก็ได้ โดย อะไรขึ้นก่อนก็ได้