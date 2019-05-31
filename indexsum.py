def minimum(l,val):
        while val in l:
            l.remove(val)
        return(min(l))
n=int(input())
l=[]
for i in range(n):
    k=int(input())
    l.append(k)
for i in l:
    if(l.index(i)>i):
        l[l.index(i)]=0
if(l[0]==0):
    print(max(l)-min(l))
else:
    print(max(l)-minimum(l,0))
    
