def jio1(l1):
    u=[]
    v=[]
    k=sorted(l1)[::-1]
    a=l1.index(k[0])
    u.append(k[0])
    v.append(a)
    l1[a]=0
    for i in range(1,len(k)):
        if(k[i]>0):
            b=l1.index(k[i])
            if((b-1 not in v) and (b+1 not in v)):
                v.append(b)
                u.append(k[i])
                l1[b]=0
            else:
                l1[b]=0
    return(sum(u),v)
def jio2(l2):
    s=[]
    w=[]
    k=sorted(l2)[::-1]
    p=k.count(k[0])
    if(p<len(k)):
        x=l2.index(k[p])
        s.append(x)
        w.append(k[p])
        l2[x]=0
        for i in range(p+1,len(k)):
            if(k[i]>0):
                b=l2.index(k[i])
                if((b-1 not in s) and (b+1 not in s)):
                    s.append(b)
                    w.append(k[i])
                    l2[b]=0
                else:
                    l2[b]=0
    return(sum(w),s)
t=int(input())
for y in range(t):
    a=int(input())
    l = list(map(int, input().split()))
    l1=tuple(l)
    s1,s2=jio1(l)
    l2=list(l1)
    s3,s4=jio2(l2)
    l3=list(l1)
    if(s1==s3):
        s2.sort()
        s4.sort()
        if(l3[s2[0]]<l3[s4[0]]):
            for i in s2[::-1]:
                print(l3[i],end="")
        else:
            for i in s4[::-1]:
                print(l3[i],end="")
    else:
        s2.sort()
        for i in s2[::-1]:
            print(l3[i],end="")
    print("")

