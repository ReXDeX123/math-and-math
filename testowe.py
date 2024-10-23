a=open("sigma.txt","r").readlines()

a=[x.strip().split(" ") for x in a]
b=0
c=0
e=dict()
for x in a:
    if x[0] == 'zatrudniam':
        b+=int(x[2])
        c+=b
        
        e.update({str(x[1]):int(x[2])})
    elif x[0] == 'zwalniam':
        
        b= b-e[x[1]]
        c+=b+e[x[1]]
print(c)       
