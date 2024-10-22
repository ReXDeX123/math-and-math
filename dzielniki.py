def dzielniki(liczba,liczba2):
    c = set()
    d = set()
    for x in range(1,liczba+1):
        if liczba % x == 0:
            c.add(x)
        else:
            continue
    for x in range(1,liczba2+1):
        if liczba2 % x == 0:
            d.add(x)
        else:
            continue
        f=c & d
    print(";".join(str(x) for x in f))
dzielniki(2137,6969)

