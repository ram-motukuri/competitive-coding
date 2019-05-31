while(1):
    str1=input()
    l1=[]
    l=[]
    k=0
    p=0
    for i in str1:
        l1.append(i)
    r=l1.index('a')
    temp=l1[:]
    temp.reverse()
    t=len(temp)-temp.index('u')
    for i in range(r,t):
        l.append(l1[i])
    n=[['a','a'],['a','e'],['e','e'],['e','i'],['i','i'],['i','o'],['o','o'],['o','u'],['u','u']]
    for i in range(len(l)-2):
        for j in range(len(l)-1):
            if((j+1+k)<=(len(l)-1)):
                m=[]
                m.append(l[k])
                m.append(l[j+1+k])
                print(m)
                if m in n:
                    if(m[0]!=m[1]):
                        k=l.index(m[1])
                        break
                else:
                    l[j+1]=0            
    q=l.count(0)
    print(q)
    print(len(l)-q)

        
        
    
