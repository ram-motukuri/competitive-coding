n=int(input())
q=[]
if(1<=n<=100):
    for i in range(n):
        k=input().split(" ")
        if((2<=int(k[0])<=1000) and (2<=int(k[1])<=int(k[0]))):
            m=input().split(" ")
            for i in range(len(m)):
                m[i]=int(m[i])
            for i in m:
                if(m.count(i)>=int(k[1])):
                    v.append(0)
                    break
            else:
                p=m.sort()
                for i in range(int(k[1])):
                    s=0
                    l=m[i:int(k[1])+i-1]
                    for i in range(len(l)-1):
                        s=s+l[len(l)-1]-l[i]
                    q.append(s)
                    if(s==1):
                        break
                print("Case #"+str(i+1)+": "+str(min(q)))
        k=[]
        m=[]
        p=[]
        l=[]
        q=[]
                
                
    
