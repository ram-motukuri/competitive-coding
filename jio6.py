from itertools import combinations
t=int(input())
l=[]
p=[]
for i in range(t):
    a=int(input())
    l.append(a)
f=int(input())
k=int(input())
c=list(map(list,combinations(l,k)))
for i in c:
    if(sum(i)%f==0):
        p.append(sum(i))
if(len(p)==0):
    print(str(-1),end="")
else:
    print(min(p),end="")
