a=open("sigma.txt","r").readlines()
a.pop(0)
a=[x.strip().split(" ") for x in a]

a=a[0]
b=set()
c=[]
wynik=[]
testownik=0
for x in a:
    for i in b:
        if int(x) > int(i):
            c.append(int(i))
        for g in c:
            if int(g) < int(x):
                testownik+=1
    if testownik > 0:
        wynik.append(max(c))
    else:
        wynik.append(-1)
    testownik=0
    c=[]
    b.add(x)
    
print(" ".join(str(x) for x in wynik))
    
