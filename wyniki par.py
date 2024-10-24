a=open("sigma.txt","r").readlines()

b=a[0]
a.pop(0)
b=b.strip().split()
b.pop(0)
b=b[0]
c=set()
c1=set()
for x in a:
    c.add(x.strip())
licznik=0
for x in c:
    for i in c:
        wynik=int(x)+int(i)
        if wynik == int(b):
            c1.add(x+"+"+i)
            if i!=x:
                try:
                    c1.remove(i+"+"+x)
                except:
                    pass
print(len(c1))

