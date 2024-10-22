a=open("sigma.txt","r").readlines()
def liczbyper(n):
    global liczby
    liczby = list()
    for x in range(2,n+1):
        liczby.append(x)
    for x in liczby:
        if x % 2 == 1 or x == 2:
            for i in range(2,n+1):
                d=x*i
                try:
                    liczby.remove(d)
                except:
                    pass
        else:
            continue
     
licz=set()      
b=list()
c=list()
licznik=1
for x in a:
    if licznik % 2 == 0:
        
        b.append(x.strip().split(" "))
    else:
        c.append(x.strip().split(" "))
        
    licznik +=1
licznik2=0
while licznik2 < len(c):
    for x in c:
        ilosc=x[0]
        liczbyper(int(ilosc))
        liczby = set(liczby)
        for x in b[licznik2]:
            licz.add(int(x))
        if liczby < licz:
            print("TAK")
        else:
            print("NIE")
    licznik2 +=1
    
