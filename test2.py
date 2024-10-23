a=open("sigma.txt","r").readlines()
a=[x.strip().split(" ") for x in a]
b=0
wynik=0
e=dict()
licznik=len(a)


for x in a:
    if x[0] == 'zatrudniam':
        e.update({str(x[1]):int(x[2])})
        wynik+=int(x[2])*licznik
        
    else:
        wynik=wynik-(e[x[1]]*(licznik-1))
    licznik= licznik - 1
print(wynik)
