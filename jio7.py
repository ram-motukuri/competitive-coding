a=int(input())
b=int(input())
c=int(input())
d=int(input())
p=0
l=[]
x=0
for i in range(a,b+1):
    for j in range(c,d+1):
        l.append([])
        l[x].append(i)
        l[x].append(j)
        x=x+1
for i in l:
    while(i[0]!=i[1]):
        i.sort()
        i[1]=i[1]-i[0]
        p=p+1
    else:
        p=p+1
print(a,b,c,d)
if(a==b or c==d):
    print(p*2,end="")
elif(a==b==c==d):
    print(p*4,end="")
else:
    print(p,end="")
