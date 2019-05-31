t=int(input())
for k in range(t):
    n,p = map(int, input().split())
    l = list(map(int, input().split()))
    l=sorted(l, reverse=True)
    print(l)
    c=[]
    s=sum(l[1:p])
    print(s)
    for i in range(0,n-p+1):
        x=l[i]
        cc=x*(p-1) - s
        print(cc)
        c.append(cc)
        if i!=n-p:
            s-=l[i+1]
            s+=l[i+p]
    print("Case #"+str(k+1)+": "+str(min(c)))
