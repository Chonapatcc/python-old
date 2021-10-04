# คำนวณเกรด
'''try:
    fw=open("score.txt","w",encoding="utf-8")
    while True:
        studentid=input("ป้อนid:")
        if studentid=="exis":
            break
        score=input("ป้อนคะแนน:")
        fw.writelines(studentid+"\t"+score+"\n")
    fw.close()
except Exception as a:
    print(a)'''
try:
    fr=open("score.txt","r",encoding="utf-8")
    fw=open("grade.txt","w",encoding="utf-8")
    grade=None
    for line in fr.readlines():
        studentid=line[:-4].strip()
        score=line[-4:].strip()
        score=int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<80:
            grade="B"
        elif score>=60 and score<70:
            grade="C"
        elif score>=50 and score<60:
            grade="D"
        else:
            grade="F"
        fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fw.close
except Exception as a:
    print(a)