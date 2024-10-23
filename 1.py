a=open("sigma.txt","r").readlines()
a=[x.strip().split(" ") for x in a]
a=a[0]
b=dict()
c=list()
for x in a:
    if x not in b:
        b.update([(x,1)])
    else:
        b[x]=b[x]+1
for x in a:
    c.append(b[x])
print(";".join(str(x) for x in c))
