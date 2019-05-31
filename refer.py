def mask(n):
    mas=0
    k=list(map(int,str(n)))
    k.reverse()
    for i in k:
        mas=mas|1<<i
    return mas

def dp(a,b,c):
    if(a==0):
        b[a]=0
        return b[a]
    if(b[a]!=-1):
        return b[a]
    res=0
    for i in c:
        bitmask=mask(i)
        if((a|bitmask)==a):
            res=max(dp(a^mask(i),b,c)+i,res)
    b[a]=res
    return b[a]

t=int(input())
for i in range(t):
    x=int(input())
    l=list(map(int,input().split()))
    memo=[-1]*1024
    res=0
    for i in range(1024):
        res=max(res,dp(i,memo,l))
    print(res,end="")
    print("")
