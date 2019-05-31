a=list(input().split())
a1=tuple(a)
c2=list(a1)
b=list(input().split())
b1=[]
for i in b:
    b1.append(b.count(i))
a2=min(b1)
a3=b1.index(a2)
c=b[a3:len(b)+1]
del b[a3:len(b)+1]
b=c+b
for i in range(a2):
    s=a.index(b[0])
    v=c2[s:len(c2)+1]
    del c2[s:len(c2)+1]
    v=v+c2
    a[s]=0
    c2=list(a1)
    if(v==b):
        print("Yes",end="")
        break
else:
    print("No",end="")

    
    
