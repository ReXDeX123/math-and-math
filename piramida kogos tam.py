def piramida(y):
    x=[1,1]
    lista=[1,1]
    while int(y) > int(len(x))-1:
        dl=len(x)
        for i in range(0,dl):
            try:
                a=x[i] + x[i+1]
                lista.insert(i+1,a)
            except:
                pass
        x=lista.copy()
        wynik=lista.copy()
        lista=[1,1]
    print(wynik)
a=input("pisz ile chcesz piramidy ")
print(piramida(a))   
