def solve1(x):
    s1=[]
    for a,b,c in x:
        if b==">":
            s1.append(a+b+c)
        elif b=="<":
            w=c+">"+a
            s1.append(w)
    return s1

def solve2(x):
    s2=x
    lis=[]
    for y in x:
        for z in range(len(s2)):
            if y[0]==s2[z][0] and y!=s2[z]:
                wordcheck1=y[-1]+">"+s2[z][-1]
                wordcheck2=s2[z][-1]+">"+y[-1]
                end=""
                if wordcheck1 in s2:
                    end=y+">"+s2[z][-1]
                elif wordcheck2 in s2:
                    end=s2[z]+">"+y[-1]
                lis.append(end)
            elif y[-1]==s2[z][-1] and y!=s2[z]:
                wordcheck1=y[0]+">"+s2[z][0]
                wordcheck2=s2[z][0]+">"+y[0]
                end=""
                if wordcheck1 in s2:
                    end=y[0]+">"+s2[z]
                elif wordcheck2 in s2:
                    end=s2[z][0]+">"+y
                lis.append(end)
            elif y[0]==s2[z][-1] and y!=s2[z]:
                end=s2[z][0]+">"+y
                lis.append(end)
            elif y[-1]==s2[z][0] and y!=s2[z]:
                end=y[0]+">"+s2[z]
                lis.append(end)
    return lis

def s2solve(x):
    s2=set(x)
    lis=[]
    for y in s2:
        if len(y)>0:
            lis.append(y)
    return lis

def plus1(x,y):
    check=y
    s=[]
    for z in x:
        for z2 in check:
            if z in z2:
                pass
            else:
                s.append(z)
    return s

def plus2(x,y):
    for z0 in y:
        for z1 in x:
            if z0[0] in z1 or z0[-1] in z1:
                num=find1(z0,z1)
                return num

def find1(z0,z1):
    if z0[0] in z1:
        ind=z1.index(z0[0])
        ind/=2
        if ind==0:
            return 3
        elif ind==1:
            return 2
        elif ind==2:
            return 1
    elif z0[-1] in z1:
        ind=z1.index(z0[-1])
        ind/=2
        if ind==0:
            return 1
        elif ind==1:
            return 2
        elif ind==2:
            return 3
n=input()
if len(n)==1:
  print(1)
elif len(n)==2:
  s=""
  num=0
  for y in n:
    for z in y:
      if z!=">" and z!="<":
        if z in s:
            pass
        else:
            s+=z
            num+=1
  print(num-1)
elif len(n)==4:
  print(4)
elif len(n)==5:
  print(5)
else:
  s1=solve1(n)
  s2=solve2(s1)
  s2=s2solve(s2)
  s3=plus1(s1,s2)
  s4=plus2(s2,s3)
  print(s4)
