string=input("enter string : ")
l=list(string.split(" "))
n=[int(a) for a in l]
b=[int(a) for a in l]
k=[]
m=[]
a=len(l)
for i in n:
    k.append(i)
    a=i
    for j in b:
        if(a<j):
            k.append(j)
            a=k[-1]
    m.append(k)
    k=[]
    b.remove(i)
v=[len(a) for a in m]
s=max(v)
print(m[v.index(s)])



    
