def liczciagi(ciag):
    if len(ciag)== 0:
        print("nieprawidłowy ciag")  
    else:
        print(ciag)
        print("suma ciagu wynosi " + str(sum(ciag)))
        print("sredni wyraz ciagu wynosi " + str(sum(ciag)/len(ciag)))
        try:
            if int(ciag[0])<int(ciag[1])>int(ciag[2]) or int(ciag[0])>int(ciag[1])<int(ciag[2]):
                print("ciag sinusoidalny")
            elif int(ciag[0])<int(ciag[1]):
                print("ciag rosnacy")
            elif int(ciag[0])>int(ciag[1]):
                print("ciag malejacy")
            else:
                print("ciag stały")
        except:
            try:
                if int(ciag[0])<int(ciag[1]):
                    print("ciag rosnacy")
                elif int(ciag[0])>int(ciag[1]):
                    print("ciag malejacy")
                else:
                    print("ciag stały")
            except:
                print("ciag stały")
def ciaga(n,m,q=1,x="liczba"):
    if x=="liczba":
        ciag = [x for x in range(n,m,q)]
        liczciagi(ciag)
    else:
        ciag=[n]
        while m > len(ciag):
            n=n+q
            ciag.append(n)
        liczciagi(ciag)
def ciagg(n,m,q=1,x="liczba"):
    ciag=[n]
    if x =="liczba":
        while m > n:
            n=n*q
            ciag.append(n)
        liczciagi(ciag)
    else:
        while m > len(ciag):
            n=n*q
            ciag.append(n)
        liczciagi(ciag)
ciaga(n,m,q,x)

