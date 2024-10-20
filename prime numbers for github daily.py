def prime_numbers(n):
    number=[x for x in range(n+1)]
    number.pop(0)
    number.pop(0)
    for x in number:
        for i in range(2,n+1):
            try:
                a=i*x
                number.remove(a)
            except:
                continue
    return number
