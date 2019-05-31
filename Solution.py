def hcf(x,y):
    n=max([x,y])
    m=min([x,y])
    while(m!=0):
        n,m=m,n%m
    return n
testcase=int(input())
alpha=dict()
resl=[]
while(testcase):
    inp=input().split(" ")
    N=int(inp[0])
    ln=int(inp[1])
    text=input().split(" ")
    primes=[]
    for i in range(ln):
        text[i]=int(text[i])
    for i in range(ln):
        if(i!=ln-1):
            primes.append(hcf(text[i],text[i+1]))
    primes.insert(0,int(text[0]/primes[0]))
    primes.append(int(text[ln-1]/primes[ln-1]))
    pr=sorted(primes)
    for i in pr:
        if(pr.count(i)>1):
            pr.remove(i)
    j=0
    res=""
    for i in range(65,91):
        alpha[pr[j]]=chr(i)
        j+=1
    for i in primes:
        res+=alpha[i]
    resl.append(res)
    testcase-=1
for i in range(len(resl)):
    print("Case #"+str(i+1)+": "+resl[i],sep="")
