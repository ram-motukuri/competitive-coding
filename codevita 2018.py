def product(list):
    p = 1
    for i in list:
        p *= i
    return p
import itertools
items= []
c=[]
com1=[]
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
N,P,Q=map(int,input("").split(","))
if(N<=300 and P<=50 and Q<=50 and P in prime and Q in prime):
    for i in range(N):
        k=int(input())
        items.append(k)
    for i in range(N+1):
        print(i)
        if(i>1):
            print(i)
            com=list(itertools.combinations(items,i))
            com1=com1+com
            com=[]
    print(com1)
    for j in range(len(com1)):
        a=list(com1[j])
        b=product(a)
        c.append(b)
    mul=P*Q
    count=0
    for x in c:
        if(mul!=0 and x%mul==0):
            count=count+1
    print(count%1009)
    
        
        
        
        
        
    


    
    
