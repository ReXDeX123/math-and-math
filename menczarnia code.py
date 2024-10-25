a=open("sigma.txt","r").readlines()
a=[x.strip().split(" ") for x in a]
b=[]
a=a[0]
wynik=set()
a=[int(x) for x in a]
while len(a)>0:
    for i in range(1,max(a)):
        b=a.copy()
        for x in range(0,len(b)):
            try:
                while b[x] + i != b[x+1]:
                    b.pop(x+1)
            except:
                pass
        wynik.add(len(b))
        if len(b) == 11:
            print(b)
    a.pop(0)
print(max(wynik))

