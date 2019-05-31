import operator
from functools import reduce
T=int(input())
ans=[]
v=(10**9)+7
if(0<T<11):
    for a in range(T):
        t=0
        num=[]
        n,k=map(int,input("").split(" "))
        if(1<=n<=10**6 and 1<=k<=10):
            num = list(map(int, input().split()))
            for i in range(n-k):
                p=len(num)
                q=num[t:p]
                pro=reduce((lambda x, y: x * y),q)
                t=t+1
                num.append(pro%v)
            ans.append(num[len(num)-1])
    for j in ans:
        print(j%v)
    
