from itertools import combinations
t=int(input())
for x in range(t):
    a=int(input())
    if(a<6):
        b=list(map(int,input().split()))
        d=[]
        b=sorted(b)[::-1]
        for k in range(0,len(b)):
            c=list(combinations(b,len(b)-k))
            for j in c:
                a1=[]
                a2=set()
                for i in j:
                    a1=a1+list(set(str(i)))
                    a2=a2|set(str(i))
                if(len(a1)==len(a2)):
                    print(sum(j),end="")
                    print("")
                    break
            if(len(a1)==len(a2)):
                break
    elif(a>5 and a<15):
        b=list(map(int,input().split()))
        b=sorted(b)[::-1]
        p=0
        f=[]
        while(p<3):
            d=list(str(b[0]))
            e=[b[0]]
            for i in b:
                for j in list(str(i)):
                    if(j in d):
                        break
                else:
                    d=d+list(str(i))
                    e.append(i)
            f.append(sum(e))
            b.remove(b[0])
            p=p+1
        print(max(f),end="")
        print("")
    else:
        b=list(map(int,input().split()))
        b=sorted(b)[::-1]
        d=list(str(b[0]))
        e=[b[0]]
        for i in b:
            for j in list(str(i)):
                if(j in d):
                    break
            else:
                d=d+list(str(i))
                e.append(i)
        print(sum(e),end="")
        print("")
