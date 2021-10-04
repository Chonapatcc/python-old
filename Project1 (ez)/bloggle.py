def find(x):
    lis=[]
    for y in x.split(", "):
        w=[]
        for z in y:
            w.append(z.lower())
        lis+=w
    dic=dict()
    for letter in lis:
        dic[letter]=dic.get(letter,0)+1
    return dic

def count(x):
    lis=list()
    words=x.split(",")
    for word in words:
        dic=dict()
        for letter in word:
            dic[letter]=dic.get(letter,0)+1
        lis.append(dic)
    return lis

    
    
def solve(a,x,y):
    words=a.split(",")
    wordsdic=x
    letters=y
    lis=[]
    for num in range(len(words)):
        for letter in words[num]:
            s1=wordsdic[num].get(letter)
            s2=letters.get(letter)
            if s2==None:
                s2=0
            if s1>s2:
                lis.append(words[num])
    if len(lis)==0:
        print('true')
    else:
        long=[]
        for end in lis:
          if end in long:
            pass
          else:
            long.append(end)
        longman=""
        for ended in long:       
          longman+=ended+","
        longman=longman.rstrip(",")
        print(longman)

            

letters,words=["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]

letters=find(letters) # dic letters
wordsdic=count(words) # dic words in lis
solves=solve(words,wordsdic,letters)
